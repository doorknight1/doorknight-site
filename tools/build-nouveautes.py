#!/usr/bin/env python3
"""Génère la rubrique Nouveautés à partir de tools/nouveautes.json (copie du fichier du jeu).

- /nouveautes/ (français) et /en/nouveautes/ (anglais, traductions dans tools/news_i18n.py)
- le bloc « Nouveautés » de l'accueil (index.html, entre <!-- nouveautes:start --> et <!-- nouveautes:end -->),
  avec les traductions EN/ES/DE ajoutées au dictionnaire i18nData de la page.
- les entrées du sitemap (bloc <!-- nouveautes -->).

À relancer après chaque mise à jour du fichier du jeu :
  cp ../door-knight/nouveautes/nouveautes.json tools/nouveautes.json  (+ images dans img/news/, voir README)
  python3 tools/build-nouveautes.py && python3 tools/build-langues.py
"""
import os, re, sys, json, html, datetime, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://doorknight.games'
TODAY = datetime.date.today().isoformat()
HOME_N = 6  # entrées mises en avant sur l'accueil

spec = importlib.util.spec_from_file_location('bg', os.path.join(ROOT, 'tools', 'build-guides.py'))
bg = importlib.util.module_from_spec(spec); spec.loader.exec_module(bg)
from news_i18n import CAT, EN, ES, DE

UI = {
    'fr': {'title': 'Nouveautés de Door Knight · toutes les mises à jour du jeu', 'desc': "Tout ce qui change dans Door Knight, version après version : héros, monstres, mondes, campement, musiques, corrections. Mis à jour à chaque patch de la bêta.",
           'h1': 'Nouveautés', 'eyebrow': 'Journal des mises à jour', 'lede': "Tout ce qui change dans le jeu, patch après patch. Les nouveautés sont aussi annoncées dans #nouveautés sur le Discord.",
           'crumb': 'Nouveautés', 'fr_only': ''},
    'en': {'title': "What's new in Door Knight · every game update", 'desc': "Everything that changes in Door Knight, version after version: heroes, monsters, worlds, camp, music, fixes. Updated with every beta patch.",
           'h1': "What's new", 'eyebrow': 'Update log', 'lede': "Everything that changes in the game, patch after patch. Updates are also announced in #nouveautés on the Discord.",
           'crumb': "What's new", 'fr_only': '(in French)'},
}
MONTHS = {'fr': ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'],
          'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
          'es': ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
          'de': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']}

def esc(x): return html.escape(x, quote=True)

def date_txt(d, lang):
    y, m, j = d.split('-'); j = int(j); m = MONTHS[lang][int(m) - 1]
    if lang == 'fr': return f"{j if j != 1 else '1er'} {m} {y}"
    if lang == 'en': return f"{m} {j}, {y}"
    if lang == 'es': return f"{j} de {m} de {y}"
    return f"{j}. {m} {y}"

def md(text):
    """Mini-markdown des nouveautés : **gras**, puces « • », paragraphes."""
    paras = [p.strip() for p in re.split(r'\n\s*\n', text.strip()) if p.strip()]
    out = []
    for p in paras:
        lines = [l.strip() for l in p.split('\n') if l.strip()]
        if all(l.startswith('•') for l in lines):
            out.append('<ul>' + ''.join('<li>' + inline(l[1:].strip()) + '</li>' for l in lines) + '</ul>')
        else:
            out.append('<p>' + '<br>'.join(inline(l) for l in lines) + '</p>')
    return '\n'.join(out)

def inline(s):
    s = esc(s)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)

def excerpt(text, n=150):
    t = re.sub(r'\*\*', '', text.split('\n')[0]).replace('•', '').strip()
    t = re.sub(r'\s+', ' ', t)
    if len(t) <= n: return t
    cut = t[:n].rsplit(' ', 1)[0].rstrip(',;:')
    return cut + '…'

def load():
    d = json.load(open(os.path.join(ROOT, 'tools', 'nouveautes.json'), encoding='utf-8'))
    HIDE = {'NV-2026-10-28-mentions-legales'}  # entrées administratives, sans intérêt pour les joueurs (demande d'Antoine)
    entries = sorted((e for e in d['entries'] if e['id'] not in HIDE), key=lambda e: (e['date'], e['id']), reverse=True)
    for e in entries:
        img = e.get('image')
        e['img'] = None
        if img:
            name = os.path.splitext(os.path.basename(img))[0]
            if os.path.exists(os.path.join(ROOT, 'img', 'news', name + '.webp')):
                e['img'] = f'/img/news/{name}.webp'; e['imgs'] = f'/img/news/{name}-s.webp'
    return entries

def texts(e, lang):
    if lang == 'fr': return e['titre'], e['description'], True
    if lang == 'en' and e['id'] in EN: return EN[e['id']][0], EN[e['id']][1], True
    return e['titre'], e['description'], False

def page(entries, lang):
    u = UI[lang]
    url = f"{BASE}/nouveautes/" if lang == 'fr' else f"{BASE}/en/nouveautes/"
    alt = f"{BASE}/en/nouveautes/" if lang == 'fr' else f"{BASE}/nouveautes/"
    home = f"{BASE}/" if lang == 'fr' else f"{BASE}/en/"
    items = []
    for e in entries:
        t, d, ok = texts(e, lang)
        fig = f'<figure><img src="{e["img"]}" alt="{esc(t)}" loading="lazy" width="1200" height="675"></figure>' if e['img'] else ''
        flag = '' if ok else f' <small>{esc(u["fr_only"])}</small>'
        items.append(f"""<article class="news" id="{esc(e['id'])}"{'' if ok else ' lang="fr"'}>
  <p class="nmeta"><span class="ncat c-{esc(e['categorie'])}">{esc(CAT[e['categorie']][lang])}</span> <time datetime="{e['date']}">{esc(date_txt(e['date'], lang))}</time></p>
  <h2>{esc(t)}{flag}</h2>
  {fig}
  {md(d)}
</article>""")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": u['title'], "description": u['desc'], "inLanguage": lang,
         "isPartOf": {"@id": f"{BASE}/#site"}, "about": {"@id": f"{BASE}/#game"},
         "hasPart": [{"@type": "Article", "headline": texts(e, lang)[0], "datePublished": e['date'], "url": url + '#' + e['id'],
                      **({"image": BASE + e['img']} if e['img'] else {})} for e in entries]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Door Knight", "item": home},
            {"@type": "ListItem", "position": 2, "name": u['crumb'], "item": url}]}]}
    head = f"""<p class="eyebrow">{esc(u['eyebrow'])}</p><h1>{esc(u['h1'])}</h1><p class="lede">{esc(u['lede'])}</p>"""
    main = '\n'.join(items) + f'<article>{bg.cta(lang)}</article>'
    extra = """<style>
.news{padding:34px 0 10px;border-top:1px solid var(--line)}
.news:first-of-type{border-top:0;padding-top:10px}
.news h2{margin:8px 0 14px;font-size:1.45rem}
.news h2::after{display:none}
.news h2 small{display:block;font:500 .78rem/1 "Inter",sans-serif;color:var(--ink-dim);margin-top:6px}
.nmeta{display:flex;align-items:center;gap:12px;font-size:.82rem;color:var(--ink-dim);margin:0}
.ncat{display:inline-block;padding:4px 10px;border-radius:999px;font-weight:600;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;background:rgba(155,134,255,.18);color:#c7b8ff}
.ncat.c-evenement{background:rgba(240,196,90,.2);color:var(--gold)}.ncat.c-correctif{background:rgba(95,224,208,.16);color:var(--mint)}.ncat.c-gameplay{background:rgba(255,120,90,.18);color:#ffb39f}.ncat.c-classes{background:rgba(255,105,180,.16);color:#ffb3d9}
.news figure{margin:0 0 16px}
.news strong{color:var(--ink)}
</style>"""
    out = bg.layout(lang, u['title'], u['desc'], url, alt, {'head': head, 'main': main}, ld, (BASE + entries[0]['img']) if entries and entries[0].get('img') else f"{BASE}/img/og.jpg",
                    [("Door Knight", home), (u['crumb'], None)])
    out = out.replace('</head>', extra + '\n</head>')
    return out

def home_block(entries):
    """Bloc FR de l'accueil + traductions à verser dans i18nData."""
    cards, tr = [], {}
    # sur l'accueil : d'abord les entrées illustrées (plus parlantes), puis les autres, toujours de la plus récente à la plus ancienne
    picked = [e for e in entries if e.get('imgs')][:HOME_N]
    picked += [e for e in entries if e not in picked][:HOME_N - len(picked)]
    picked.sort(key=lambda e: (e['date'], e['id']), reverse=True)
    for e in picked:
        t_fr, d_fr = e['titre'], excerpt(e['description'])
        en_t, en_d = (EN[e['id']][0], excerpt(EN[e['id']][1])) if e['id'] in EN else (t_fr, d_fr)
        es_t, es_d = ES.get(e['id'], (en_t, en_d)); de_t, de_d = DE.get(e['id'], (en_t, en_d))
        tr[t_fr] = [en_t, es_t, de_t]; tr[d_fr] = [en_d, es_d, de_d]
        cat_fr = CAT[e['categorie']]['fr']; tr[cat_fr] = [CAT[e['categorie']][l] for l in ('en', 'es', 'de')]
        dt = date_txt(e['date'], 'fr'); tr[dt] = [date_txt(e['date'], l) for l in ('en', 'es', 'de')]
        img = f'<img src="{e["imgs"]}" alt="" loading="lazy" width="640" height="360">' if e.get('imgs') else '<span class="nimg-ph" aria-hidden="true"><img src="/img/icon.webp" alt="" loading="lazy" width="96" height="96"></span>'
        cards.append(f"""      <a class="ncard rv" href="/nouveautes/#{esc(e['id'])}">
        <span class="nimg">{img}</span>
        <span class="nbody"><span class="nmeta"><span class="ncat c-{esc(e['categorie'])}">{esc(cat_fr)}</span><time datetime="{e['date']}">{esc(dt)}</time></span><b>{esc(t_fr)}</b><span class="ntxt">{esc(d_fr)}</span></span>
      </a>""")
    return '\n'.join(cards), tr

def update_home(entries):
    p = os.path.join(ROOT, 'index.html'); s = open(p, encoding='utf-8').read()
    block, tr = home_block(entries)
    s2 = re.sub(r'(<!-- nouveautes:start -->).*?(<!-- nouveautes:end -->)', lambda m: m.group(1) + '\n' + block + '\n' + m.group(2), s, flags=re.S)
    assert s2 != s or block in s, 'marqueurs nouveautes:start/end introuvables dans index.html'
    # dictionnaire i18n
    m = re.search(r'(<script id="i18nData" type="application/json">)(.*?)(</script>)', s2, flags=re.S)
    D = json.loads(m.group(2))
    key = lambda x: x.replace('’', "'")
    changed = 0
    for k, v in tr.items():
        if D.get(key(k)) != v: D[key(k)] = v; changed += 1
    s2 = s2[:m.start(2)] + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + s2[m.end(2):]
    open(p, 'w', encoding='utf-8').write(s2)
    return changed

def update_sitemap():
    p = os.path.join(ROOT, 'sitemap.xml'); s = open(p, encoding='utf-8').read()
    s = re.sub(r'\s*<!-- nouveautes -->.*?<!-- /nouveautes -->', '', s, flags=re.S)
    blocks = []
    for path, alt, lang in (('/nouveautes/', '/en/nouveautes/', 'fr'), ('/en/nouveautes/', '/nouveautes/', 'en')):
        other = 'en' if lang == 'fr' else 'fr'
        blocks.append(f"""  <url>
    <loc>{BASE}{path}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="{lang}" href="{BASE}{path}"/>
    <xhtml:link rel="alternate" hreflang="{other}" href="{BASE}{alt}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/nouveautes/"/>
  </url>""")
    s = s.replace('</urlset>', '  <!-- nouveautes -->\n' + '\n'.join(blocks) + '\n  <!-- /nouveautes -->\n</urlset>')
    open(p, 'w', encoding='utf-8').write(s)

if __name__ == '__main__':
    entries = load()
    for lang, rel in (('fr', 'nouveautes'), ('en', 'en/nouveautes')):
        path = os.path.join(ROOT, rel, 'index.html'); os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(page(entries, lang)); print(rel, len(entries), 'entrées')
    print('accueil :', update_home(entries), 'traductions ajoutées')
    update_sitemap()
