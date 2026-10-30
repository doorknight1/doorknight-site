#!/usr/bin/env python3
"""Durcissement du site : politique de sécurité du contenu (CSP) et en-têtes équivalents
en <meta>, sur toutes les pages HTML. GitHub Pages n'autorise pas les en-têtes HTTP
personnalisés : la CSP en <meta> est la seule option, et frame-ancestors n'y est pas pris en
compte, d'où le petit anti-cadre dans js/site.js et js/legal.js.

Idempotent : à relancer après avoir généré des pages (build-langues.py, build-guides.py) :
    python3 tools/securite.py
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSP = ("default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self'; "
       "media-src 'self'; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; "
       "form-action 'none'; frame-src 'none'; manifest-src 'self'; upgrade-insecure-requests")
META = ('<meta http-equiv="Content-Security-Policy" content="%s">\n'
        '<meta name="referrer" content="strict-origin-when-cross-origin">\n'
        '<meta http-equiv="X-Content-Type-Options" content="nosniff">\n') % CSP
MARK_RE = re.compile(r'<meta http-equiv="Content-Security-Policy"[^>]*>\n(<meta name="referrer"[^>]*>\n)?(<meta http-equiv="X-Content-Type-Options"[^>]*>\n)?')
LEGAL_INLINE = re.compile(r'<script>document\.querySelectorAll\(\'\.langs a\'\).*?</script>\n?', re.S)

def harden(path):
    s = open(path, encoding='utf-8').read()
    s = MARK_RE.sub('', s)
    # juste après <meta charset>, avant tout chargement de ressource
    s = re.sub(r'(<meta charset="utf-8">\n)', r'\1' + META.replace('\\', '\\\\'), s, count=1)
    # pages légales : le script inline passe en fichier externe (interdit par la CSP sinon)
    if LEGAL_INLINE.search(s):
        s = LEGAL_INLINE.sub('<script src="/js/legal.js" defer></script>\n', s)
    # pages sans script : l'anti-cadre
    if '/js/site.js' not in s and '/js/legal.js' not in s:
        s = s.replace('</body>', '<script src="/js/legal.js" defer></script>\n</body>', 1)
    open(path, 'w', encoding='utf-8').write(s)

def main():
    files = [p for p in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
             if 'google' not in os.path.basename(p) and '/tools/' not in p]
    for p in files:
        harden(p)
    print(len(files), 'pages durcies')

if __name__ == '__main__':
    main()
