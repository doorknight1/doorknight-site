from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
def cin(s): return ImageFont.truetype('/root/shorts/cinzel-latin-900-normal.ttf',s)
def inter(s): return ImageFont.truetype('/root/shorts/inter-latin-600-normal.ttf',s)
def gold_layer(W,H,items):
    im=Image.new('RGBA',(W,H),(0,0,0,0))
    for (xy,text,font,kind) in items:
        mask=Image.new('L',(W,H),0); ImageDraw.Draw(mask).text(xy,text,font=font,fill=255,anchor='mm')
        bb=mask.getbbox()
        sh=mask.filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.8))
        im.alpha_composite(Image.merge('RGBA',[Image.new('L',(W,H),0)]*3+[sh]))
        if kind=='gold':
            g=Image.new('RGB',(W,H)); gd=ImageDraw.Draw(g); cols=[(0xff,0xf4,0xcf),(0xf0,0xc4,0x5a),(0xc0,0x86,0x2a)]
            for y in range(bb[1],bb[3]+1):
                t=(y-bb[1])/max(1,bb[3]-bb[1]); a,b,u=(cols[0],cols[1],t*2) if t<.5 else (cols[1],cols[2],(t-.5)*2)
                gd.line([(0,y),(W,y)],fill=tuple(int(a[i]*(1-u)+b[i]*u) for i in range(3)))
            glow=mask.filter(ImageFilter.GaussianBlur(18)).point(lambda v:int(v*0.45))
            im.alpha_composite(Image.merge('RGBA',[Image.new('L',(W,H),c) for c in (0xf0,0xc4,0x5a)]+[glow]))
            im.alpha_composite(Image.merge('RGBA',list(g.split())+[mask]))
        else:
            im.alpha_composite(Image.merge('RGBA',[Image.new('L',(W,H),c) for c in (0xec,0xe8,0xf8)]+[mask]))
    return im
