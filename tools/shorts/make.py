# Fabrique les Shorts verticaux (1080x1920, 30 fps) de Door Knight à partir des captures du jeu.
# usage: python3 make.py <nom>   (ou "all")
import os, sys, subprocess, json, math
sys.path.insert(0, '/root/shorts')
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from ovlib import gold_layer, cin, inter

W, H = 1080, 1920
CAP = '/root/cap'
AUD = '/home/claude/door-knight/public/audio'
OUT = '/root/shorts/out'
TMP = '/root/shorts/tmp'
os.makedirs(OUT, exist_ok=True); os.makedirs(TMP, exist_ok=True)
END = '/root/trailer/ov/P-en-end.png'

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-2000:]); raise SystemExit(cmd[:3])

def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout.strip())

def overlay(name, lines):
    """lines: list of (y, text, kind, size) ; kind gold|white. Rend un PNG 1080x1920 transparent."""
    items = []
    for y, text, kind, size in lines:
        items.append(((W // 2, y), text, cin(size) if kind == 'gold' else inter(size), kind))
    p = f'/root/shorts/ov/{name}.png'
    gold_layer(W, H, items).save(p)
    return p

def seg_from_frames(d, start, n, out, fade_in=0.0, fade_out=0.0):
    """Encode n frames à partir de start (30 fps) d'un dossier de captures."""
    run(['ffmpeg', '-v', 'error', '-y', '-framerate', '30', '-start_number', str(start), '-i', f'{CAP}/{d}/f%05d.jpg', '-frames:v', str(n),
         '-vf', f'scale={W}:{H}' + (f',fade=t=in:d={fade_in}' if fade_in else '') + (f',fade=t=out:st={n/30-fade_out:.3f}:d={fade_out}' if fade_out else ''),
         '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-pix_fmt', 'yuv420p', '-an', out])

def seg_from_image(img, secs, out, zoom=1.08, fit='cover'):
    """Image fixe avec un lent zoom (Ken Burns), fond flou si l'image ne couvre pas."""
    im = Image.open(img).convert('RGB')
    bg = im.resize((W, H)).filter(ImageFilter.GaussianBlur(40))
    r = max(W / im.width, H / im.height) if fit == 'cover' else min(W / im.width, (H * 0.8) / im.height)
    fg = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    p = f'{TMP}/{os.path.basename(out)}.png'; bg.save(p)
    n = int(secs * 30)
    run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', p, '-frames:v', str(n),
         '-vf', f"scale={int(W*zoom)}:{int(H*zoom)},zoompan=z='1+({zoom}-1)*on/{n}':d={n}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps=30,fade=t=in:d=0.3,fade=t=out:st={secs-0.3:.2f}:d=0.3",
         '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-pix_fmt', 'yuv420p', '-an', out])

def seg_end(secs, out):
    n = int(secs * 30)
    run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', END, '-frames:v', str(n), '-vf', f'scale={W}:{H},fade=t=in:d=0.4',
         '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-pix_fmt', 'yuv420p', '-an', out])

def assemble(name, segs, overlays, music, voices, music_vol=0.5, duck=0.25):
    """segs: liste de mp4 ; overlays: [(png, start, end)] ; voices: [(mp3, start)]."""
    lst = f'{TMP}/{name}.txt'
    open(lst, 'w').write(''.join(f"file '{s}'\n" for s in segs))
    vid = f'{TMP}/{name}-v.mp4'
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', vid])
    total = dur(vid)
    # overlays
    inputs = ['-i', vid]; fc = []; cur = '[0:v]'
    for i, (png, s, e) in enumerate(overlays):
        inputs += ['-i', png]
        fc.append(f"{cur}[{i+1}:v]overlay=0:0:enable='between(t,{s},{e})'[v{i}]"); cur = f'[v{i}]'
    # audio: musique en boucle + voix
    ai = len(overlays) + 1
    inputs += ['-stream_loop', '-1', '-i', music]
    a = [f"[{ai}:a]atrim=0:{total},afade=t=in:d=0.5,afade=t=out:st={total-1.2:.2f}:d=1.2,volume={music_vol}[m]"]
    vlabels = []
    for j, (mp3, s) in enumerate(voices):
        inputs += ['-i', mp3]
        a.append(f"[{ai+1+j}:a]adelay={int(s*1000)}|{int(s*1000)},volume=1.6[vo{j}]"); vlabels.append(f'[vo{j}]')
    if vlabels:
        a.append(''.join(vlabels) + f"amix=inputs={len(vlabels)}:normalize=0,apad=whole_dur={total}[vo]")
        a.append(f"[m][vo]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=400:makeup=1[md]")
        a.append(f"[md][vo]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]")
    else:
        a.append("[m]alimiter=limit=0.95[a]")
    # sidechaincompress consomme [vo] : il faut le dupliquer
    if vlabels:
        a[-3] = a[-3].replace('[vo]', '[vo][vo2]').replace(f"apad=whole_dur={total}[vo][vo2]", f"apad=whole_dur={total},asplit=2[vo][vo2]")
        a[-1] = a[-1].replace('[md][vo]', '[md][vo2]')
    out = f'{OUT}/{name}.mp4'
    run(['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', ';'.join(fc + a), '-map', cur if overlays else '[0:v]', '-map', '[a]',
         '-c:v', 'libx264', '-preset', 'slow', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', f'{total:.2f}', out])
    print(name, f'{total:.1f}s', os.path.getsize(out) // 1024, 'KB')
    return out

def hook(name, l1, l2=None, y=230, size=92):
    if len(l1) > 12 and size > 70: size = 70
    lines = [(y, l1, 'gold', size)]
    if l2: lines.append((y + int(size * 1.2), l2, 'white', 48))
    return overlay(name, lines)

def boss_short(name, cap, voice_no, music, hook1, hook2, fight_frames=270, start=0):
    segs = [f'{TMP}/{name}-a.mp4', f'{TMP}/{name}-e.mp4']
    seg_from_frames(cap, start, fight_frames, segs[0], fade_in=0.2, fade_out=0.3)
    seg_end(3.0, segs[1])
    ovs = [(hook(name + '-h', hook1, hook2), 0.3, 1.9), (hook(name + '-f', 'FREE BETA · iPhone & iPad', 'doorknight.games', y=1540, size=58), 5.5, 9.0)]
    return assemble(name, segs, ovs, f'{AUD}/music/{music}', [(f'{AUD}/voice/en/gardien_{voice_no}.mp3', 2.0)], music_vol=0.45)

def montage_short(name, clips, hook1, hook2, music, cta_at=None):
    segs = []
    for i, (cap, start, n) in enumerate(clips):
        p = f'{TMP}/{name}-{i}.mp4'; seg_from_frames(cap, start, n, p, fade_in=0.15 if i == 0 else 0, fade_out=0.15); segs.append(p)
    e = f'{TMP}/{name}-e.mp4'; seg_end(3.0, e); segs.append(e)
    total = sum(n for _, _, n in clips) / 30
    ovs = [(hook(name + '-h', hook1, hook2), 0.3, 2.6), (hook(name + '-f', 'FREE BETA · iPhone & iPad', 'doorknight.games', y=1540, size=58), cta_at or total - 3.5, total)]
    return assemble(name, segs, ovs, f'{AUD}/music/{music}', [], music_vol=0.7)

def image_short(name, images, hook1, hook2, music, secs=1.6):
    """images: [(path, label)]"""
    segs = []; ovs = [(hook(name + '-h', hook1, hook2), 0.3, 2.6)]
    t = 0.0
    for i, (img, label) in enumerate(images):
        p = f'{TMP}/{name}-{i}.mp4'; seg_from_image(img, secs, p, fit='contain'); segs.append(p)
        if label: ovs.append((overlay(f'{name}-l{i}', [(1420, label, 'gold', 76)]), t + 0.2, t + secs - 0.2))
        t += secs
    e = f'{TMP}/{name}-e.mp4'; seg_end(3.0, e); segs.append(e)
    ovs.append((hook(name + '-f', 'FREE BETA · iPhone & iPad', 'doorknight.games', y=1540, size=58), t - 3.4, t))
    return assemble(name, segs, ovs, f'{AUD}/music/{music}', [], music_vol=0.7)

SHORTS = {
    'guardian-black-knight': lambda: boss_short('guardian-black-knight', 'port-b80', '08', 'boss_chevalier_noir.mp3', 'DOOR 80', 'He talks before he fights'),
    'guardian-dragon': lambda: boss_short('guardian-dragon', 'port-b100', '10', 'boss_dragon.mp3', 'DOOR 100', 'The Ancestral Dragon'),
    'guardian-colossus': lambda: boss_short('guardian-colossus', 'port-b50', '05', 'boss_gardien.mp3', 'CAN YOU PASS DOOR 50?', 'The Summit Colossus'),
    'guardian-slime-king': lambda: boss_short('guardian-slime-king', 'port-b10', '01', 'boss_gardien.mp3', 'YOUR FIRST GUARDIAN', 'Door 10 · the Slime King', fight_frames=240),
    'monsters-spells': lambda: montage_short('monsters-spells', [('port-m23', 30, 120), ('port-m45', 30, 120), ('port-m72', 30, 120), ('port-m95', 30, 120)],
                                             'EVERY MONSTER', 'has its own spell · watch the ground', 'world03_marais.mp3'),
    'ten-worlds': lambda: montage_short('ten-worlds', [('port-b10', 90, 45), ('port-m15', 60, 45), ('port-m23', 60, 45), ('port-4', 30, 45), ('port-m45', 60, 45),
                                                        ('port-5', 30, 45), ('port-1', 30, 45), ('port-m72', 60, 45), ('port-m88', 60, 45), ('port-b100', 180, 45)],
                                        '10 WORLDS', '100 doors · then it loops, harder', 'theme.mp3', cta_at=11.5),
    'camp': lambda: image_short('camp', [('/root/site/img/camp/camp-meadow.webp', 'MEADOW'), ('/root/site/img/camp/camp-autumn.webp', 'AUTUMN'), ('/root/site/img/camp/camp-snow.webp', 'SNOW'),
                                         ('/root/site/img/camp/camp-arcane.webp', 'ARCANE'), ('/root/site/img/camp/raid.webp', 'RAID EVERY 3 HOURS')],
                                'BETWEEN DOORS', 'build your camp · it works while you sleep', 'campement.mp3', secs=2.2),
}

if __name__ == '__main__':
    names = list(SHORTS) if sys.argv[1] == 'all' else sys.argv[1:]
    for n in names: SHORTS[n]()
