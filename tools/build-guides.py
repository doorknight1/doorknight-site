#!/usr/bin/env python3
"""Génère la rubrique Guides : /guide/ (français) et /en/guide/ (anglais).

Chaque article existe dans les deux langues, avec canonical, hreflang, Open Graph,
données structurées Article + BreadcrumbList, et le même habillage que le site.
À relancer après toute modification :  python3 tools/build-guides.py
Les textes sont dans tools/guides-content.py.
"""
import os, json, re, datetime, html
from guides_content import ARTICLES, UI

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://doorknight.games'
TODAY = datetime.date.today().isoformat()

CSS = """
@font-face{font-family:"Cinzel";font-weight:700;font-display:swap;src:url(/fonts/cinzel-latin-700-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-weight:400;font-display:swap;src:url(/fonts/inter-latin-400-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-weight:600;font-display:swap;src:url(/fonts/inter-latin-600-normal.woff2) format("woff2")}
:root{color-scheme:dark;--night:#0d0b1c;--night-2:#161330;--line:rgba(190,170,255,.14);--ink:#f3eefc;--ink-dim:#a9a2c8;--gold:#f0c45a;--mint:#5fe0d0}
*{box-sizing:border-box}
body{margin:0;background:var(--night);color:var(--ink);font:17px/1.7 "Inter",system-ui,-apple-system,"Segoe UI",sans-serif;overflow-x:hidden}
a{color:var(--gold)}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
nav{position:sticky;top:0;z-index:9;background:rgba(13,11,28,.85);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
nav .wrap{max-width:1120px;display:flex;align-items:center;justify-content:space-between;gap:16px;padding-block:12px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);font-family:"Cinzel",serif;font-weight:700;letter-spacing:.06em;font-size:.95rem}
.brand img{width:34px;height:34px}
nav .r{display:flex;align-items:center;gap:10px}
nav .r a{text-decoration:none;color:var(--ink-dim);font-size:.92rem;font-weight:600}
nav .r a.lang{border:1px solid var(--line);border-radius:10px;padding:6px 10px;color:var(--ink);font-size:.8rem}
nav .r a.cta{background:var(--gold);color:#2a1a08;border-radius:10px;padding:8px 14px;font-family:"Cinzel",serif;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase}
.hero{padding:56px 0 28px;background:radial-gradient(ellipse 90% 70% at 50% 0%,#33276e 0%,#1c1745 45%,var(--night) 85%)}
.crumbs{font-size:.85rem;color:var(--ink-dim);margin-bottom:14px}
.crumbs a{color:var(--ink-dim);text-decoration:none}
.crumbs a:hover{color:var(--ink)}
.eyebrow{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:var(--mint);font-weight:600;margin:0 0 10px}
h1{font-family:"Cinzel",serif;font-size:clamp(1.7rem,4.5vw,2.6rem);line-height:1.15;margin:0 0 14px}
.lede{font-size:1.15rem;color:var(--ink-dim);margin:0}
.meta{font-size:.85rem;color:var(--ink-dim);margin-top:18px}
article{padding:28px 0 60px}
article h2{font-family:"Cinzel",serif;font-size:1.35rem;margin:38px 0 12px;padding-top:6px}
article h2::after{content:"";display:block;height:3px;width:70px;margin-top:10px;border-radius:2px;background:linear-gradient(90deg,var(--gold),transparent)}
article h3{font-size:1.05rem;margin:24px 0 8px}
article p{margin:0 0 14px}
article ul,article ol{padding-left:22px;margin:0 0 14px}
article li{margin-bottom:6px}
article figure{margin:22px 0}
article figure img{width:100%;height:auto;max-height:420px;object-fit:cover;object-position:top;border-radius:16px;border:1px solid var(--line)}
.tbl{overflow-x:auto;margin:0 0 18px}
.tbl table{margin:0;min-width:520px}
article figcaption{font-size:.85rem;color:var(--ink-dim);margin-top:8px;text-align:center}
.tip{border:1px solid rgba(240,196,90,.4);background:rgba(240,196,90,.07);border-radius:14px;padding:14px 18px;margin:18px 0}
.tip b{color:var(--gold)}
table{width:100%;border-collapse:collapse;font-size:.95rem;margin:0 0 18px}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--gold);font-family:"Cinzel",serif;font-size:.85rem;letter-spacing:.04em}
.cta-box{text-align:center;border:1px solid var(--line);background:var(--night-2);border-radius:20px;padding:28px 22px;margin:40px 0 0}
.cta-box h2{margin:0 0 8px;font-size:1.3rem}.cta-box h2::after{display:none}
.cta-box p{color:var(--ink-dim);margin:0 0 16px}
.btn{display:inline-flex;align-items:center;gap:10px;font-family:"Cinzel",serif;font-weight:700;font-size:.9rem;letter-spacing:.06em;text-transform:uppercase;text-decoration:none;padding:14px 22px;border-radius:14px;color:#2a1a08;background:linear-gradient(180deg,#ffe9a8,#f0c45a 55%,#d19a33);box-shadow:0 8px 24px rgba(240,196,90,.25);margin:4px}
.btn.ghost{background:rgba(22,19,48,.7);color:var(--ink);border:1px solid var(--line);box-shadow:none}
.cards{display:grid;gap:14px;margin:30px 0 0}
.card{display:block;text-decoration:none;color:var(--ink);border:1px solid var(--line);background:var(--night-2);border-radius:18px;padding:20px 22px;transition:border-color .2s,transform .15s}
.card:hover{border-color:var(--gold);transform:translateY(-2px)}
.card b{font-family:"Cinzel",serif;font-size:1.05rem;display:block;margin-bottom:6px}
.card span{color:var(--ink-dim);font-size:.95rem}
.more{margin-top:40px}
.more h2{font-size:1.2rem}
footer{border-top:1px solid var(--line);padding:28px 0 40px;color:var(--ink-dim);font-size:.9rem}
footer .wrap{max-width:1120px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px}
footer a{color:var(--ink-dim)}
@media(max-width:600px){nav .r a.hide{display:none}.brand span{display:none}}
"""

def esc(x): return html.escape(x, quote=True)

def layout(lang, title, desc, url, alt_url, body, ld, og_image, crumbs):
    u = UI[lang]
    other = 'en' if lang == 'fr' else 'fr'
    home = '/' if lang == 'fr' else '/en/'
    legal = ('mentions-legales.html', 'politique-confidentialite.html') if lang == 'fr' else ('mentions-legales-en.html', 'politique-confidentialite-en.html')
    crumbs_html = ' › '.join(f'<a href="{esc(h)}">{esc(t)}</a>' if h else esc(t) for t, h in crumbs)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#0d0b1c">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="{lang}" href="{url}">
<link rel="alternate" hreflang="{other}" href="{alt_url}">
<link rel="alternate" hreflang="x-default" href="{url if lang == 'fr' else alt_url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Door Knight">
<meta property="og:locale" content="{'fr_FR' if lang == 'fr' else 'en_US'}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og_image}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<nav><div class="wrap">
  <a class="brand" href="{home}"><img src="/img/icon.webp" alt=""><span>Door Knight</span></a>
  <div class="r">
    <a class="hide" href="{home}#heros">{esc(u['heroes'])}</a>
    <a class="hide" href="{'/guide/' if lang == 'fr' else '/en/guide/'}">{esc(u['guides'])}</a>
    <a class="hide" href="https://discord.gg/GNWHbMUqP3" target="_blank" rel="noopener">Discord</a>
    <a class="lang" href="{alt_url}" hreflang="{other}" lang="{other}">{other.upper()}</a>
    <a class="cta" href="{home}#telecharger">{esc(u['beta'])}</a>
  </div>
</div></nav>
<header class="hero"><div class="wrap">
  <p class="crumbs">{crumbs_html}</p>
  {body['head']}
</div></header>
<main><div class="wrap">
{body['main']}
</div></main>
<footer><div class="wrap">
  <div>© {TODAY[:4]} FDA · Door Knight</div>
  <div><a href="{home}">{esc(u['home'])}</a> · <a href="https://discord.gg/GNWHbMUqP3" target="_blank" rel="noopener">Discord</a> · <a href="https://www.instagram.com/doorknight.games/" target="_blank" rel="noopener">Instagram</a> · <a href="/{legal[0]}">{esc(u['legal'])}</a> · <a href="/{legal[1]}">{esc(u['privacy'])}</a></div>
</div></footer>
</body>
</html>
"""

def cta(lang):
    u = UI[lang]
    home = '/' if lang == 'fr' else '/en/'
    return f"""<div class="cta-box">
  <h2>{esc(u['cta_title'])}</h2>
  <p>{esc(u['cta_text'])}</p>
  <a class="btn" href="https://testflight.apple.com/join/Jhxx6gj1" target="_blank" rel="noopener">{esc(u['cta_btn'])}</a>
  <a class="btn ghost" href="https://discord.gg/GNWHbMUqP3" target="_blank" rel="noopener">{esc(u['cta_discord'])}</a>
</div>"""

def more(lang, current):
    u = UI[lang]
    items = ''.join(f'<a class="card" href="{a["url"][lang]}"><b>{esc(a[lang]["title"])}</b><span>{esc(a[lang]["desc"])}</span></a>'
                    for a in ARTICLES if a is not current)
    return f'<section class="more"><h2>{esc(u["more"])}</h2><div class="cards">{items}</div></section>'

def build():
    org = {"@type": "Organization", "@id": f"{BASE}/#org", "name": "FDA", "url": f"{BASE}/", "logo": f"{BASE}/img/icon.webp"}
    out = []
    for a in ARTICLES:
        for lang in ('fr', 'en'):
            c = a[lang]; url = BASE + a['url'][lang]; alt = BASE + a['url']['en' if lang == 'fr' else 'fr']
            guide_url = f"{BASE}/guide/" if lang == 'fr' else f"{BASE}/en/guide/"
            home = f"{BASE}/" if lang == 'fr' else f"{BASE}/en/"
            ld = {"@context": "https://schema.org", "@graph": [
                {"@type": "Article", "@id": url + "#article", "headline": c['title'], "description": c['desc'],
                 "inLanguage": lang, "image": BASE + a['image'], "datePublished": a['date'], "dateModified": TODAY,
                 "author": org, "publisher": org, "mainEntityOfPage": url,
                 "about": {"@id": f"{BASE}/#game"}, "isPartOf": {"@id": f"{BASE}/#site"}},
                {"@type": "BreadcrumbList", "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Door Knight", "item": home},
                    {"@type": "ListItem", "position": 2, "name": UI[lang]['guides'], "item": guide_url},
                    {"@type": "ListItem", "position": 3, "name": c['title'], "item": url}]}]}
            if c.get('faq'):
                ld['@graph'].append({"@type": "FAQPage", "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in c['faq']]})
            head = f"""<p class="eyebrow">{esc(c['eyebrow'])}</p>
  <h1>{esc(c['h1'])}</h1>
  <p class="lede">{esc(c['lede'])}</p>
  <p class="meta">{esc(UI[lang]['updated'])} {a['date']} · {esc(UI[lang]['by'])} FDA</p>"""
            img = a['image'].replace('/img/shot-', '/img/en/shot-') if lang == 'en' and '/img/shot-' in a['image'] else a['image']
            body_html = c['body'].replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
            main = f"""<article>
<figure><img src="{img}" alt="{esc(c['image_alt'])}"></figure>
{body_html}
{cta(lang)}
</article>
{more(lang, a)}"""
            page = layout(lang, c['title'], c['desc'], url, alt, {'head': head, 'main': main}, ld, BASE + a['image'],
                          [("Door Knight", home), (UI[lang]['guides'], guide_url), (c['h1'], None)])
            path = os.path.join(ROOT, a['url'][lang].lstrip('/'))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, 'w', encoding='utf-8').write(page)
            out.append((a['url'][lang], a['url']['en' if lang == 'fr' else 'fr'], a['date']))
    # index des guides
    for lang in ('fr', 'en'):
        u = UI[lang]; url = f"{BASE}/guide/" if lang == 'fr' else f"{BASE}/en/guide/"
        alt = f"{BASE}/en/guide/" if lang == 'fr' else f"{BASE}/guide/"
        home = f"{BASE}/" if lang == 'fr' else f"{BASE}/en/"
        cards = ''.join(f'<a class="card" href="{a["url"][lang]}"><b>{esc(a[lang]["title"])}</b><span>{esc(a[lang]["desc"])}</span></a>' for a in ARTICLES)
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": u['index_title'], "description": u['index_desc'],
             "inLanguage": lang, "isPartOf": {"@id": f"{BASE}/#site"}, "about": {"@id": f"{BASE}/#game"},
             "hasPart": [{"@type": "Article", "@id": BASE + a['url'][lang] + "#article", "headline": a[lang]['title'], "url": BASE + a['url'][lang]} for a in ARTICLES]},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Door Knight", "item": home},
                {"@type": "ListItem", "position": 2, "name": u['guides'], "item": url}]}]}
        head = f"""<p class="eyebrow">{esc(u['guides'])}</p><h1>{esc(u['index_h1'])}</h1><p class="lede">{esc(u['index_lede'])}</p>"""
        main = f'<div class="cards" style="margin-top:0">{cards}</div><article>{cta(lang)}</article>'
        page = layout(lang, u['index_title'], u['index_desc'], url, alt, {'head': head, 'main': main}, ld, f"{BASE}/img/og.jpg",
                      [("Door Knight", home), (u['guides'], None)])
        path = os.path.join(ROOT, 'guide' if lang == 'fr' else 'en/guide', 'index.html')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(page)
        out.append(('/guide/' if lang == 'fr' else '/en/guide/', '/en/guide/' if lang == 'fr' else '/guide/', TODAY))
    return out

def update_sitemap(pages):
    p = os.path.join(ROOT, 'sitemap.xml'); s = open(p, encoding='utf-8').read()
    s = re.sub(r'\s*<!-- guides -->.*?<!-- /guides -->', '', s, flags=re.S)
    blocks = []
    for path, alt, date in pages:
        lang = 'en' if path.startswith('/en/') else 'fr'; other = 'fr' if lang == 'en' else 'en'
        xd = path if lang == 'fr' else alt
        blocks.append(f"""  <url>
    <loc>{BASE}{path}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
    <xhtml:link rel="alternate" hreflang="{lang}" href="{BASE}{path}"/>
    <xhtml:link rel="alternate" hreflang="{other}" href="{BASE}{alt}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{xd}"/>
  </url>""")
    s = s.replace('</urlset>', '  <!-- guides -->\n' + '\n'.join(blocks) + '\n  <!-- /guides -->\n</urlset>')
    open(p, 'w', encoding='utf-8').write(s)

if __name__ == '__main__':
    pages = build()
    update_sitemap(pages)
    for p in pages: print(p[0])
