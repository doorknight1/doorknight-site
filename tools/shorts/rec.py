# usage: rec.py out_dir W H DPR L cls seconds [warm]
from playwright.sync_api import sync_playwright
import time,sys,os
out,W,H,DPR,L,cls,secs=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),float(sys.argv[4]),int(sys.argv[5]),sys.argv[6],float(sys.argv[7])
warm=float(sys.argv[8]) if len(sys.argv)>8 else 2.0
os.makedirs(out,exist_ok=True)
INIT="""
(()=>{ let vt=0; const q=[]; const _pn=performance.now.bind(performance);
 window.__virt=false;
 const rafOrig=window.requestAnimationFrame.bind(window);
 window.requestAnimationFrame=(cb)=>{ if(!window.__virt) return rafOrig(cb); q.push(cb); return q.length; };
 performance.now=()=> window.__virt ? vt : _pn();
 window.__goVirt=()=>{ vt=_pn(); window.__virt=true; };
 window.__step=(ms)=>{ vt+=ms; const cbs=q.splice(0); for(const cb of cbs){ try{cb(vt);}catch(e){console.log('err',e)} } };
})();
"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-gl=swiftshader','--enable-unsafe-swiftshader'])
    ctx=b.new_context(viewport={'width':W,'height':H},device_scale_factor=DPR,locale='en-US')
    ctx.add_init_script(INIT)
    pg=ctx.new_page()
    pg.goto('http://localhost:8765/index.html'); time.sleep(3)
    pg.evaluate("()=>{const b=document.getElementById('introSkip'); if(b) b.click();}"); time.sleep(1)
    pg.evaluate("""(a)=>window.__dkEval(`
      S.introSeen=true; S.lookSet=true; S.profile={name:'Hero'}; S.look.cls='${a.cls}'; S.look.helm='${a.helm}'; S.look.cape=2; S.look.armor=2;
      S.lvl=${a.lvl}; S.unlocked=101; for (const k in S.up) S.up[k]=${a.up}; S.music=false; S.sound=false;
      const sp=BAL.SPELLS.filter(s=>CLS_SCHOOLS['${a.cls}'].includes(s.school)).sort((x,y)=>y.tier-x.tier)[0]; if(sp){S.spell=sp.id; S.owned[sp.id]=true;}
      save(); startLevel(${a.L}); G.maxAlive=${a.ma}; if(G.total) G.total=Math.max(G.total,80);
      for (const id of ['ctrl','hud','bossBar']) { const el=document.getElementById(id); if(el) el.style.visibility='hidden'; }
      let tt=0;
      window.__cpBot=(P,G)=>{ input.atk=true; tt++;
        if (P.spinCd<=0 && tt%40===0) input.spinQ=true;
        if (P.spellCd<=0 && tt%55===0) input.spellQ=true;
        if (P.hp < P.maxHp*0.6) P.hp=P.maxHp; if (G.bossE && G.bossE.hp < G.bossE.max*0.3) G.bossE.hp=G.bossE.max*0.7;
        let best=null,bd=1e9; for(const e of G.en){const d=Math.hypot(e.x-P.x,e.y-P.y); if(d<bd){bd=d;best=e;}}
        if(!best) return {x:0,y:0}; const dx=best.x-P.x, dy=best.y-P.y, d=Math.hypot(dx,dy)||1;
        return d>70?{x:dx/d,y:dy/d}:{x:-dy/d*0.4,y:dx/d*0.4}; };
      'ok'`)""",{'L':L,'cls':cls,'lvl':int(os.environ.get('LVL','50')),'up':int(os.environ.get('UP','15')),'ma':int(os.environ.get('MA','18')),'helm':{'knight':'closed','archer':'open','mage':'winged','samurai':'horned'}.get(cls,'closed')})
    pg.add_style_tag(content='.coach{display:none!important}')
    pg.evaluate("()=>window.__goVirt()")
    for i in range(int(warm*30)): pg.evaluate("()=>window.__step(1000/30)")
    n=int(secs*30)
    for i in range(n):
        pg.evaluate("()=>window.__step(1000/30)")
        pg.screenshot(path=f'{out}/f{i:05d}.jpg',type='jpeg',quality=92)
    print(out, n, pg.evaluate("()=>window.__dkEval('[G.en.length,G.kills,state]')"))
    b.close()
