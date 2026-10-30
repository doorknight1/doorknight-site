# Fabrication des Shorts (TikTok / YouTube Shorts / Reels) — Door Knight

Outils utilisés le 30/10/2026 pour la série quotidienne. Tout tourne dans une session Claude (Linux, ffmpeg, Python + Pillow + Playwright).

1. Servir une copie du jeu : copier `index.html` + `public/` du dépôt du jeu dans un dossier et lancer `python3 -m http.server 8765`.
2. Capturer du gameplay en portrait : `LVL=60 UP=18 MA=14 python3 rec.py port-b80 270 480 4 80 samurai 9 0.3`
   (dossier de sortie, largeur, hauteur, DPR → 1080×1920, porte, classe, secondes, préchauffe en s ; 0.3 pour une porte de gardien = la bannière du boss apparaît vers 2 s, 3 pour un combat de monstres déjà lancé). Variables : LVL niveau du héros, UP améliorations, MA monstres simultanés. Sortie : images f00000.jpg… à 30 i/s.
3. Monter : `python3 make.py all` (ou un nom). `make.py` contient les recettes : `boss_short` (accroche 1,9 s, bannière + voix du gardien `public/audio/voice/en/gardien_NN.mp3` lancée à 2,0 s, musique du jeu baissée sous la voix, carte de fin), `montage_short` (plusieurs captures), `image_short` (images du site avec zoom lent). Polices Cinzel 900 / Inter 600 (dossier fonts/ du site). Carte de fin : `P-en-end.png` générée par `ov.py` de la bande-annonce (icône + « Free open beta » + doorknight.games).
4. Publier via Zernio : `media_get_media_presigned_url` → PUT du mp4 → `posts_create_post` (un post par réseau, légende adaptée).

Zones sûres : accroche à 230 px du haut, appel à l'action vers 1540 px, rien d'important sous 1600 px ni sur la bande droite.
