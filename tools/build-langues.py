#!/usr/bin/env python3
"""Génère en/index.html, es/index.html et de/index.html à partir de index.html (français).

Pourquoi : pour le référencement, chaque langue a sa propre adresse (/, /en/, /es/, /de/)
avec le texte déjà traduit dans le HTML (Google n'a pas besoin d'exécuter la traduction JavaScript).
Le dictionnaire de traduction est celui du site (bloc i18nData), appliqué avec la même logique
que le JavaScript du site : textes, alt/title/aria-label, description, images localisées, liens légaux.

À relancer après chaque modification de index.html :  python3 tools/build-langues.py
"""
import json, os, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://doorknight.games/'
LANGS = ['en', 'es', 'de']
META = {
    'en': {
        'title': 'Door Knight · Action-adventure mobile game for iPhone and iPad (open beta)',
        'og_title': 'Door Knight · Action-adventure mobile game, open beta',
        'og_desc': 'Behind every door, a horde of monsters. 4 heroes, 10 worlds, 10 guardians. Join the free beta on iPhone and iPad.',
        'og_alt': 'Door Knight: the knight in front of a door, ready to fight the monsters',
        'locale': 'en_US',
        'ld_desc': "Door Knight is an action-adventure mobile game: pick the knight, the archer, the mage or the samurai and open endless doors. Every 5 doors a mini-boss, every 10 a guardian. 10 worlds, 96 spells, a camp to build and an arena. Free open beta on iPhone and iPad via TestFlight.",
        'ld_sub': 'Action-adventure', 'ld_genre': ['Action', 'Adventure', 'Roguelite'], 'ld_beta': 'Open beta',
        'chars': ['The Knight', 'The Archer', 'The Mage', 'The Samurai'],
    },
    'es': {
        'title': 'Door Knight · Juego móvil de acción y aventura para iPhone y iPad (beta abierta)',
        'og_title': 'Door Knight · Juego móvil de acción y aventura, beta abierta',
        'og_desc': 'Tras cada puerta, una horda de monstruos. 4 héroes, 10 mundos, 10 guardianes. Únete a la beta gratuita en iPhone y iPad.',
        'og_alt': 'Door Knight: el caballero frente a una puerta, listo para enfrentarse a los monstruos',
        'locale': 'es_ES',
        'ld_desc': "Door Knight es un juego móvil de acción y aventura: elige al caballero, al arquero, al mago o al samurái y abre puertas sin fin. Cada 5 puertas un minijefe, cada 10 un guardián. 10 mundos, 96 hechizos, un campamento que construir y una arena. Beta abierta gratuita en iPhone y iPad vía TestFlight.",
        'ld_sub': 'Acción y aventura', 'ld_genre': ['Acción', 'Aventura', 'Roguelite'], 'ld_beta': 'Beta abierta',
        'chars': ['El Caballero', 'El Arquero', 'El Mago', 'El Samurái'],
    },
    'de': {
        'title': 'Door Knight · Action-Adventure-Handyspiel für iPhone und iPad (offene Beta)',
        'og_title': 'Door Knight · Action-Adventure-Handyspiel, offene Beta',
        'og_desc': 'Hinter jeder Tür eine Horde Monster. 4 Helden, 10 Welten, 10 Wächter. Mach bei der kostenlosen Beta auf iPhone und iPad mit.',
        'og_alt': 'Door Knight: der Ritter vor einer Tür, bereit für den Kampf gegen die Monster',
        'locale': 'de_DE',
        'ld_desc': "Door Knight ist ein Action-Adventure-Handyspiel: Wähle Ritter, Bogenschütze, Magier oder Samurai und öffne endlose Türen. Alle 5 Türen ein Mini-Boss, alle 10 ein Wächter. 10 Welten, 96 Zauber, ein Lager zum Aufbauen und eine Arena. Kostenlose offene Beta auf iPhone und iPad über TestFlight.",
        'ld_sub': 'Action-Adventure', 'ld_genre': ['Action', 'Adventure', 'Roguelite'], 'ld_beta': 'Offene Beta',
        'chars': ['Der Ritter', 'Der Bogenschütze', 'Der Magier', 'Der Samurai'],
    },
}

# même logique que I18.collect/apply dans index.html, exécutée sur le DOM statique (JavaScript désactivé)
JS = r"""
([l, meta]) => {
  const D = JSON.parse(document.getElementById('i18nData').textContent), IX = {en:0, es:1, de:2};
  const key = x => x.replace(/’/g, "'").replace(/\s+/g, ' ').trim();
  const T = fr => { const v = D[key(fr)]; return v ? v[IX[l]] : fr; };
  const LOC = /(^|\/)(shot-[\w-]+|cls-[\w-]+|camp-(meadow|autumn|snow|arcane)|raid)\.webp$/;
  const img = p => (!LOC.test(p) || /^\/img\/(camp\/)?(en|es|de)\//.test(p)) ? p : p.replace(/^\/img\/(camp\/)?/, (m, c) => '/img/' + (c || '') + l + '/');
  let nTexts = 0, nAttrs = 0;
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const nodes = []; for (let n; (n = w.nextNode());) {
    const p = n.parentNode && n.parentNode.nodeName;
    if (p === 'SCRIPT' || p === 'STYLE') continue;
    if (D[key(n.nodeValue)]) nodes.push(n); }
  nodes.forEach(n => { const m = n.nodeValue.match(/^(\s*)([\s\S]*?)(\s*)$/); n.nodeValue = m[1] + T(m[2]) + m[3]; nTexts++; });
  document.querySelectorAll('[alt],[title],[aria-label]').forEach(el => ['alt', 'title', 'aria-label'].forEach(a => {
    const v = el.getAttribute(a); if (v && D[key(v)]) { el.setAttribute(a, T(v)); nAttrs++; } }));
  const md = document.querySelector('meta[name="description"]'); md.setAttribute('content', T(md.getAttribute('content')));
  document.querySelectorAll('img[src]').forEach(im => { const s = im.getAttribute('src'), n2 = img(s); if (n2 !== s) im.setAttribute('src', n2); });
  document.querySelectorAll('a[href*="mentions-legales"],a[href*="politique-confidentialite"]').forEach(a => {
    a.setAttribute('href', a.getAttribute('href').replace(/(-(en|es|de))?\.html$/, '') + '-' + l + '.html'); });
  // en-tête propre à la langue
  const h = document.documentElement; h.setAttribute('lang', l); h.setAttribute('data-lang', l);
  document.title = meta.title;
  const url = 'https://doorknight.games/' + l + '/';
  const set = (sel, val) => { const e = document.querySelector(sel); if (e) e.setAttribute('content', val); };
  document.querySelector('link[rel="canonical"]').setAttribute('href', url);
  set('meta[property="og:url"]', url); set('meta[property="og:title"]', meta.og_title); set('meta[property="og:description"]', meta.og_desc);
  set('meta[property="og:image:alt"]', meta.og_alt); set('meta[name="twitter:title"]', meta.og_title);
  set('meta[name="twitter:description"]', meta.og_desc); set('meta[name="twitter:image:alt"]', meta.og_alt);
  const locs = ['fr_FR', 'en_US', 'es_ES', 'de_DE'];
  set('meta[property="og:locale"]', meta.locale);
  const alts = document.querySelectorAll('meta[property="og:locale:alternate"]');
  locs.filter(x => x !== meta.locale).forEach((x, i) => alts[i].setAttribute('content', x));
  document.getElementById('langCur').textContent = l.toUpperCase();
  document.querySelectorAll('#langMenu [data-l]').forEach(b => b.setAttribute('aria-checked', String(b.dataset.l === l)));
  // données structurées
  const ld = JSON.parse(document.getElementById('ldjson').textContent);
  ld['@graph'].forEach(o => {
    const t = [].concat(o['@type']);
    if (t.includes('WebSite')) o.inLanguage = l;
    if (t.includes('VideoGame')) { o.url = url; o.description = meta.ld_desc; o.applicationSubCategory = meta.ld_sub; o.genre = meta.ld_genre;
      o.offers.category = meta.ld_beta; o.character = meta.chars.map(n => ({'@type': 'Person', name: n}));
      o.gameLocation = o.gameLocation.map(p => ({'@type': 'Place', name: T(p.name)})); }
    if (t.includes('FAQPage')) { o['@id'] = url + '#faq'; o.mainEntity.forEach(q => { q.name = T(q.name); q.acceptedAnswer.text = T(q.acceptedAnswer.text); }); }
    if (t.includes('WebPage')) { o['@id'] = url + '#page'; o.url = url; o.name = meta.title; o.inLanguage = l; }
  });
  document.getElementById('ldjson').textContent = JSON.stringify(ld);
  return [nTexts, nAttrs];
}
"""

def main():
    src = os.path.join(ROOT, 'index.html')
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(java_script_enabled=False)
        for l in LANGS:
            pg = ctx.new_page()
            pg.goto('file://' + src, wait_until='domcontentloaded')
            n = pg.evaluate(JS, [l, META[l]])
            html = '<!doctype html>\n' + pg.evaluate('document.documentElement.outerHTML') + '\n'
            out = os.path.join(ROOT, l, 'index.html')
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, 'w', encoding='utf-8') as f:
                f.write(html)
            print(l, 'textes', n[0], 'attributs', n[1], '->', os.path.relpath(out, ROOT), len(html), 'octets')
            pg.close()
        b.close()

if __name__ == '__main__':
    main()
