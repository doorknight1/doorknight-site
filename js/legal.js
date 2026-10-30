// Pages légales, guides, 404 : anti-cadre (clickjacking) + mémorisation de la langue choisie.
(function(){
  // la page refuse d'être affichée dans un cadre d'un autre site
  try{if(window.top!==window.self){window.top.location=window.self.location;}}catch(e){document.documentElement.style.display='none';}
  document.querySelectorAll('.langs a').forEach(function(a){a.addEventListener('click',function(){try{localStorage.setItem('dkLang',a.dataset.l)}catch(e){}})});
})();
