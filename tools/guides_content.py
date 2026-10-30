# -*- coding: utf-8 -*-
# Textes de la rubrique Guides (français et anglais). Tout ce qui est dit ici vient du jeu
# tel que le site le présente : pas de chiffre inventé.

UI = {
    'fr': {'heroes': 'Héros', 'guides': 'Guides', 'beta': 'Bêta', 'home': 'Accueil', 'legal': 'Mentions légales',
           'privacy': 'Confidentialité', 'updated': 'Mis à jour le', 'by': 'par', 'more': 'Les autres guides',
           'cta_title': 'Prêt à ouvrir la première porte ?', 'cta_text': 'Door Knight est gratuit, en bêta ouverte sur iPhone et iPad via TestFlight. Android arrive sur Google Play.',
           'cta_btn': 'Rejoindre la bêta', 'cta_discord': 'Rejoindre le Discord',
           'index_title': 'Guides Door Knight : débuter, choisir son héros, battre les gardiens',
           'index_desc': "Les guides officiels de Door Knight : bien débuter, choisir entre chevalier, archer, mage et samouraï, comprendre les 10 gardiens et installer la bêta sur iPhone.",
           'index_h1': 'Les guides Door Knight', 'index_lede': "Tout ce qu'il faut savoir avant d'ouvrir la première porte, écrit par l'équipe du jeu."},
    'en': {'heroes': 'Heroes', 'guides': 'Guides', 'beta': 'Beta', 'home': 'Home', 'legal': 'Legal notice',
           'privacy': 'Privacy', 'updated': 'Updated', 'by': 'by', 'more': 'More guides',
           'cta_title': 'Ready to open the first door?', 'cta_text': 'Door Knight is free, in open beta on iPhone and iPad via TestFlight. Android is coming to Google Play.',
           'cta_btn': 'Join the beta', 'cta_discord': 'Join the Discord',
           'index_title': 'Door Knight guides: getting started, picking a hero, beating the guardians',
           'index_desc': "The official Door Knight guides: how to start well, how to choose between knight, archer, mage and samurai, the 10 guardians explained, and how to install the beta on iPhone.",
           'index_h1': 'The Door Knight guides', 'index_lede': 'Everything worth knowing before you open the first door, written by the team behind the game.'},
}

ARTICLES = [
# ─────────────────────────────────────────────────────────────── 1. Bien commencer
{
 'url': {'fr': '/guide/bien-commencer.html', 'en': '/en/guide/getting-started.html'},
 'image': '/img/og.jpg', 'date': '2026-10-30',
 'fr': {
  'eyebrow': 'Guide du débutant',
  'title': "Door Knight : le guide du débutant pour bien commencer",
  'h1': "Bien commencer Door Knight : les 10 premières portes",
  'desc': "Comment débuter Door Knight : les contrôles à un pouce, le choix du premier héros, les sorts dès le niveau 10, le butin, le campement et le premier gardien à la porte 10.",
  'lede': "Tu viens d'installer la bêta ? Voici ce qui compte vraiment pendant les dix premières portes, avant de croiser le Roi Gluant.",
  'image_alt': "Le chevalier de Door Knight devant une porte, prêt à affronter les monstres",
  'body': """
<h2>Le principe en une phrase</h2>
<p>Door Knight est un jeu d'action-aventure où tu ouvres des portes, à l'infini. Derrière chacune, une horde de monstres. Toutes les 5 portes, un mini-boss ; toutes les 10, un gardien qui protège la sortie du monde. Dix portes par monde, dix mondes, puis le Cercle II recommence tout, plus redoutable.</p>

<h2>Les contrôles : un pouce pour bouger, un pour frapper</h2>
<p>Pose le pouce n'importe où sur l'écran et glisse : ton héros suit. Maintiens le bouton d'attaque pour enchaîner les coups : le héros vise de lui-même l'ennemi le plus proche. Tu n'as donc pas à viser, seulement à te placer. C'est la compétence numéro un du jeu : rester hors des zones annoncées au sol.</p>
<div class="tip"><b>À retenir :</b> chaque monstre annonce son sort au sol avant de le lancer, par un cercle, une ligne ou un cône. Si tu es encore dedans quand il part, tu prends du poison, une brûlure, une lenteur ou une entrave. Sors de la zone, puis seulement frappe.</div>

<h2>Quel héros pour commencer ?</h2>
<p>Quatre classes sont disponibles dès la création : Chevalier, Archer, Mage et Samouraï. Pour une première partie, le <strong>Chevalier</strong> est le plus tolérant : c'est le plus robuste, il frappe en arc de cercle et renvoie les projectiles. L'<strong>Archer</strong> est un bon second choix si tu préfères garder tes distances. Rien n'est définitif : tu peux jouer jusqu'à quatre héros, chacun avec son niveau, son or et son armurerie. On compare les quatre en détail dans <a href="/guide/quel-heros-choisir.html">Quel héros choisir ?</a></p>

<h2>Niveau 10 : le Grimoire s'ouvre</h2>
<p>Dès le niveau 10, ton héros débloque ses sorts. Chaque classe a trois écoles et 24 sorts au total (96 dans le jeu). Choisis une école, ouvre le Grimoire, et regarde l'animation du sort avant de l'équiper : Boule de feu, Blizzard, Phénix, Jugement céleste… chacun a la sienne. Un sort de zone change tout face aux hordes ; un sort de contrôle (lenteur, entrave) sauve des vies face aux mini-boss.</p>

<h2>Le butin se voit sur toi</h2>
<p>Casque, armure, bottes et talisman trouvés derrière les portes s'affichent directement sur ton héros. La rareté se lit à l'œil : gemme dès le rare, lueur dès l'épique, liseré d'or au légendaire, étincelles au mythique. Chaque pièce peut être teinte parmi 12 couleurs. Côté armes, chaque classe a 8 rangs (de l'arc court à l'arc de givre, du bokken au nodachi) et chaque rang augmente l'attaque : monter de rang est la façon la plus sûre de passer un gardien qui résiste.</p>

<h2>Porte 5 : le Chef Troll, ton premier mini-boss</h2>
<p>Le premier mini-boss garde la porte 5 de la Forêt de Brume. Les mini-boss et gardiens ont leurs propres attaques : charges, pluies de projectiles, invocations. La règle des zones au sol s'applique encore plus ici. Sa première défaite rapporte un coffre d'or et des potions : ne les gaspille pas, garde-les pour la porte 10.</p>

<h2>Porte 10 : le Roi Gluant</h2>
<p>« Personne ne traverse mon royaume gluant. Incline-toi devant ton roi ! » Le premier gardien est aussi ton premier vrai examen. Si tu bloques, trois leviers avant de réessayer : monter d'un rang d'arme, équiper un sort de zone, et dépenser les potions du Chef Troll. On détaille les dix gardiens dans <a href="/guide/gardiens.html">Les 10 gardiens de Door Knight</a>.</p>

<h2>Entre deux portes : le campement</h2>
<p>Dès que possible, passe par le campement. Il produit du bois, de la pierre et du cristal <em>même quand tu ne joues pas</em>, et renforce tous tes héros. Onze bâtiments à monter (Grand hall, Scierie, Carrière, Mine de cristal, Entrepôt, Tour de guet, Tour arcanique, Caserne, Armurerie, Infirmerie, Marché), chacun avec trois apparences selon son niveau. Toutes les 3 heures, des monstres attaquent le camp : défends le Grand hall vague après vague.</p>

<h2>Chaque jour, sans y penser</h2>
<ul>
<li>Un <strong>cadeau du jour</strong>, trois <strong>quêtes</strong> et une <strong>roue</strong> : récupère-les avant de partir ouvrir des portes.</li>
<li>Un <strong>pseudo</strong> dès la création du héros : c'est lui qui t'inscrit au classement en ligne (tournoi de la semaine, record, arène).</li>
<li>L'<strong>arène</strong> : des duels de 90 secondes contre des joueurs de ton niveau, statistiques équilibrées. C'est ton talent qui compte, pas ton équipement.</li>
</ul>
""",
  'faq': [
   ("Par quel héros commencer Door Knight ?", "Le Chevalier est le plus tolérant pour une première partie : le plus robuste, il frappe en arc de cercle et renvoie les projectiles. L'Archer convient si tu préfères garder tes distances. Tu peux jouer jusqu'à quatre héros."),
   ("À quel niveau débloque-t-on les sorts dans Door Knight ?", "Au niveau 10. Chaque héros a trois écoles et 24 sorts, soit 96 sorts dans le jeu."),
   ("Qu'est-ce qui arrive toutes les 5 et toutes les 10 portes ?", "Un mini-boss toutes les 5 portes, un gardien toutes les 10. Sa première défaite rapporte un coffre d'or et des potions."),
  ]},
 'en': {
  'eyebrow': "Beginner's guide",
  'title': "Door Knight: the beginner's guide to a good start",
  'h1': "Getting started in Door Knight: the first 10 doors",
  'desc': "How to start Door Knight: one-thumb controls, which hero to pick first, spells from level 10, loot, the camp and the first guardian at door 10.",
  'lede': "Just installed the beta? Here is what really matters during the first ten doors, before you meet the Slime King.",
  'image_alt': "The Door Knight knight in front of a door, ready to fight the monsters",
  'body': """
<h2>The idea in one sentence</h2>
<p>Door Knight is an action-adventure game where you open doors, endlessly. Behind each one, a horde of monsters. Every 5 doors a mini-boss; every 10 a guardian who blocks the way out of the world. Ten doors per world, ten worlds, then Circle II starts everything again, deadlier.</p>

<h2>Controls: one thumb to move, one to strike</h2>
<p>Put your thumb anywhere on the screen and slide: your hero follows. Hold the attack button to chain hits: the hero aims at the nearest enemy by itself. So you never aim, you only position. That is the number one skill in the game: staying out of the zones drawn on the ground.</p>
<div class="tip"><b>Remember:</b> every monster announces its spell on the ground before casting it, as a circle, a line or a cone. If you are still inside when it fires, you take poison, burn, slow or snare. Leave the zone first, then strike.</div>

<h2>Which hero to start with?</h2>
<p>Four classes are available from character creation: Knight, Archer, Mage and Samurai. For a first run the <strong>Knight</strong> is the most forgiving: the sturdiest, it strikes in an arc and reflects projectiles. The <strong>Archer</strong> is a good second pick if you prefer to keep your distance. Nothing is final: you can play up to four heroes, each with its own level, gold and armory. We compare all four in <a href="/en/guide/which-hero.html">Which hero should you pick?</a></p>

<h2>Level 10: the Grimoire opens</h2>
<p>From level 10 your hero unlocks spells. Each class has three schools and 24 spells in total (96 in the game). Pick a school, open the Grimoire, and watch the spell's animation before equipping it: Fireball, Blizzard, Phoenix, Celestial Judgment… each has its own. An area spell changes everything against hordes; a control spell (slow, snare) saves lives against mini-bosses.</p>

<h2>Your loot shows on you</h2>
<p>Helmet, armor, boots and talisman found behind the doors appear directly on your hero. Rarity is visible at a glance: a gem from rare, a glow from epic, a gold trim at legendary, sparks at mythic. Every piece can be dyed in one of 12 colors. For weapons, each class has 8 ranks (from the short bow to the frost bow, from the bokken to the nodachi) and every rank raises your attack: ranking up is the surest way past a guardian that keeps beating you.</p>

<h2>Door 5: the Troll Chief, your first mini-boss</h2>
<p>The first mini-boss guards door 5 of Mistwood Forest. Mini-bosses and guardians have attacks of their own: charges, rains of projectiles, summons. The ground-zone rule matters even more here. Beating one for the first time gives a chest of gold and potions: don't waste them, keep them for door 10.</p>

<h2>Door 10: the Slime King</h2>
<p>"Nobody crosses my slimy kingdom. Bow before your king!" The first guardian is also your first real test. If you are stuck, three levers before trying again: rank up your weapon, equip an area spell, and spend the Troll Chief's potions. All ten guardians are covered in <a href="/en/guide/guardians.html">The 10 guardians of Door Knight</a>.</p>

<h2>Between two doors: the camp</h2>
<p>As soon as you can, visit the camp. It produces wood, stone and crystal <em>even when you are not playing</em>, and strengthens all your heroes. Eleven buildings to raise (Great hall, Sawmill, Quarry, Crystal mine, Warehouse, Watchtower, Arcane tower, Barracks, Armory, Infirmary, Market), each with three looks depending on its level. Every 3 hours monsters raid the camp: defend the Great hall wave after wave.</p>

<h2>Every day, without thinking about it</h2>
<ul>
<li>A <strong>daily gift</strong>, three <strong>quests</strong> and a <strong>wheel</strong>: collect them before you go open doors.</li>
<li>A <strong>nickname</strong> at hero creation: that is what enters you in the online leaderboard (weekly tournament, best score, arena).</li>
<li>The <strong>arena</strong>: 90-second duels against players of your level, with balanced stats. Your skill counts, not your gear.</li>
</ul>
""",
  'faq': [
   ("Which hero should I start with in Door Knight?", "The Knight is the most forgiving for a first run: the sturdiest, it strikes in an arc and reflects projectiles. The Archer suits you if you prefer to keep your distance. You can play up to four heroes."),
   ("At what level do you unlock spells in Door Knight?", "At level 10. Each hero has three schools and 24 spells, 96 spells in the game."),
   ("What happens every 5 and every 10 doors?", "A mini-boss every 5 doors, a guardian every 10. Beating one for the first time gives a chest of gold and potions."),
  ]},
},
# ─────────────────────────────────────────────────────────────── 2. Quel héros
{
 'url': {'fr': '/guide/quel-heros-choisir.html', 'en': '/en/guide/which-hero.html'},
 'image': '/img/shot-knight.webp', 'date': '2026-10-30',
 'fr': {
  'eyebrow': 'Les classes',
  'title': "Chevalier, Archer, Mage ou Samouraï : quel héros choisir dans Door Knight ?",
  'h1': "Quel héros choisir ? Chevalier, Archer, Mage et Samouraï comparés",
  'desc': "Comparatif des 4 classes de Door Knight : style de combat, écoles de sorts, attaque spéciale, armes, et pour quel type de joueur chacune est faite.",
  'lede': "Quatre façons d'ouvrir les portes. Voici ce que chaque classe fait vraiment, et laquelle te correspond.",
  'image_alt': "Le chevalier de Door Knight au combat dans le Château Hanté",
  'body': """
<p>Dans Door Knight, chaque héros a son niveau, son or, son armurerie et ses trois écoles de sorts. Tu peux en jouer jusqu'à quatre, donc le choix n'enferme pas. Mais le premier héros est celui avec lequel tu vas apprendre le jeu, et les quatre ne s'apprennent pas de la même manière.</p>

<table>
<tr><th>Héros</th><th>Style</th><th>Écoles de sorts</th><th>Spéciale</th><th>Armes (rang 1 → 8)</th></tr>
<tr><td><strong>Chevalier</strong></td><td>Corps à corps, le plus robuste</td><td>Sacré, Guerre, Terre</td><td>Tourbillon</td><td>Épée → Marteau</td></tr>
<tr><td><strong>Archer</strong></td><td>Distance, flèches perçantes</td><td>Nature, Vent, Ombre</td><td>Volée</td><td>Arc court → Arc de givre</td></tr>
<tr><td><strong>Mage</strong></td><td>Orbes de zone, fragile</td><td>Feu, Glace, Foudre</td><td>Nova</td><td>Bâton d'apprenti → Bâton stellaire</td></tr>
<tr><td><strong>Samouraï</strong></td><td>Enchaînements, mobilité</td><td>Lame, Ki, Sakura</td><td>Ruée Iaijutsu</td><td>Bokken → Nodachi</td></tr>
</table>

<h2>Le Chevalier : pour apprendre sans mourir</h2>
<p>Corps à corps. Il frappe en arc de cercle, ce qui touche plusieurs monstres à la fois quand ils se regroupent, et il <strong>renvoie les projectiles</strong>, ce qui désamorce une bonne partie des pluies de flèches et de sorts des gardiens. C'est le plus robuste des quatre : il pardonne un mauvais placement. Ses écoles (Sacré, Guerre, Terre) vont dans le même sens : tenir, frapper, encaisser. Sa spéciale, Tourbillon, est faite pour les hordes qui t'entourent.</p>
<p><em>Pour qui :</em> les débutants, et ceux qui aiment être au milieu de la mêlée.</p>

<h2>L'Archer : jamais à portée</h2>
<p>Il tire de loin des flèches qui <strong>transpercent les ennemis alignés</strong>. Dans les couloirs de Door Knight, les monstres arrivent souvent en file : une bonne position et une seule flèche traverse toute la ligne. Il n'est jamais à portée, à condition de bouger sans arrêt. Ses écoles Nature, Vent et Ombre ajoutent contrôle et dégâts sur la durée. Sa spéciale, Volée, couvre une zone à distance.</p>
<p><em>Pour qui :</em> ceux qui préfèrent gérer la distance plutôt que l'armure, et qui aiment lire le terrain.</p>

<h2>Le Mage : fragile, mais dévastateur</h2>
<p>Ses orbes arcaniques <strong>explosent en zone</strong> : c'est la classe qui nettoie une horde le plus vite. Le prix, c'est la fragilité. Un Mage qui reste dans un cercle au sol meurt ; un Mage qui bouge entre deux lancers rase tout. Ses trois écoles sont les grands classiques : Feu, Glace, Foudre, avec Boule de feu et Blizzard dès le Grimoire. Sa spéciale, Nova, est l'explosion de secours quand on est entouré.</p>
<p><em>Pour qui :</em> les joueurs qui ont déjà compris la règle des zones au sol et veulent des combats courts et spectaculaires.</p>

<h2>Le Samouraï : la mobilité</h2>
<p>Il enchaîne les coups de katana et <strong>traverse les hordes</strong> d'une Ruée Iaijutsu : la spéciale sert autant à frapper qu'à s'échapper d'une zone annoncée. Écoles Lame, Ki et Sakura. C'est la classe la plus technique : moins robuste que le Chevalier, plus exposé que l'Archer, mais capable de se sortir de situations que les autres ne peuvent pas quitter. Ses armes vont du bokken d'entraînement au nodachi.</p>
<p><em>Pour qui :</em> ceux qui aiment les enchaînements et le placement millimétré ; idéal en second héros.</p>

<h2>Et le bon choix pour l'arène ?</h2>
<p>L'arène oppose des joueurs de ton niveau pendant 90 secondes, avec des statistiques équilibrées : le talent compte, pas l'équipement. Les quatre classes y sont jouables ; ce qui fait la différence, c'est de connaître parfaitement les portées et la spéciale de son héros. Le héros que tu maîtrises le mieux est le bon choix.</p>

<div class="tip"><b>Conseil :</b> commence Chevalier ou Archer, monte-le jusqu'au niveau 10 pour ouvrir le Grimoire et comprendre les sorts, puis crée un Mage ou un Samouraï. Chaque héros garde sa progression, et le campement renforce les quatre.</div>
""",
  'faq': [
   ("Quelle est la classe la plus facile dans Door Knight ?", "Le Chevalier : le plus robuste, il frappe en arc de cercle et renvoie les projectiles, ce qui pardonne les erreurs de placement."),
   ("Peut-on changer de héros dans Door Knight ?", "Oui. Tu peux jouer jusqu'à quatre héros, chacun avec son niveau, son or, son armurerie et ses trois écoles de sorts."),
   ("Combien de sorts a chaque classe ?", "24 sorts par héros, répartis en trois écoles, débloqués à partir du niveau 10. 96 sorts dans le jeu."),
  ]},
 'en': {
  'eyebrow': 'The classes',
  'title': "Knight, Archer, Mage or Samurai: which hero should you pick in Door Knight?",
  'h1': "Which hero should you pick? Knight, Archer, Mage and Samurai compared",
  'desc': "Comparison of the 4 Door Knight classes: fighting style, spell schools, special attack, weapons, and which kind of player each one suits.",
  'lede': "Four ways to open doors. Here is what each class really does, and which one fits you.",
  'image_alt': "The Door Knight knight fighting in the Haunted Castle",
  'body': """
<p>In Door Knight every hero has its own level, gold, armory and three spell schools. You can play up to four, so the choice doesn't lock you in. But your first hero is the one you learn the game with, and the four don't teach it the same way.</p>

<table>
<tr><th>Hero</th><th>Style</th><th>Spell schools</th><th>Special</th><th>Weapons (rank 1 → 8)</th></tr>
<tr><td><strong>Knight</strong></td><td>Melee, the sturdiest</td><td>Holy, War, Earth</td><td>Whirlwind</td><td>Sword → Hammer</td></tr>
<tr><td><strong>Archer</strong></td><td>Ranged, piercing arrows</td><td>Nature, Wind, Shadow</td><td>Volley</td><td>Short bow → Frost bow</td></tr>
<tr><td><strong>Mage</strong></td><td>Area orbs, fragile</td><td>Fire, Ice, Lightning</td><td>Nova</td><td>Apprentice staff → Stellar staff</td></tr>
<tr><td><strong>Samurai</strong></td><td>Combos, mobility</td><td>Blade, Ki, Sakura</td><td>Iaijutsu Dash</td><td>Bokken → Nodachi</td></tr>
</table>

<h2>The Knight: learn without dying</h2>
<p>Melee. It strikes in an arc, which hits several monsters at once when they bunch up, and it <strong>reflects projectiles</strong>, which defuses a good part of the guardians' arrow and spell rains. It is the sturdiest of the four: it forgives a bad position. Its schools (Holy, War, Earth) all point the same way: hold, hit, take it. Its special, Whirlwind, is made for hordes surrounding you.</p>
<p><em>For whom:</em> beginners, and anyone who likes being in the middle of the fight.</p>

<h2>The Archer: never in reach</h2>
<p>It shoots from afar with arrows that <strong>pierce enemies in a line</strong>. In Door Knight's corridors monsters often come single file: with a good position, one arrow goes through the whole line. It is never in reach, as long as you keep moving. Its Nature, Wind and Shadow schools add control and damage over time. Its special, Volley, covers an area at range.</p>
<p><em>For whom:</em> players who would rather manage distance than armor, and who like reading the ground.</p>

<h2>The Mage: fragile, but devastating</h2>
<p>Its arcane orbs <strong>explode in an area</strong>: it is the class that clears a horde fastest. The price is fragility. A Mage standing in a circle on the ground dies; a Mage moving between two casts wipes everything. Its three schools are the great classics: Fire, Ice, Lightning, with Fireball and Blizzard right from the Grimoire. Its special, Nova, is the emergency blast when surrounded.</p>
<p><em>For whom:</em> players who already understand the ground-zone rule and want short, spectacular fights.</p>

<h2>The Samurai: mobility</h2>
<p>It chains katana hits and <strong>dashes through hordes</strong> with Iaijutsu Dash: the special is as much for striking as for escaping a zone that was just announced. Blade, Ki and Sakura schools. It is the most technical class: less sturdy than the Knight, more exposed than the Archer, but able to get out of situations the others cannot leave. Its weapons go from the training bokken to the nodachi.</p>
<p><em>For whom:</em> players who love combos and pixel-perfect positioning; ideal as a second hero.</p>

<h2>And the right pick for the arena?</h2>
<p>The arena pits you against players of your level for 90 seconds with balanced stats: skill counts, not gear. All four classes are viable; what makes the difference is knowing your hero's ranges and special inside out. The hero you master best is the right pick.</p>

<div class="tip"><b>Tip:</b> start Knight or Archer, take it to level 10 to open the Grimoire and understand spells, then create a Mage or a Samurai. Every hero keeps its progress, and the camp strengthens all four.</div>
""",
  'faq': [
   ("What is the easiest class in Door Knight?", "The Knight: the sturdiest, it strikes in an arc and reflects projectiles, which forgives positioning mistakes."),
   ("Can you switch heroes in Door Knight?", "Yes. You can play up to four heroes, each with its own level, gold, armory and three spell schools."),
   ("How many spells does each class have?", "24 spells per hero, split into three schools, unlocked from level 10. 96 spells in the game."),
  ]},
},
# ─────────────────────────────────────────────────────────────── 3. Gardiens
{
 'url': {'fr': '/guide/gardiens.html', 'en': '/en/guide/guardians.html'},
 'image': '/img/shot-door.webp', 'date': '2026-10-30',
 'fr': {
  'eyebrow': 'Les gardiens',
  'title': "Les 10 gardiens de Door Knight : qui ils sont et comment les aborder",
  'h1': "Les 10 gardiens de Door Knight, porte par porte",
  'desc': "Du Roi Gluant au Dragon Ancestral : les 10 gardiens de Door Knight, leur monde, leur mini-boss, leur réplique, et les règles qui valent contre tous.",
  'lede': "Un gardien toutes les 10 portes, un mini-boss toutes les 5. Voici qui t'attend, monde par monde, et ce qui marche contre eux.",
  'image_alt': "L'entrée de la porte 72 au Château Hanté dans Door Knight",
  'body': """
<p>Chaque monde de Door Knight fait dix portes. À la porte 5, un mini-boss ; à la porte 10, le gardien du monde. Chacun a ses propres attaques (charges, pluies de projectiles, invocations) et sa première défaite rapporte un coffre d'or et des potions. Après le dixième gardien, le Cercle II recommence les dix mondes, plus redoutables, et change l'ambiance (jour, crépuscule, nuit, lune de sang).</p>

<table>
<tr><th>Portes</th><th>Monde</th><th>Mini-boss (porte 5)</th><th>Gardien (porte 10)</th></tr>
<tr><td>1–10</td><td>Forêt de Brume</td><td>Chef Troll</td><td>Roi Gluant</td></tr>
<tr><td>11–20</td><td>Grottes d'Écho</td><td>Capitaine Squelette</td><td>Seigneur des Os</td></tr>
<tr><td>21–30</td><td>Marais Putride</td><td>Sorcière des Marais</td><td>Mère des Crapauds</td></tr>
<tr><td>31–40</td><td>Désert d'Ambre</td><td>Gardien Anubis</td><td>Pharaon Maudit</td></tr>
<tr><td>41–50</td><td>Pics Gelés</td><td>Loup Alpha</td><td>Colosse des Cimes</td></tr>
<tr><td>51–60</td><td>Forge Volcanique</td><td>Colosse de Magma</td><td>Minotaure de Lave</td></tr>
<tr><td>61–70</td><td>Cité Engloutie</td><td>Sirène Noire</td><td>Kraken des Abysses</td></tr>
<tr><td>71–80</td><td>Château Hanté</td><td>Gargouille Ancienne</td><td>Chevalier Noir</td></tr>
<tr><td>81–90</td><td>Cieux d'Orage</td><td>Reine Déchue</td><td>Griffon Tonnerre</td></tr>
<tr><td>91–100</td><td>Antre du Dragon</td><td>Drake Écarlate</td><td>Dragon Ancestral</td></tr>
</table>

<h2>Les règles qui valent contre les dix</h2>
<ul>
<li><strong>Lis le sol.</strong> Comme les monstres, les gardiens annoncent leurs attaques par des zones au sol. Une charge se voit venir ; une pluie de projectiles aussi. Sors d'abord, frappe ensuite.</li>
<li><strong>Les invocations d'abord.</strong> Quand un gardien appelle des monstres, ils annoncent eux aussi leurs sorts. Un sort de zone (Mage, Chevalier en Tourbillon, Volée de l'Archer) nettoie les invocations avant qu'elles ne t'encerclent.</li>
<li><strong>Les projectiles sont une ressource pour le Chevalier.</strong> Il les renvoie. Face à un gardien qui mitraille, c'est la classe qui souffre le moins.</li>
<li><strong>Un rang d'arme avant de réessayer.</strong> Chaque rang augmente l'attaque. Si le combat dure trop longtemps, le problème est souvent là, pas dans ton placement.</li>
<li><strong>Les potions des mini-boss sont pour les gardiens.</strong> Le mini-boss de la porte 5 te donne de quoi tenir à la porte 10.</li>
</ul>

<h2>Les dix, dans leurs mots</h2>
<p>Chaque gardien se présente avant le combat, à voix haute. Voici leur réplique et celle de leur mini-boss.</p>

<h3>Porte 10 · Roi Gluant (Forêt de Brume)</h3>
<p>« Personne ne traverse mon royaume gluant. Incline-toi devant ton roi ! » Son mini-boss, le Chef Troll : « Personne ne traverse ma forêt… La brume va engloutir tes os ! » Le premier examen du jeu : c'est ici qu'on apprend à sortir des zones.</p>

<h3>Porte 20 · Seigneur des Os (Grottes d'Écho)</h3>
<p>« Tes os rejoindront ma collection. Il me manquait justement un héros. » Avant lui, le Capitaine Squelette : « Écoute l'écho, mortel… c'est le dernier son que tu entendras. »</p>

<h3>Porte 30 · Mère des Crapauds (Marais Putride)</h3>
<p>« Mes enfants ont faim… et toi, tu sens bon le festin. » Le marais est le monde du poison : garde une potion. Mini-boss, la Sorcière des Marais : « Hé hé… encore un héros pour mon chaudron. Le marais n'oublie jamais ! »</p>

<h3>Porte 40 · Pharaon Maudit (Désert d'Ambre)</h3>
<p>« Mon tombeau ne s'ouvre qu'une fois. Tu n'en ressortiras pas. » Mini-boss, le Gardien Anubis : « Le sable a pesé ton cœur. Il est trop léger pour franchir cette porte. »</p>

<h3>Porte 50 · Colosse des Cimes (Pics Gelés)</h3>
<p>« La montagne ne recule devant personne. Tu vas être enseveli ! » Les Pics Gelés sont le monde de la lenteur : un héros ralenti dans une zone au sol n'en sort plus. Mini-boss, le Loup Alpha : « Grrr… La meute a faim. Et la glace garde bien la viande. »</p>

<h3>Porte 60 · Minotaure de Lave (Forge Volcanique)</h3>
<p>« Ma lave a forgé des armes plus dures que toi. À genoux ! » Mini-boss, le Colosse de Magma : « La forge a soif d'acier. Ton armure fondra comme de la cire ! » Le monde de la brûlure.</p>

<h3>Porte 70 · Kraken des Abysses (Cité Engloutie)</h3>
<p>« La marée monte, petit héros… Personne ne remonte des abysses. » Mini-boss, la Sirène Noire : « Approche… Écoute mon chant. Les abysses t'attendent. »</p>

<h3>Porte 80 · Chevalier Noir (Château Hanté)</h3>
<p>« Je garde ce château depuis mille ans. Croise le fer, si tu l'oses. » Un duel : le gardien le plus proche d'un affrontement de joueur à joueur. Mini-boss, la Gargouille Ancienne : « Mille ans de pierre… et je ne m'éveille que pour toi. »</p>

<h3>Porte 90 · Griffon Tonnerre (Cieux d'Orage)</h3>
<p>« Le ciel gronde pour toi… La foudre sera ta dernière lumière. » Mini-boss, la Reine Déchue : « J'ai perdu ma couronne dans l'orage… Je prendrai ta tête à la place. »</p>

<h3>Porte 100 · Dragon Ancestral (Antre du Dragon)</h3>
<p>« Cent portes… et tu crois pouvoir me défier ? Brûle, mortel ! » Le dernier gardien du Cercle I. Mini-boss, le Drake Écarlate : « Tu sens cette chaleur ? Mon maître dort plus loin… tu n'iras pas jusqu'à lui. » Après lui, le Cercle II commence : les mêmes dix mondes, plus redoutables, sans fin.</p>

<div class="tip"><b>Tu bloques sur un gardien ?</b> Dis-le dans #gameplay sur le Discord avec ta classe et ton rang d'arme : les autres joueurs y partagent leurs stratégies, et l'équipe lit tout pour équilibrer le jeu.</div>
""",
  'faq': [
   ("Combien de gardiens y a-t-il dans Door Knight ?", "Dix, un par monde, à chaque porte multiple de 10 : Roi Gluant, Seigneur des Os, Mère des Crapauds, Pharaon Maudit, Colosse des Cimes, Minotaure de Lave, Kraken des Abysses, Chevalier Noir, Griffon Tonnerre et Dragon Ancestral. Après le dixième, le Cercle II recommence."),
   ("Que gagne-t-on en battant un gardien ?", "Sa première défaite rapporte un coffre d'or et des potions."),
   ("Qu'y a-t-il après la porte 100 ?", "Le Cercle II : les dix mêmes mondes, plus redoutables, avec une ambiance qui change (jour, crépuscule, nuit, lune de sang), et ainsi de suite sans fin."),
  ]},
 'en': {
  'eyebrow': 'The guardians',
  'title': "The 10 guardians of Door Knight: who they are and how to approach them",
  'h1': "The 10 guardians of Door Knight, door by door",
  'desc': "From the Slime King to the Ancestral Dragon: the 10 guardians of Door Knight, their world, their mini-boss, their line, and the rules that work against all of them.",
  'lede': "A guardian every 10 doors, a mini-boss every 5. Here is who is waiting, world by world, and what works against them.",
  'image_alt': "The entrance of door 72 in the Haunted Castle in Door Knight",
  'body': """
<p>Every Door Knight world is ten doors long. At door 5, a mini-boss; at door 10, the world's guardian. Each has its own attacks (charges, rains of projectiles, summons) and beating it for the first time gives a chest of gold and potions. After the tenth guardian, Circle II restarts the ten worlds, deadlier, and changes the mood (day, dusk, night, blood moon).</p>

<table>
<tr><th>Doors</th><th>World</th><th>Mini-boss (door 5)</th><th>Guardian (door 10)</th></tr>
<tr><td>1–10</td><td>Mistwood Forest</td><td>Troll Chief</td><td>Slime King</td></tr>
<tr><td>11–20</td><td>Echo Caves</td><td>Skeleton Captain</td><td>Bone Lord</td></tr>
<tr><td>21–30</td><td>Putrid Swamp</td><td>Swamp Witch</td><td>Mother of Toads</td></tr>
<tr><td>31–40</td><td>Amber Desert</td><td>Anubis Guardian</td><td>Cursed Pharaoh</td></tr>
<tr><td>41–50</td><td>Frozen Peaks</td><td>Alpha Wolf</td><td>Colossus of the Peaks</td></tr>
<tr><td>51–60</td><td>Volcanic Forge</td><td>Magma Colossus</td><td>Lava Minotaur</td></tr>
<tr><td>61–70</td><td>Sunken City</td><td>Black Siren</td><td>Abyssal Kraken</td></tr>
<tr><td>71–80</td><td>Haunted Castle</td><td>Ancient Gargoyle</td><td>Black Knight</td></tr>
<tr><td>81–90</td><td>Storm Skies</td><td>Fallen Queen</td><td>Thunder Griffin</td></tr>
<tr><td>91–100</td><td>Dragon's Lair</td><td>Scarlet Drake</td><td>Ancestral Dragon</td></tr>
</table>

<h2>The rules that work against all ten</h2>
<ul>
<li><strong>Read the ground.</strong> Like monsters, guardians announce their attacks with zones on the ground. A charge can be seen coming; so can a rain of projectiles. Get out first, strike second.</li>
<li><strong>Summons first.</strong> When a guardian calls monsters, they announce their spells too. An area spell (Mage, Knight's Whirlwind, Archer's Volley) clears the summons before they surround you.</li>
<li><strong>Projectiles are a resource for the Knight.</strong> It reflects them. Against a guardian that sprays, it is the class that suffers least.</li>
<li><strong>One weapon rank before retrying.</strong> Every rank raises your attack. If the fight drags on too long, the problem is often there, not in your positioning.</li>
<li><strong>Mini-boss potions are for guardians.</strong> The door-5 mini-boss gives you what you need to hold on at door 10.</li>
</ul>

<h2>The ten, in their own words</h2>
<p>Every guardian introduces itself before the fight, out loud. Here is its line and its mini-boss's.</p>

<h3>Door 10 · Slime King (Mistwood Forest)</h3>
<p>"Nobody crosses my slimy kingdom. Bow before your king!" Its mini-boss, the Troll Chief: "Nobody crosses my forest… The mist will swallow your bones!" The game's first test: this is where you learn to leave the zones.</p>

<h3>Door 20 · Bone Lord (Echo Caves)</h3>
<p>"Your bones will join my collection. I was just missing a hero." Before it, the Skeleton Captain: "Listen to the echo, mortal… it is the last sound you will hear."</p>

<h3>Door 30 · Mother of Toads (Putrid Swamp)</h3>
<p>"My children are hungry… and you smell like a feast." The swamp is the world of poison: keep a potion. Mini-boss, the Swamp Witch: "Heh heh… another hero for my cauldron. The swamp never forgets!"</p>

<h3>Door 40 · Cursed Pharaoh (Amber Desert)</h3>
<p>"My tomb opens only once. You will not come out." Mini-boss, the Anubis Guardian: "The sand has weighed your heart. It is too light to pass this door."</p>

<h3>Door 50 · Colossus of the Peaks (Frozen Peaks)</h3>
<p>"The mountain backs down from no one. You will be buried!" The Frozen Peaks are the world of slow: a slowed hero inside a ground zone doesn't get out. Mini-boss, the Alpha Wolf: "Grrr… The pack is hungry. And ice keeps the meat well."</p>

<h3>Door 60 · Lava Minotaur (Volcanic Forge)</h3>
<p>"My lava has forged weapons harder than you. On your knees!" Mini-boss, the Magma Colossus: "The forge thirsts for steel. Your armor will melt like wax!" The world of burn.</p>

<h3>Door 70 · Abyssal Kraken (Sunken City)</h3>
<p>"The tide is rising, little hero… Nobody comes back up from the abyss." Mini-boss, the Black Siren: "Come closer… Listen to my song. The abyss awaits you."</p>

<h3>Door 80 · Black Knight (Haunted Castle)</h3>
<p>"I have guarded this castle for a thousand years. Cross swords, if you dare." A duel: the guardian closest to a player-versus-player fight. Mini-boss, the Ancient Gargoyle: "A thousand years of stone… and I wake only for you."</p>

<h3>Door 90 · Thunder Griffin (Storm Skies)</h3>
<p>"The sky rumbles for you… Lightning will be your last light." Mini-boss, the Fallen Queen: "I lost my crown in the storm… I will take your head instead."</p>

<h3>Door 100 · Ancestral Dragon (Dragon's Lair)</h3>
<p>"A hundred doors… and you think you can challenge me? Burn, mortal!" The last guardian of Circle I. Mini-boss, the Scarlet Drake: "Feel that heat? My master sleeps further in… you will not reach him." After it, Circle II begins: the same ten worlds, deadlier, without end.</p>

<div class="tip"><b>Stuck on a guardian?</b> Say so in #gameplay on the Discord with your class and weapon rank: other players share their strategies there, and the team reads everything to balance the game.</div>
""",
  'faq': [
   ("How many guardians are there in Door Knight?", "Ten, one per world, at every door that is a multiple of 10: Slime King, Bone Lord, Mother of Toads, Cursed Pharaoh, Colossus of the Peaks, Lava Minotaur, Abyssal Kraken, Black Knight, Thunder Griffin and Ancestral Dragon. After the tenth, Circle II starts again."),
   ("What do you get for beating a guardian?", "Beating it for the first time gives a chest of gold and potions."),
   ("What comes after door 100?", "Circle II: the same ten worlds, deadlier, with a changing mood (day, dusk, night, blood moon), and so on without end."),
  ]},
},
# ─────────────────────────────────────────────────────────────── 4. TestFlight
{
 'url': {'fr': '/guide/installer-la-beta-testflight.html', 'en': '/en/guide/install-beta-testflight.html'},
 'image': '/img/shot-title.webp', 'date': '2026-10-30',
 'fr': {
  'eyebrow': 'Installation',
  'title': "Installer la bêta de Door Knight sur iPhone et iPad avec TestFlight",
  'h1': "Installer la bêta Door Knight sur iPhone et iPad (TestFlight)",
  'desc': "Pas à pas : installer TestFlight, ouvrir le lien de la bêta Door Knight, installer le jeu, recevoir les mises à jour et signaler un bug. Gratuit, sur iPhone et iPad.",
  'lede': "Trois étapes, cinq minutes. Et tout ce qu'il faut savoir sur les mises à jour, les achats en mode test et Android.",
  'image_alt': "L'écran titre de Door Knight",
  'body': """
<p>Door Knight n'est pas encore sur l'App Store. En attendant, le jeu est ouvert à tous via <strong>TestFlight</strong>, l'application officielle d'Apple pour tester les applications avant leur sortie. Tu joues à la vraie version du jeu, et tes retours aident à la finir.</p>

<h2>Étape 1 · Installe TestFlight</h2>
<p>Ouvre l'App Store sur ton iPhone ou ton iPad, cherche <strong>TestFlight</strong> (éditeur : Apple) et installe-le. C'est gratuit. Si tu l'as déjà, passe à l'étape 2.</p>

<h2>Étape 2 · Ouvre le lien de la bêta</h2>
<p>Depuis ton iPhone ou iPad, ouvre ce lien : <a href="https://testflight.apple.com/join/Jhxx6gj1" target="_blank" rel="noopener">testflight.apple.com/join/Jhxx6gj1</a>. TestFlight s'ouvre et te propose de rejoindre la bêta de Door Knight. Accepte.</p>

<h2>Étape 3 · Installe et joue</h2>
<p>Appuie sur <strong>Installer</strong> dans TestFlight. L'icône de Door Knight apparaît sur ton écran d'accueil comme n'importe quel jeu. Lance-le, crée ton héros avec un pseudo, et ouvre la première porte.</p>

<h2>Les mises à jour</h2>
<p>TestFlight t'avertit à chaque nouvelle version. Installe-la pour continuer à jouer : chaque version de test dure 90 jours. Les nouveautés de chaque mise à jour sont publiées dans le salon #nouveautés du Discord.</p>

<h2>Les achats dans la bêta</h2>
<p>Les achats intégrés sont en <strong>mode test</strong> pendant la bêta : rien n'est débité, jamais. Tu peux les essayer librement.</p>

<h2>Signaler un bug</h2>
<p>Deux façons : fais une capture d'écran dans le jeu et envoie-la depuis TestFlight (il le propose automatiquement après une capture), ou poste-la dans le forum <strong>#bugs</strong> du Discord avec ton modèle de téléphone et ton pseudo. Un post par bug, en vérifiant d'abord qu'il n'existe pas déjà.</p>

<h2>Et sur Android ?</h2>
<p>La bêta est pour l'instant réservée à l'iPhone et à l'iPad. La version Android est en préparation et sortira sur Google Play ; la date sera annoncée en premier sur le Discord et sur Instagram.</p>

<div class="tip"><b>Ça ne marche pas ?</b> Vérifie que tu ouvres le lien depuis l'appareil où TestFlight est installé (pas depuis un ordinateur), et que ton iPhone ou iPad est à jour. Sinon, demande dans #taverne sur le Discord.</div>
""",
  'faq': [
   ("Door Knight est-il sur l'App Store ?", "Pas encore. Le jeu est en bêta ouverte, gratuite, via TestFlight sur iPhone et iPad. La sortie sur l'App Store et Google Play sera annoncée sur le Discord et sur Instagram."),
   ("Les achats dans la bêta sont-ils payants ?", "Non. Pendant la bêta, les achats intégrés sont en mode test : rien n'est débité."),
   ("Combien de temps dure une version de test ?", "90 jours. TestFlight t'avertit à chaque nouvelle version ; il suffit de l'installer pour continuer."),
  ]},
 'en': {
  'eyebrow': 'Installation',
  'title': "Install the Door Knight beta on iPhone and iPad with TestFlight",
  'h1': "Install the Door Knight beta on iPhone and iPad (TestFlight)",
  'desc': "Step by step: install TestFlight, open the Door Knight beta link, install the game, get updates and report a bug. Free, on iPhone and iPad.",
  'lede': "Three steps, five minutes. Plus everything about updates, test-mode purchases and Android.",
  'image_alt': "The Door Knight title screen",
  'body': """
<p>Door Knight is not on the App Store yet. In the meantime the game is open to everyone through <strong>TestFlight</strong>, Apple's official app for testing apps before release. You play the real version of the game, and your feedback helps finish it.</p>

<h2>Step 1 · Install TestFlight</h2>
<p>Open the App Store on your iPhone or iPad, search for <strong>TestFlight</strong> (by Apple) and install it. It's free. If you already have it, go to step 2.</p>

<h2>Step 2 · Open the beta link</h2>
<p>From your iPhone or iPad, open this link: <a href="https://testflight.apple.com/join/Jhxx6gj1" target="_blank" rel="noopener">testflight.apple.com/join/Jhxx6gj1</a>. TestFlight opens and offers to join the Door Knight beta. Accept.</p>

<h2>Step 3 · Install and play</h2>
<p>Tap <strong>Install</strong> in TestFlight. The Door Knight icon appears on your home screen like any other game. Launch it, create your hero with a nickname, and open the first door.</p>

<h2>Updates</h2>
<p>TestFlight notifies you of every new version. Install it to keep playing: each test build lasts 90 days. What's new in each update is posted in the #nouveautés channel of the Discord.</p>

<h2>Purchases in the beta</h2>
<p>In-app purchases are in <strong>test mode</strong> during the beta: nothing is ever charged. Feel free to try them.</p>

<h2>Reporting a bug</h2>
<p>Two ways: take a screenshot in the game and send it from TestFlight (it offers to, right after a screenshot), or post it in the <strong>#bugs</strong> forum on the Discord with your phone model and nickname. One post per bug, after checking it doesn't exist already.</p>

<h2>What about Android?</h2>
<p>For now the beta is only for iPhone and iPad. The Android version is in the works and will be released on Google Play; the date will be announced first on the Discord and on Instagram.</p>

<div class="tip"><b>Not working?</b> Make sure you open the link from the device where TestFlight is installed (not from a computer), and that your iPhone or iPad is up to date. Otherwise, ask in #taverne on the Discord.</div>
""",
  'faq': [
   ("Is Door Knight on the App Store?", "Not yet. The game is in a free open beta through TestFlight on iPhone and iPad. The App Store and Google Play release will be announced on the Discord and on Instagram."),
   ("Do purchases in the beta cost money?", "No. During the beta, in-app purchases are in test mode: nothing is charged."),
   ("How long does a test build last?", "90 days. TestFlight notifies you of every new version; just install it to keep playing."),
  ]},
},
]
