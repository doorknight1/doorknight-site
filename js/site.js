(function(){
  // anti-cadre : le site refuse d'être affiché dans un cadre d'un autre site (clickjacking)
  try{if(window.top!==window.self){window.top.location=window.self.location;}}catch(e){document.documentElement.style.display='none';}

  // les animations, la porte et la musique sont le cœur du site : elles restent actives même si l'ordinateur demande moins d'animations
  var reduce=false;

  // ===== Langues du jeu : français, anglais, espagnol, allemand =====
  var I18=(function(){
    var D=JSON.parse(document.getElementById('i18nData').textContent),IX={en:0,es:1,de:2},CODES=['fr','en','es','de'],lang='fr',nodes=[],attrs=[],subs=[];
    // images qui contiennent du texte du jeu : une version par langue (img/<langue>/...)
    var LOC=/(^|\/)(shot-[\w-]+|cls-[\w-]+|camp-(meadow|autumn|snow|arcane)|raid)\.webp$/;
    function key(x){return x.replace(/’/g,"'").replace(/\s+/g,' ').trim();}
    function T(fr){if(lang==='fr'||fr==null)return fr;var v=D[key(fr)];return v?v[IX[lang]]:fr;}
    function img(path){if(lang==='fr'||!LOC.test(path)||/^\/img\/(camp\/)?(en|es|de)\//.test(path))return path;return path.replace(/^\/img\/(camp\/)?/,function(m,c){return '/img/'+(c||'')+lang+'/';});}
    function collect(){
      var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,{acceptNode:function(n){var p=n.parentNode&&n.parentNode.nodeName;
        if(p==='SCRIPT'||p==='STYLE')return NodeFilter.FILTER_REJECT;return D[key(n.nodeValue)]?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_SKIP;}});
      for(var n;(n=w.nextNode());)nodes.push([n,n.nodeValue]);
      [].forEach.call(document.querySelectorAll('[alt],[title],[aria-label]'),function(el){['alt','title','aria-label'].forEach(function(a){var v=el.getAttribute(a);if(v&&D[key(v)])attrs.push([el,a,v]);});});
      var md=document.querySelector('meta[name="description"]');if(md)attrs.push([md,'content',md.getAttribute('content')]);
    }
    function apply(l){lang=l;var h=document.documentElement;h.lang=l;h.dataset.lang=l;
      nodes.forEach(function(x){var fr=x[1],m=fr.match(/^(\s*)([\s\S]*?)(\s*)$/);x[0].nodeValue=l==='fr'?fr:m[1]+T(m[2])+m[3];});
      attrs.forEach(function(x){x[0].setAttribute(x[1],T(x[2]));});
      [].forEach.call(document.querySelectorAll('img[src]'),function(im){var o=im.dataset.src0||(im.dataset.src0=im.getAttribute('src'));var nw=img(o);if(im.getAttribute('src')!==nw)im.setAttribute('src',nw);});
      [].forEach.call(document.querySelectorAll('a[href^="/mentions-legales"],a[href^="/politique-confidentialite"]'),function(a){var b=a.getAttribute('href').replace(/(-(en|es|de))?\.html$/,'');a.setAttribute('href',b+(l==='fr'?'':'-'+l)+'.html');});
      var cur=document.getElementById('langCur');if(cur)cur.textContent=l.toUpperCase();
      [].forEach.call(document.querySelectorAll('#langMenu [data-l]'),function(b){b.setAttribute('aria-checked',String(b.dataset.l===l));});
      subs.forEach(function(fn){try{fn(l);}catch(e){}});}
    // Chaque langue a sa propre adresse (/, /en/, /es/, /de/) : mieux pour le référencement. La page affiche sa langue ; on ne traduit plus à la volée.
    var PAGE=(document.documentElement.getAttribute('lang')||'fr').slice(0,2).toLowerCase();if(CODES.indexOf(PAGE)<0)PAGE='fr';
    function urlFor(l){return (l==='fr'?'/':'/'+l+'/')+(location.hash||'');}
    function stored(){var s=null;try{s=localStorage.getItem('dkLang');}catch(e){}return CODES.indexOf(s)>=0?s:null;}
    function wanted(){var list=navigator.languages&&navigator.languages.length?navigator.languages:[navigator.language||'en'];
      for(var i=0;i<list.length;i++){var c=String(list[i]).slice(0,2).toLowerCase();if(CODES.indexOf(c)>=0)return c;}return null;}
    collect();apply(PAGE);
    var st=stored();
    if(st&&st!==PAGE){location.replace(urlFor(st));}
    // pas de bandeau « ce site existe aussi en … » (retiré à la demande d'Antoine) : le choix de langue reste dans le menu
    // bandeau discret : « ce site existe dans ta langue » (texte dans la langue proposée)
    function langBar(w){var BAR={fr:['Ce site existe aussi en français.','Passer en français','Fermer'],en:['This site is also available in English.','Switch to English','Close'],es:['Este sitio también está disponible en español.','Cambiar a español','Cerrar'],de:['Diese Seite gibt es auch auf Deutsch.','Auf Deutsch wechseln','Schließen']}[w];
      var d=document.createElement('div');d.className='langbar';d.setAttribute('lang',w);d.innerHTML='<span></span><a href="'+urlFor(w)+'"></a><button type="button" aria-label=""></button>';
      d.firstChild.textContent=BAR[0];d.children[1].textContent=BAR[1];d.children[2].setAttribute('aria-label',BAR[2]);d.children[2].textContent='×';
      d.children[1].addEventListener('click',function(){try{localStorage.setItem('dkLang',w);}catch(_){}});
      d.children[2].addEventListener('click',function(){try{localStorage.setItem('dkLang',PAGE);}catch(_){}d.remove();});
      document.body.appendChild(d);}
    // menu
    var btn=document.getElementById('langBtn'),menu=document.getElementById('langMenu');
    function open(v){menu.hidden=!v;btn.setAttribute('aria-expanded',String(v));}
    if(btn){btn.addEventListener('click',function(e){e.stopPropagation();open(menu.hidden);});
      menu.addEventListener('click',function(e){var b=e.target.closest('[data-l]');if(!b)return;try{localStorage.setItem('dkLang',b.dataset.l);}catch(_){}open(false);if(b.dataset.l!==PAGE)location.href=urlFor(b.dataset.l);});
      document.addEventListener('click',function(e){if(!menu.hidden&&!e.target.closest('#langBox'))open(false);});
      document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!menu.hidden){open(false);btn.focus();}});}
    return {T:T,img:img,lang:function(){return lang;},on:function(fn){subs.push(fn);}};
  })();
  var T=I18.T;
  document.getElementById('year').textContent=new Date().getFullYear();

  // bande-annonce en vedette : muette en boucle, le son au clic ; ne tourne que lorsqu'elle est visible
  (function(){
    var v=document.getElementById('trailerVid'),b=document.getElementById('trailerSnd');if(!v)return;
    var l=I18.lang(),sfx=l==='fr'?'':'-'+l,want='/vid/trailer-hero'+sfx+'.mp4';
    if(v.getAttribute('data-src')!==want){v.poster='/vid/intro-landscape'+sfx+'.jpg';v.src=want;v.setAttribute('data-src',want);v.load();}
    function tryPlay(){var p=v.play();if(p&&p.catch)p.catch(function(){});}
    if('IntersectionObserver' in window){
      new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting)tryPlay();else v.pause();});},{threshold:.2}).observe(v);
    }else tryPlay();
    afterIntro(tryPlay);
    if(b)b.addEventListener('click',function(){v.muted=!v.muted;var on=!v.muted;b.classList.toggle('on',on);b.setAttribute('aria-pressed',String(on));
      b.querySelector('span').textContent=T(on?'Couper le son':'Activer le son');b.title=b.querySelector('span').textContent;
      if(on){try{DKA.duck(true);}catch(e){}}else{try{DKA.duck(false);}catch(e){}}
      if(v.paused)tryPlay();});
    v.addEventListener('click',function(){if(v.paused)tryPlay();else if(b)b.click();});
  })();

  // héros
  var H=[
    {n:'Le Chevalier',d:"Corps à corps. Frappe en arc de cercle et renvoie les projectiles. Le plus robuste.",c:['Sacré','Guerre','Terre','Spéciale : Tourbillon','Épée → Marteau'],img:'/img/cls-chevalier.webp'},
    {n:"L'Archer",d:"Tire de loin des flèches qui transpercent les ennemis alignés. Jamais à portée.",c:['Nature','Vent','Ombre','Spéciale : Volée',"Arc court → Arc de givre"],img:'/img/cls-archer.webp'},
    {n:'Le Mage',d:"Lance des orbes arcaniques qui explosent en zone. Fragile, mais dévastateur.",c:['Feu','Glace','Foudre','Spéciale : Nova',"Bâton d'apprenti → Bâton stellaire"],img:'/img/cls-mage.webp'},
    {n:'Le Samouraï',d:"Enchaîne les coups de katana et traverse les hordes d'une ruée Iaijutsu.",c:['Lame','Ki','Sakura','Spéciale : Ruée Iaijutsu','Bokken → Nodachi'],img:'/img/cls-samourai.webp'}
  ];

  // ===== Son du jeu : musique « theme » (Suno), bruitages des sorts, voix des gardiens =====
  var DKA=(function(){
    // La musique passe par un simple élément <audio> lancé dans le geste (toucher/clic) : c'est ce qui marche partout,
    // y compris sur iPhone en mode silencieux. Le fichier commence par 2,4 s de silence puis un fondu : la musique
    // arrive d'elle-même quand le logo apparaît, sans minuterie.
    var on=false,ac=null,mus=null,bufs={},duckN=0,btn=document.getElementById('sndBtn'),volOK=null,LEAD=2.4,LOOP=4.6,waiting=false;
    try{if(navigator.audioSession)navigator.audioSession.type='playback';}catch(e){}
    try{on=sessionStorage.getItem('dkSnd')==='1';}catch(e){}
    function ctx(){if(!ac){var AC=window.AudioContext||window.webkitAudioContext;if(!AC)return null;ac=new AC();}
      if(ac.state==='suspended'&&ac.resume)ac.resume();return ac;}
    function music(){if(!mus){mus=new Audio();mus.preload='auto';mus.setAttribute('playsinline','');mus.src='/audio/theme-site.mp3';
        mus.addEventListener('ended',function(){if(on){try{mus.currentTime=LOOP;}catch(e){}play();}});
        mus.volume=.5;volOK=mus.volume<.9;mus.volume=1;}   // iPhone : volume fixe (on met en pause au lieu de baisser)
      return mus;}
    function play(){var p=mus.play();if(p&&p.catch)p.catch(function(){retry();});}
    // si le navigateur refuse quand même, la musique part au prochain toucher, n'importe où sur la page
    function retry(){if(waiting)return;waiting=true;var go=function(){removeEventListener('pointerdown',go,true);removeEventListener('keydown',go,true);
      waiting=false;if(on&&mus&&mus.paused){if(mus.currentTime<LEAD){try{mus.currentTime=LEAD;}catch(e){}}play();}};addEventListener('pointerdown',go,true);addEventListener('keydown',go,true);}
    function apply(){if(!mus||!on)return;
      if(document.hidden){mus.pause();return;}
      if(volOK){mus.volume=duckN>0?.22:1;if(mus.paused)play();}
      else if(duckN>0){mus.pause();}else if(mus.paused)play();}
    function ui(){if(btn){btn.classList.toggle('on',on);btn.setAttribute('aria-pressed',String(on));}}
    function save(){try{sessionStorage.setItem('dkSnd',on?'1':'0');}catch(e){}}
    // à appeler pendant un geste ; door = true : depuis la porte (le fondu du fichier fait arriver la musique avec le logo)
    function start(door){on=true;save();ui();music();
      if(!door&&mus.currentTime<LEAD){try{mus.currentTime=LEAD;}catch(e){}}
      if(volOK)mus.volume=duckN>0?.22:1;play();ctx();
      // filet de sécurité : si le téléphone n'a toujours rien lancé, le bouton Son clignote pour la lancer d'un toucher
      clearTimeout(start.chk);start.chk=setTimeout(function(){if(on&&mus&&(mus.paused||mus.currentTime<.3)){on=false;save();ui();if(btn)btn.classList.add('nudge');}},door?6000:2500);}
    function stop(){on=false;save();ui();if(mus)mus.pause();}
    function sfx(name,delay,vol){if(!on)return;var a=ctx();if(!a)return;
      function go(b){var s=a.createBufferSource(),g=a.createGain();s.buffer=b;g.gain.value=vol||.7;s.connect(g);g.connect(a.destination);s.start(a.currentTime+Math.max(0,delay||0));}
      if(bufs[name]&&bufs[name].duration){go(bufs[name]);return;}
      if(bufs[name])return;bufs[name]=1;
      fetch('/audio/sfx/'+name+'.mp3').then(function(r){return r.arrayBuffer();}).then(function(d){return new Promise(function(ok,ko){a.decodeAudioData(d,ok,ko);});})
        .then(function(b){bufs[name]=b;}).catch(function(){delete bufs[name];});}
    function duck(d){duckN=Math.max(0,duckN+(d?1:-1));apply();}
    if(btn)btn.addEventListener('click',function(){btn.classList.remove('nudge');if(on)stop();else start(false);});
    document.addEventListener('visibilitychange',apply);
    return {start:start,stop:stop,sfx:sfx,duck:duck,warm:function(){music();try{mus.load();}catch(e){}},
      resume:function(){if(on){music();retry();ui();}}};
  })();
  // voix des gardiens et des mini-boss (fichiers du jeu, en français)
  (function(){var cur=null,curB=null;
    function end(){if(curB){curB.classList.remove('play');var c=curB.closest('.gtxt');c.querySelectorAll('.gq').forEach(function(q){q.classList.remove('say');});
      var mq=c.querySelector('.mq'),gq=c.querySelector('.gq:not(.mq)');if(mq){mq.hidden=true;gq.hidden=false;}}
      if(cur){cur.pause();cur=null;DKA.duck(false);}curB=null;}
    [].forEach.call(document.querySelectorAll('.gvoice'),function(b){b.addEventListener('click',function(){
      var same=curB===b;end();if(same)return;
      var c=b.closest('.gtxt'),mq=c.querySelector('.mq'),gq=c.querySelector('.gq:not(.mq)'),mini=b.classList.contains('alt');
      if(mq){mq.hidden=!mini;gq.hidden=mini;(mini?mq:gq).classList.add('say');}
      cur=new Audio('/audio/voice/'+I18.lang()+'/'+b.dataset.v+'.mp3');curB=b;b.classList.add('play');DKA.duck(true);
      cur.addEventListener('ended',end);cur.addEventListener('error',end);var p=cur.play();if(p&&p.catch)p.catch(end);});});
  })();
  // sorts filmés dans le jeu : [fichier, nom, école, couleur]
  var SPELLS=[
    [['knight-s8','Jugement dernier','Sacré','#ffe28a'],['knight-w4','Lames tournoyantes','Guerre','#ff8a6a'],['knight-t4','Séisme','Terre','#d9b27a']],
    [['archer-n8','Colère de Gaïa','Nature','#8fe39a'],['archer-v7','Ouragan','Vent','#a8e8ff'],['archer-o7','Fléau','Ombre','#c4a8ff']],
    [['mage-f6','Phénix','Feu','#ff9a4a'],['mage-g5','Blizzard','Glace','#8fdcff'],['mage-l8','Dieu de l’orage','Foudre','#ffe14a']],
    [['samurai-b8','Mille coupes','Lame','#f2f5fb'],['samurai-k7','Ki rebondissant','Ki','#8ff0d8'],['samurai-y6','Danse des cerisiers','Sakura','#ffb3d4']]
  ];
  var vid=document.getElementById('spVid'),spPick=document.getElementById('spPick'),spBar=document.getElementById('spBar'),
      spWrap=document.querySelector('.spells'),cap=document.querySelector('.stage .cap'),hero=0,cur=0;
  function spell(j,user){
    cur=j;var s=SPELLS[hero][j];
    spWrap.style.setProperty('--sc',s[3]);
    document.getElementById('spName').textContent=T(s[1]);document.getElementById('spSch').textContent=T(s[2]);
    cap.classList.remove('swap');void cap.offsetWidth;cap.classList.add('swap');
    [].forEach.call(spPick.children,function(b,k){b.classList.toggle('on',k===j)});
    vid.poster='/vid/'+s[0]+'.jpg';vid.src='/vid/'+s[0]+'.mp4';spBar.style.width='0';
    if(!reduce||user){var pr=vid.play();if(pr&&pr.catch)pr.catch(function(){});}
  }
  function renderSpells(){
    spPick.innerHTML='';
    SPELLS[hero].forEach(function(s,j){
      var b=document.createElement('button');b.type='button';b.style.setProperty('--sc',s[3]);
      b.innerHTML='<img src="/vid/'+s[0]+'.jpg" alt="" loading="lazy"><span><small>'+T(s[2])+'</small>'+T(s[1])+'</span>';
      b.addEventListener('click',function(){spell(j,true)});spPick.appendChild(b);
    });
    spell(0);
  }
  vid.addEventListener('timeupdate',function(){if(vid.duration)spBar.style.width=(vid.currentTime/vid.duration*100)+'%';});
  var SFX={'Sacré':'sp_holy','Guerre':'sp_war','Terre':'sp_earth','Nature':'sp_leaf','Vent':'sp_wind','Ombre':'sp_shadow','Feu':'sp_fire','Glace':'sp_ice','Foudre':'sp_thunder','Lame':'sp_blade','Ki':'sp_ki','Sakura':'sp_petal'};
  vid.addEventListener('playing',function(){var s=SPELLS[hero][cur];if(vid.currentTime<.15&&s)DKA.sfx(SFX[s[2]],.22-vid.currentTime,.75);});
  vid.addEventListener('ended',function(){spell((cur+1)%3);});
  // ne lancer les vidéos que lorsqu'elles sont visibles
  if('IntersectionObserver' in window){
    new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){if(!reduce){var p=vid.play();if(p&&p.catch)p.catch(function(){});}}else vid.pause();});},{threshold:.25}).observe(vid);
  }

  var tabs=[].slice.call(document.querySelectorAll('.tab'));
  function pick(i){
    tabs.forEach(function(t,k){t.classList.toggle('on',k===i)});
    hero=i;renderSpells();
    heroText(i);
    var hp=document.getElementById('hPortrait');hp.src=I18.img(H[i].img);hp.dataset.src0=H[i].img;var hn=document.getElementById('hName');if(hn)hp.alt=hn.textContent;
    if(!reduce&&pick.ready){hp.classList.remove('pop');void hp.offsetWidth;hp.classList.add('pop');}
    pick.ready=true;
  }
  function heroText(i){
    document.getElementById('hName').textContent=T(H[i].n);
    document.getElementById('hDesc').textContent=T(H[i].d);
    document.getElementById('hChips').innerHTML=H[i].c.map(function(x){return '<span class="chip">'+T(x)+'</span>'}).join('');
  }
  // changement de langue : textes du héros et des sorts sans relancer la vidéo
  I18.on(function(){heroText(hero);var s=SPELLS[hero][cur];document.getElementById('spName').textContent=T(s[1]);document.getElementById('spSch').textContent=T(s[2]);
    [].forEach.call(spPick.children,function(b,j){var x=SPELLS[hero][j];b.querySelector('span').innerHTML='<small>'+T(x[2])+'</small>'+T(x[1]);});});
  tabs.forEach(function(t){t.addEventListener('click',function(){pick(+t.dataset.h)})});
  pick(0);


  // campement : changer de terrain
  (function(){var img=document.getElementById('campImg');if(!img)return;var bs=[].slice.call(document.querySelectorAll('.cthemes button'));
    bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.classList.toggle('on',x===b)});img.classList.add('fade');
      var p='/img/camp/camp-'+b.dataset.t+'.webp',n=new Image();n.onload=function(){img.dataset.src0=p;img.src=n.src;img.dataset.alt0='Le campement entièrement construit, sur '+b.dataset.l;img.alt=T(img.dataset.alt0);img.classList.remove('fade');};n.src=I18.img(p);});});
    // précharger les autres terrains quand la section approche
    if('IntersectionObserver' in window){var io=new IntersectionObserver(function(e){if(e[0].isIntersecting){bs.forEach(function(b){new Image().src=I18.img('/img/camp/camp-'+b.dataset.t+'.webp');});io.disconnect();}},{rootMargin:'400px'});io.observe(img);}
  })();
  I18.on(function(){var im=document.getElementById('campImg');if(im&&im.dataset.alt0)im.alt=T(im.dataset.alt0);});
  // minuteurs
  var raid=2*3600+59*60+59,rt=document.getElementById('raidTimer');
  var arena=90,at=document.getElementById('arenaTimer'),ab=document.getElementById('arenaBar');
  function fmt(s){var h=Math.floor(s/3600),m=Math.floor(s%3600/60),x=s%60;return (h?h+':':'')+(h?String(m).padStart(2,'0'):m)+':'+String(x).padStart(2,'0')}
  setInterval(function(){
    raid=raid>0?raid-1:3*3600;rt.firstChild.nodeValue=fmt(raid);
    arena=arena>0?arena-1:90;at.firstChild.nodeValue=fmt(arena);ab.style.width=(100-arena/90*100)+'%';
  },1000);

  // apparitions au défilement
  var els=[].slice.call(document.querySelectorAll('.rv'));
  if(!reduce&&'IntersectionObserver' in window){
    els.forEach(function(e){var r=e.getBoundingClientRect();if(r.top>innerHeight)e.classList.add('pre');});
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.remove('pre');io.unobserve(x.target);}})},{threshold:.12});
    els.forEach(function(e){io.observe(e)});
  }

  // poussière magique
  var c=document.getElementById('dust'),ctx=c.getContext('2d'),P=[],W,H2;
  var ddpr=Math.min(matchMedia('(hover:none)').matches?1.5:2,devicePixelRatio||1),dW=0,dH=0,dustOn=true;
  function size(){var w=c.offsetWidth,h=c.offsetHeight;if(w===dW&&Math.abs(h-dH)<160)return;dW=w;dH=h;W=c.width=Math.round(w*ddpr);H2=c.height=Math.round(h*ddpr);}
  size();addEventListener('resize',size);
  if('IntersectionObserver' in window)new IntersectionObserver(function(en){var was=dustOn;dustOn=en[0].isIntersecting;document.querySelector('.hero').classList.toggle('off',!dustOn);if(dustOn&&!was)startDust();}).observe(c);
  var dRun=false;function startDust(){if(!dRun&&!reduce&&dustOn&&!document.hidden){dRun=true;requestAnimationFrame(tick);}}
  function spawn(){return{x:Math.random()*W,y:H2+10,r:(.8+Math.random()*1.8)*ddpr,v:(.15+Math.random()*.4)*ddpr,d:(Math.random()-.5)*.3,a:.3+Math.random()*.6,g:Math.random()<.3};}
  for(var i=0;i<70;i++){var p=spawn();p.y=Math.random()*H2;P.push(p);}
  function tick(){
    ctx.clearRect(0,0,W,H2);
    for(var i=0;i<P.length;i++){var p=P[i];
      ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,6.28);
      ctx.fillStyle=p.g?'rgba(240,196,90,'+p.a+')':'rgba(200,190,255,'+p.a+')';ctx.fill();
      p.y-=p.v;p.x+=p.d;p.a-=.001;
      if(p.y<-10||p.a<=0)P[i]=spawn();
    }
    if(!reduce&&dustOn&&!document.hidden)requestAnimationFrame(tick);else dRun=false;
  }
  dRun=true;tick();
  document.addEventListener('visibilitychange',startDust);

  // cinématique d'ouverture : une fois par visite (bouton « Voir la cinématique » pour la revoir)
  var done=[];function introDone(){var f=done;done=null;if(f)f.forEach(function(fn){fn()});}
  function afterIntro(fn){if(done)done.push(fn);else fn();}
  function playIntro(){
    var r=innerWidth/innerHeight,k=r<.52?'tall':(r<1?'portrait':'landscape');var sfx=I18.lang()==='fr'?'':'-'+I18.lang();
    var o=document.createElement('div');o.id='intro';o.setAttribute('role','dialog');o.setAttribute('aria-label',T('Cinématique Door Knight'));
    o.innerHTML='<video playsinline muted autoplay preload="auto" poster="/vid/intro-'+k+sfx+'.jpg" src="/vid/intro-'+k+sfx+'.mp4"></video>'+
      '<button class="ib skip" type="button">'+T('Passer')+' <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m6 6 6 6-6 6M13 6l6 6-6 6"/></svg></button>'+
      '<button class="ib snd" type="button" aria-pressed="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H3v6h3l5 4z"/><path class="w" d="M16 9a4 4 0 0 1 0 6M19 6a8 8 0 0 1 0 12"/></svg><span>'+T('Activer le son')+'</span></button>'+
      '<div class="start"><button class="btn" type="button">'+T('Lancer la cinématique')+'</button><button class="ib" type="button" style="position:static">'+T('Entrer sur le site')+'</button></div>'+
      '<div class="ibar"></div>';
    document.body.appendChild(o);document.body.classList.add('intro-on');
    var v=o.querySelector('video'),bar=o.querySelector('.ibar'),snd=o.querySelector('.snd'),closed=false;DKA.duck(true);
    function close(){if(closed)return;closed=true;v.pause();DKA.duck(false);o.classList.add('out');document.body.classList.remove('intro-on');
      setTimeout(function(){o.remove();},750);introDone();}
    function go(){o.classList.remove('blocked');var pr=v.play();if(pr&&pr.catch)pr.catch(function(){o.classList.add('blocked');});}
    o.querySelector('.skip').addEventListener('click',close);
    o.querySelector('.start .btn').addEventListener('click',go);
    o.querySelector('.start .ib').addEventListener('click',close);
    snd.addEventListener('click',function(){v.muted=!v.muted;snd.classList.toggle('on',!v.muted);snd.setAttribute('aria-pressed',String(!v.muted));
      snd.querySelector('span').textContent=T(v.muted?'Activer le son':'Son activé');if(v.paused)go();});
    v.addEventListener('timeupdate',function(){if(v.duration)bar.style.width=(v.currentTime/v.duration*100)+'%';});
    v.addEventListener('ended',function(){setTimeout(close,500);});
    v.addEventListener('click',function(){if(v.duration&&v.currentTime>v.duration-4)close();});
    v.addEventListener('error',close);
    addEventListener('keydown',function esc(e){if(e.key==='Escape'){close();removeEventListener('keydown',esc);}});
    go();
    // si la vidéo ne démarre pas (mode économie d'énergie), proposer de la lancer
    setTimeout(function(){if(!closed&&v.paused&&v.currentTime===0)o.classList.add('blocked');},1800);
  }
  // ouverture : la grande porte qui s'ouvre sur le logo (une fois par visite)
  function playPortal(){
    var o=document.createElement('div');o.id='portal';o.setAttribute('aria-hidden','true');
    var studs='';for(var i=0;i<=12;i++){var a=Math.PI*(1-i/12),x=50+46*Math.cos(a),y=52-46*Math.sin(a);
      studs+='<path class="rune" style="--d:'+(0.55+i*0.07).toFixed(2)+'s;transform-box:fill-box;transform-origin:center" d="M'+x.toFixed(1)+' '+(y-2.2).toFixed(1)+'l1.6 2.2-1.6 2.2-1.6-2.2z" fill="#ffe7a0"/>';}
    for(var j=0;j<4;j++){var yy=62+j*20;studs+='<path class="rune" style="--d:'+(1.0+j*0.06).toFixed(2)+'s" d="M4 '+yy+'l1.6 2.2-1.6 2.2-1.6-2.2zM96 '+yy+'l1.6 2.2-1.6 2.2-1.6-2.2z" fill="#ffe7a0"/>';}
    o.innerHTML='<canvas></canvas><div class="pw"><div class="rays"></div><div class="shk"><div class="pstage">'+
      '<div class="light"></div><div class="seam"></div>'+
      '<div class="leaf l"><i></i><i></i><b></b></div><div class="leaf r"><i></i><i></i><b></b></div>'+
      '<svg class="frame" viewBox="0 0 100 145"><defs><linearGradient id="pg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff4cf"/><stop offset=".5" stop-color="#f0c45a"/><stop offset="1" stop-color="#7a4c12"/></linearGradient>'+
      '<radialGradient id="pj" cx=".35" cy=".3" r=".7"><stop offset="0" stop-color="#fff"/><stop offset=".35" stop-color="#c7b8ff"/><stop offset="1" stop-color="#5a3ab8"/></radialGradient>'+
      '<filter id="pglow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.4"/></filter></defs>'+
      '<path d="M2 145V52A48 48 0 0 1 98 52V145" fill="none" stroke="#211a3a" stroke-width="9"/>'+
      '<path d="M7 145V52A43 43 0 0 1 93 52V145" fill="none" stroke="url(#pg)" stroke-width="3.2"/>'+
      '<path class="trace" d="M7 145V52A43 43 0 0 1 93 52V145" fill="none" stroke="#fff6d2" stroke-width="2.4" filter="url(#pglow)"/>'+
      studs+
      '<rect x="0" y="141" width="100" height="5" rx="1.5" fill="url(#pg)" stroke="#120a20" stroke-width=".6"/>'+
      '<path class="gem" d="M50 0l6 7.5-6 7.5-6-7.5z" fill="url(#pj)" stroke="#120a20" stroke-width=".8"/></svg>'+
      '</div></div><div class="flash"></div><div class="wave"></div><div class="wave w2"></div><div class="plogo"></div></div>'+
      '<div class="prompt"><b>'+I18.T(matchMedia('(hover:hover)').matches?'Clique sur la porte pour entrer':'Touche la porte pour entrer')+'</b>'+
      '</div>'+
      '<button class="pskip" type="button">'+I18.T('Passer')+'</button>';
    var src=document.querySelector('.logo svg');if(src)o.querySelector('.plogo').appendChild(src.cloneNode(true));
    document.body.appendChild(o);document.body.classList.add('intro-on');try{DKA.warm();}catch(e){}
    // particules : braises qui montent, puis explosion de lumière à l'ouverture
    var c=o.querySelector('canvas'),x=c.getContext('2d'),dpr=Math.min(2,devicePixelRatio||1),Wc,Hc,parts=[],alive=true;
    function rs(){Wc=c.width=innerWidth*dpr;Hc=c.height=innerHeight*dpr;}rs();
    function ember(){return{x:Math.random()*Wc,y:Hc+10,vx:(Math.random()-.5)*.4*dpr,vy:-(0.6+Math.random()*1.4)*dpr,r:(1+Math.random()*2)*dpr,l:1,dl:.003+Math.random()*.004,g:Math.random()<.75}}
    for(var k=0;k<60;k++){var e=ember();e.y=Math.random()*Hc;parts.push(e);}
    function burst(){var cx=Wc/2,cy=Hc*.52;for(var k=0;k<220;k++){var a=Math.random()*6.283,v=(3+Math.random()*13)*dpr;
      parts.push({x:cx,y:cy,vx:Math.cos(a)*v,vy:Math.sin(a)*v,r:(1.2+Math.random()*2.8)*dpr,l:1,dl:.008+Math.random()*.012,g:Math.random()<.8,drag:.965});}}
    (function loop(){if(!alive)return;x.clearRect(0,0,Wc,Hc);x.globalCompositeOperation='lighter';
      for(var k=parts.length-1;k>=0;k--){var p=parts[k];p.x+=p.vx;p.y+=p.vy;if(p.drag){p.vx*=p.drag;p.vy*=p.drag;}p.l-=p.dl;
        if(p.l<=0||p.y<-20){if(!p.drag&&parts.length<400){parts[k]=ember();}else parts.splice(k,1);continue;}
        x.globalAlpha=Math.max(0,p.l);x.fillStyle=p.g?'#ffcf6a':'#b9a8ff';x.beginPath();x.arc(p.x,p.y,p.r,0,6.283);x.fill();}
      x.globalAlpha=1;requestAnimationFrame(loop);})();
    var T=[],ended=false,started=false,snd=null;function at(ms,fn){T.push(setTimeout(fn,ms));}
    function finish(skip){if(ended)return;ended=true;T.forEach(clearTimeout);o.classList.add('s-go','s-open','s-logo','s-fly');
      if(snd){if(skip)snd.stop();else setTimeout(snd.stop,1800);}document.body.classList.remove('intro-on');introDone();setTimeout(function(){alive=false;o.remove();},1100);}
    function start(){if(started||ended)return;started=true;
      try{DKA.start(true);}catch(e){}
      try{var AC=window.AudioContext||window.webkitAudioContext;if(AC){var ac=new AC();if(ac.resume)ac.resume();snd=epicSound(ac);}}catch(e){}
      o.classList.add('s-go');
      at(1100,function(){o.classList.add('s-leak','s-shake');});
      at(1750,function(){o.classList.remove('s-shake');o.classList.add('s-open');burst();});
      at(2250,function(){o.classList.add('s-logo');});
      at(3900,finish);}
    o.querySelector('.pskip').addEventListener('click',function(e){e.stopPropagation();if(!started){try{DKA.start(false);}catch(_){}}finish(true);});
    o.addEventListener('click',function(){if(!started)start();});
    addEventListener('keydown',function key(ev){if(ended){removeEventListener('keydown',key);return;}
      if(ev.key==='Escape')finish(true);else if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();start();}});
  }

  // son épique de l'ouverture, composé en Web Audio (se cale sur l'animation, t = 0 au toucher)
  function epicSound(ac,offline){
    var t0=ac.currentTime+(offline?0:.03),out=ac.createGain(),comp=ac.createDynamicsCompressor();
    comp.threshold.value=-14;comp.ratio.value=4;comp.attack.value=.004;comp.release.value=.25;
    out.gain.value=.44;var lim=ac.createDynamicsCompressor();lim.threshold.value=-3;lim.ratio.value=20;lim.attack.value=.001;lim.release.value=.1;out.connect(comp);comp.connect(lim);lim.connect(ac.destination);
    // réverbération de cathédrale
    var rv=ac.createConvolver(),len=ac.sampleRate*2.8,ir=ac.createBuffer(2,len,ac.sampleRate);
    for(var c=0;c<2;c++){var d=ir.getChannelData(c);for(var i=0;i<len;i++)d[i]=(Math.random()*2-1)*Math.pow(1-i/len,3.2);}
    rv.buffer=ir;var wet=ac.createGain();wet.gain.value=.38;rv.connect(wet);wet.connect(out);
    var noiseBuf=ac.createBuffer(1,ac.sampleRate*2,ac.sampleRate),nd=noiseBuf.getChannelData(0);for(var n=0;n<nd.length;n++)nd[n]=Math.random()*2-1;
    function bus(g,dry,send){var a=ac.createGain();a.gain.value=g;var b=ac.createGain();b.gain.value=dry;a.connect(b);b.connect(out);if(send){var s2=ac.createGain();s2.gain.value=send;a.connect(s2);s2.connect(rv);}return a;}
    function env(g,t,a,peak,hold,rel){g.gain.setValueAtTime(0.0001,t);g.gain.exponentialRampToValueAtTime(peak,t+a);g.gain.setValueAtTime(peak,t+a+hold);g.gain.exponentialRampToValueAtTime(0.0001,t+a+hold+rel);}
    function osc(type,f,t,a,peak,hold,rel,dst,f2,ft){var o2=ac.createOscillator(),g=ac.createGain();o2.type=type;o2.frequency.setValueAtTime(f,t);
      if(f2)o2.frequency.exponentialRampToValueAtTime(f2,t+(ft||a+hold+rel));env(g,t,a,peak,hold,rel);o2.connect(g);g.connect(dst);o2.start(t);o2.stop(t+a+hold+rel+.05);return o2;}
    function noise(t,dur,type,f,q,peak,a,rel,dst,f2){var s3=ac.createBufferSource(),fl=ac.createBiquadFilter(),g=ac.createGain();s3.buffer=noiseBuf;s3.loop=true;
      fl.type=type;fl.frequency.setValueAtTime(f,t);if(f2)fl.frequency.exponentialRampToValueAtTime(f2,t+dur);fl.Q.value=q;env(g,t,a,peak,Math.max(0,dur-a-rel),rel);
      s3.connect(fl);fl.connect(g);g.connect(dst);s3.start(t);s3.stop(t+dur+.1);}
    var fx=bus(1,1,.5),low=bus(1,1,.15),pad=bus(1,.8,.9);
    // 1. grondement sourd qui monte
    noise(t0,2.1,'lowpass',90,.7,.55,1.2,.5,low,180);
    osc('sine',38,t0,1.3,.5,.3,.5,low,52);
    // 2. carillons des runes (gamme de ré mineur qui monte)
    var notes=[587,659,698,880,988,1047,1175,1319,1397,1760];
    notes.forEach(function(f,i){var t=t0+.15+i*.075;osc('triangle',f,t,.004,.16,.02,.7,fx);osc('sine',f*2,t,.004,.05,.0,.5,fx);});
    // 3. la gemme s'embrase
    [1319,1976,2637,3520].forEach(function(f,i){osc('sine',f,t0+.85+i*.02,.03,.07,.25,1.1,fx);});
    // 4. la porte tremble : souffle qui monte + craquement du bois
    noise(t0+1.05,.75,'bandpass',300,1.2,.28,.6,.1,fx,2400);
    var cr=ac.createOscillator(),crf=ac.createBiquadFilter(),crg=ac.createGain(),lfo=ac.createOscillator(),lg=ac.createGain();
    cr.type='sawtooth';cr.frequency.setValueAtTime(70,t0+1.1);cr.frequency.linearRampToValueAtTime(140,t0+1.75);lfo.frequency.value=23;lg.gain.value=25;lfo.connect(lg);lg.connect(cr.frequency);
    crf.type='bandpass';crf.frequency.value=900;crf.Q.value=3;env(crg,t0+1.1,.1,.18,.45,.12);cr.connect(crf);crf.connect(crg);crg.connect(fx);cr.start(t0+1.1);lfo.start(t0+1.1);cr.stop(t0+1.9);lfo.stop(t0+1.9);
    // 5. ouverture : impact + timbales
    var T1=t0+1.75;
    noise(T1,.9,'lowpass',2600,.5,.9,.005,.85,fx,180);
    osc('sine',95,T1,.004,1,.05,1.2,low,32,1.1);
    [0,.25,.5].forEach(function(dt,i){var t=T1+dt;osc('sine',[73,82,73][i],t,.003,.75,.02,.6,low,[48,55,48][i],.5);noise(t,.18,'lowpass',900,.7,.35,.002,.16,low);});
    // 6. chœur et cuivres (ré mineur puis ré majeur héroïque à l'apparition du logo)
    function choir(freqs,t,dur,peak){freqs.forEach(function(f){[-7,0,7].forEach(function(dt){var o3=ac.createOscillator(),g=ac.createGain();o3.type='sawtooth';o3.frequency.value=f;o3.detune.value=dt;
      env(g,t,.35,peak,dur-.35-.9,.9);[[800,6],[1150,7],[2900,9]].forEach(function(fq){var bp=ac.createBiquadFilter();bp.type='bandpass';bp.frequency.value=fq[0];bp.Q.value=fq[1];o3.connect(bp);bp.connect(g);});
      g.connect(pad);o3.start(t);o3.stop(t+dur+.1);});});}
    function brass(freqs,t,dur,peak){freqs.forEach(function(f){var o4=ac.createOscillator(),lp=ac.createBiquadFilter(),g=ac.createGain();o4.type='sawtooth';o4.frequency.value=f;
      lp.type='lowpass';lp.Q.value=2;lp.frequency.setValueAtTime(300,t);lp.frequency.exponentialRampToValueAtTime(2600,t+.25);lp.frequency.exponentialRampToValueAtTime(900,t+dur);
      env(g,t,.06,peak,dur-.06-.7,.7);o4.connect(lp);lp.connect(g);g.connect(pad);o4.start(t);o4.stop(t+dur+.1);});}
    choir([146.8,220,293.7,349.2],T1+.02,1.2,.06);
    brass([73.4,146.8,220],T1,1.0,.07);
    var T2=t0+2.25;
    choir([146.8,220,293.7,370,440,587.3],T2,2.1,.12);
    brass([73.4,146.8,185,220,293.7],T2,2.0,.13);
    osc('sine',73.4,T2,.004,.8,.05,1.3,low,46,1.2);noise(T2,.25,'lowpass',1200,.7,.45,.002,.22,low);
    [2637,3136,3520,4186].forEach(function(f,i){osc('sine',f,T2+.05+i*.06,.01,.04,.1,1.4,fx);});
    return {stop:function(){try{var now=ac.currentTime;out.gain.cancelScheduledValues(now);out.gain.setValueAtTime(out.gain.value,now);out.gain.linearRampToValueAtTime(0,now+.6);
      setTimeout(function(){try{ac.close&&ac.close();}catch(e){}},900);}catch(e){}}};
  }
  // la porte s'affiche à chaque arrivée ; en revenant des pages légales du site, on entre directement
  // la porte ne se rejoue pas : ni après un rechargement (l'iPhone recharge parfois l'onglet en plein défilement), ni au retour arrière, ni une 2e fois dans le même onglet
  var seen=false;try{var ref=document.referrer||'';var nav=(performance.getEntriesByType&&performance.getEntriesByType('navigation')[0]||{}).type||'';
    seen=(ref.indexOf(location.origin)===0&&/(mentions-legales|politique-confidentialite)/.test(ref))||/^(reload|back_forward)$/.test(nav)||/^(skip|seen)$/.test(sessionStorage.getItem('dkPortal')||'');}catch(e){}
  if(!seen){try{sessionStorage.setItem('dkPortal','seen');}catch(e){}}
  if(seen)DKA.resume();
  if(!reduce&&!seen)playPortal();else introDone();
  var rp=document.getElementById('replayIntro');
  if(rp)rp.addEventListener('click',function(){if(!document.getElementById('intro')){done=[];playIntro();}});

  // compteurs qui défilent
  if(!reduce){
    [].slice.call(document.querySelectorAll('.counter b:not(.inf)')).forEach(function(b,k){
      var to=+b.textContent,t0=null;b.textContent='0';
      function step(ts){if(!t0)t0=ts;var q=Math.min(1,(ts-t0)/(1100+k*250));b.textContent=Math.round(to*(1-Math.pow(1-q,3)));if(q<1)requestAnimationFrame(step);}
      afterIntro(function(){setTimeout(function(){requestAnimationFrame(step);},500);});
    });
  }

  // frise des mondes : flèches et rail de progression (porte 1 → 100)
  (function(){
    var co=document.getElementById('corridor');if(!co)return;
    var pv=co.parentNode.querySelector('.carr.prev'),nx=co.parentNode.querySelector('.carr.next'),bar=document.getElementById('railBar');
    function upd(){var m=co.scrollWidth-co.clientWidth;var q=m>0?co.scrollLeft/m:0;if(bar){var w=Math.max(10,co.clientWidth/co.scrollWidth*100);bar.style.width=w+'%';bar.style.transform='translateX('+(q*(100-w)/w*100)+'%)';}
      if(pv)pv.disabled=co.scrollLeft<8;if(nx)nx.disabled=co.scrollLeft>m-8;}
    function go(d){co.scrollBy({left:d*(co.clientWidth*.8),behavior:'smooth'});}
    if(pv)pv.addEventListener('click',function(){go(-1);});if(nx)nx.addEventListener('click',function(){go(1);});
    co.addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd();
  })();

  // barre de progression
  var root=document.documentElement;
  function prog(){var m=root.scrollHeight-innerHeight;root.style.setProperty('--prog',m>0?Math.min(1,scrollY/m):0);}
  addEventListener('scroll',prog,{passive:true});prog();

  // cartes qui s'inclinent sous la souris
  if(!reduce&&matchMedia('(hover:hover)').matches){
    [].slice.call(document.querySelectorAll('.world,.boss,.stage')).forEach(function(el){
      el.addEventListener('pointermove',function(e){var r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
        el.style.transform='perspective(700px) rotateY('+(x*10)+'deg) rotateX('+(-y*10)+'deg) translateY(-4px)';});
      el.addEventListener('pointerleave',function(){el.style.transform='';});
    });
  }

  // étincelles au toucher
  if(!reduce){
    var sc=document.createElement('canvas');sc.id='sparks';sc.setAttribute('aria-hidden','true');document.body.appendChild(sc);
    var sx=sc.getContext('2d'),S=[],run=false,dpr=Math.min(2,devicePixelRatio||1);
    var sw=0;function ss(){if(innerWidth===sw&&sc.height>=innerHeight*dpr)return;sw=innerWidth;sc.width=innerWidth*dpr;sc.height=Math.max(innerHeight,screen.height||0)*dpr;}ss();addEventListener('resize',ss);
    function frame(){
      sx.clearRect(0,0,sc.width,sc.height);
      for(var i=S.length-1;i>=0;i--){var q=S[i];q.x+=q.vx;q.y+=q.vy;q.vy+=.12*dpr;q.l-=1;
        if(q.l<=0){S.splice(i,1);continue;}
        var a=q.l/q.m;sx.save();sx.translate(q.x,q.y);sx.rotate(q.r+=.15);sx.globalAlpha=a;sx.fillStyle=q.c;
        var z=q.s*(.5+a/2);sx.beginPath();sx.moveTo(0,-z);sx.lineTo(z*.3,-z*.3);sx.lineTo(z,0);sx.lineTo(z*.3,z*.3);sx.lineTo(0,z);sx.lineTo(-z*.3,z*.3);sx.lineTo(-z,0);sx.lineTo(-z*.3,-z*.3);sx.closePath();sx.fill();sx.restore();}
      if(S.length)requestAnimationFrame(frame);else run=false;
    }
    addEventListener('pointerdown',function(e){
      for(var i=0;i<16;i++){var an=Math.random()*6.28,v=(2+Math.random()*4)*dpr,m=30+Math.random()*25;
        S.push({x:e.clientX*dpr,y:e.clientY*dpr,vx:Math.cos(an)*v,vy:Math.sin(an)*v-2*dpr,l:m,m:m,r:Math.random()*6,s:(3+Math.random()*4)*dpr,c:Math.random()<.7?'#f0c45a':'#b9a8ff'});}
      if(!run){run=true;requestAnimationFrame(frame);}
    },{passive:true});
  }
})();
