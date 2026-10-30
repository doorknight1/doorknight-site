#!/bin/sh
# Reconstruit tout le site après une modification : version des fichiers css/js, nouveautés, langues, guides.
set -e
cd "$(dirname "$0")/.."
python3 - <<'PY'
import hashlib,re
v=hashlib.md5(open('css/site.css','rb').read()+open('js/site.js','rb').read()).hexdigest()[:8]
h=open('index.html').read()
h=re.sub(r'/css/site\.css\?v=\w+','/css/site.css?v='+v,h); h=re.sub(r'/js/site\.js\?v=\w+','/js/site.js?v='+v,h)
open('index.html','w').write(h); print('version',v)
PY
python3 tools/build-nouveautes.py
python3 tools/build-guides.py >/dev/null
python3 tools/build-langues.py
