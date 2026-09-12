import sys
p=r'C:\Users\JSJ\David\AI\Projects\David\David - Projects\DAtingFun\luxder.html'
s=open(p,encoding='utf-8').read()

s=s.replace('canvas#fx{', '''.score{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:8px;text-align:center}
.score .t{font-family:var(--display);font-size:22px;letter-spacing:.06em}
.score .n{font-family:var(--display);font-size:64px;line-height:1;font-variant-numeric:tabular-nums}
.score .vs{font-family:var(--display);font-size:20px;color:var(--muted)}
.eles{color:var(--sky)} .elas{color:var(--pink)}
.timer{font-family:var(--display);font-size:clamp(70px,24vw,110px);line-height:.9;text-align:center;color:var(--lime);font-variant-numeric:tabular-nums}
.pad.go{border-color:var(--lime);background:#2a3a10;box-shadow:0 0 0 14px #c9ff3a33,0 0 80px #c9ff3a88}
.secret{filter:blur(14px);transition:filter .2s} .secret.show{filter:none}
canvas#fx{''',1)

s=s.replace('''    <p class="small">Não guardamos nada. Zero fotos. Isto morre aqui. Um "não" bem dado também conta como feedback.</p>
  </section>''','''    <div class="btns col"><button class="ghost" id="comp-start">⚔️ Modo competição: Eles vs Elas</button></div>
    <p class="small">Não guardamos nada. Zero fotos. Isto morre aqui. Um "não" bem dado também conta como feedback.</p>
  </section>''',1)
s=s.replace('<div class="btns"><button class="yes" data-go="s-duo0">Modo a dois</button><button class="ghost" data-go="s-report">Relatório</button></div>',
 '<div class="btns"><button class="yes" data-go="s-duo0">Modo a dois</button><button class="ghost" id="comp-start2">Eles vs Elas</button></div>',1)

screens='''
  <!-- ===== COMPETIÇÃO ===== -->
  <section class="screen" id="s-c0">
    <span class="tag">Modo competição · 2 vs 2</span>
    <h1>Eles vs Elas.</h1>
    <p>Um telemóvel, 3 rondas, 20 segundos cada. Quem perde cumpre castigo. Se elas perderem, podem delegar o castigo neles.</p>
    <div class="card"><p><b style="color:var(--lime)">Ronda 1</b> Reflexos: toca quando ficar verde.</p><p><b style="color:var(--lime)">Ronda 2</b> Adivinha: uma equipa responde em segredo, a outra adivinha.</p><p><b style="color:var(--lime)">Ronda 3</b> Mímica: 20 s, a outra equipa é o júri.</p></div>
    <div class="spacer"></div>
    <div class="btns col"><button class="yes" id="c-go1">Começar</button></div>
  </section>

  <section class="screen" id="s-cscore">
    <span class="tag" id="cs-tag">Placar</span>
    <div class="score"><div><div class="t eles">Eles</div><div class="n eles" id="sc-eles">0</div></div><div class="vs">VS</div><div><div class="t elas">Elas</div><div class="n elas" id="sc-elas">0</div></div></div>
    <h2 id="cs-title"></h2>
    <p class="verdict" id="cs-text"></p>
    <div class="spacer"></div>
    <div class="btns col"><button class="yes" id="cs-next">Próxima ronda</button></div>
  </section>

  <section class="screen" id="s-reflex">
    <span class="tag">Ronda 1 · Reflexos</span>
    <div class="who" id="rf-who"></div>
    <h2 id="rf-title">Toca no círculo. Espera. Quando ficar verde, toca outra vez.</h2>
    <div class="pad" id="rfpad"><div class="status" id="rf-status" style="font-size:30px">Toca para armar</div></div>
    <p class="verdict" id="rf-res" style="min-height:52px"></p>
  </section>

  <section class="screen" id="s-guess">
    <span class="tag" id="g-tag">Ronda 2 · Adivinha</span>
    <div class="who" id="g-who"></div>
    <h2 id="g-q"></h2>
    <p class="small" id="g-hint"></p>
    <div class="opts" id="g-opts"></div>
  </section>

  <section class="screen" id="s-mime">
    <span class="tag">Ronda 3 · Mímica</span>
    <div class="who" id="m-who"></div>
    <h2 id="m-title">Só quem faz a mímica pode ver. Os outros olham para o tecto.</h2>
    <div class="card" style="text-align:center"><p class="secret" id="m-word" style="font-family:var(--display);font-size:34px;letter-spacing:.04em;color:var(--sun)"></p></div>
    <div class="timer" id="m-timer" hidden>20</div>
    <div class="btns col" id="m-ctl"><button class="ghost" id="m-reveal">Mostrar palavra (3 s)</button><button class="yes" id="m-start" disabled style="opacity:.35">Começar 20 s</button></div>
    <div class="btns" id="m-judge" hidden><button class="yes" id="m-ok">Acertaram</button><button class="no" id="m-fail">Falharam</button></div>
    <p class="small" id="m-hint">A outra equipa é o júri. Sem subornos.</p>
  </section>

  <section class="screen" id="s-cfinal">
    <span class="tag lime">Resultado final</span>
    <div class="score"><div><div class="t eles">Eles</div><div class="n eles" id="fc-eles">0</div></div><div class="vs">VS</div><div><div class="t elas">Elas</div><div class="n elas" id="fc-elas">0</div></div></div>
    <h1 id="fc-title"></h1>
    <div class="card"><p id="fc-who" style="color:var(--sun)"></p><p id="fc-castigo"></p></div>
    <p class="small" id="fc-note"></p>
    <div class="spacer"></div>
    <div class="btns"><button class="ghost" id="fc-again">Outro castigo</button><button class="yes" id="fc-restart">Revanche</button></div>
    <div class="btns col"><button class="ghost" data-go="s-beta">Voltar ao início</button></div>
  </section>
'''
s=s.replace('  <!-- REPORT -->', screens+'\n  <!-- REPORT -->',1)

js='''
/* ---------- COMPETIÇÃO 2v2 ---------- */
let comp;
function compReset(){comp={eles:0,elas:0,round:0,rf:{i:0,times:{eles:[],elas:[]},armed:null,t0:0,timer:null},g:{i:0,secret:null},m:{i:0,timer:null,left:20}}}
const ORDER=[['eles','Ele 1'],['elas','Ela 1'],['eles','Ele 2'],['elas','Ela 2']];
const T=x=>x==='eles'?'Eles':'Elas';
function startComp(){compReset();go('s-c0')}
$('#comp-start').onclick=startComp;$('#comp-start2').onclick=startComp;
$('#c-go1').onclick=()=>{buzz(20);reflexPlayer()};
function showScore(title,text,next){$('#sc-eles').textContent=comp.eles;$('#sc-elas').textContent=comp.elas;$('#cs-title').textContent=title;$('#cs-text').innerHTML=text;$('#cs-next').onclick=next;$('#cs-tag').textContent='Placar · ronda '+comp.round;go('s-cscore')}

/* Ronda 1: reflexos */
const rfpad=$('#rfpad'),rfs=$('#rf-status');
function reflexPlayer(){const r=comp.rf;if(r.i>=4)return reflexEnd();const [team,name]=ORDER[r.i];
  const w=$('#rf-who');w.textContent=name+', é a tua vez';w.className='who '+team;$('#rf-res').textContent='';rfpad.className='pad';rfs.textContent='Toca para armar';r.armed=null;go('s-reflex')}
rfpad.addEventListener('pointerdown',e=>{e.preventDefault();if(!comp||!$('#s-reflex').classList.contains('on'))return;const r=comp.rf;
  if(r.armed===null){r.armed=false;rfpad.classList.add('hot');rfs.textContent='Espera…';buzz(15);
    r.timer=setTimeout(()=>{r.armed=true;rfpad.classList.remove('hot');rfpad.classList.add('go');rfs.textContent='AGORA';r.t0=performance.now();buzz(80)},1200+Math.random()*2500);return}
  const [team,name]=ORDER[r.i];let ms;
  if(r.armed===false){clearTimeout(r.timer);ms=999;$('#rf-res').innerHTML='<b style="color:var(--pink)">Falso arranque.</b> '+name+' conta 999 ms. Clássico.';buzz([30,30,30])}
  else{ms=Math.round(performance.now()-r.t0);$('#rf-res').innerHTML='<b style="color:var(--lime)">'+ms+' ms.</b> '+(ms<220?'Suspeito. Já bebeste?':ms<350?'Aceitável para as '+new Date().getHours()+'h.':'A imperial já chegou aos dedos.');buzz(40)}
  r.times[team].push(ms);r.armed='done';rfpad.className='pad';rfs.textContent='Feito';r.i++;setTimeout(reflexPlayer,1600)});
function reflexEnd(){const t=comp.rf.times,be=Math.min(...t.eles),ba=Math.min(...t.elas);comp.round=1;
  const win=be<ba?'eles':ba<be?'elas':null;if(win)comp[win]++;
  showScore(win?T(win)+' levam a ronda 1.':'Empate. Ninguém tem reflexos.','Melhor deles: <b class="eles">'+be+' ms</b> · Melhor delas: <b class="elas">'+ba+' ms</b>',()=>guessStep())}

/* Ronda 2: adivinha */
const GQ=[
 {q:'Que música vos faz ir para a pista sem vergonha?',o:['Reggaeton de 2014','Techno a 140 bpm','Remix do Tony Carreira']},
 {q:'A que horas saem do Lux esta noite, honestamente?',o:['Às 3h, como pessoas responsáveis','Às 6h, com o sol','Com o pessoal da limpeza']},
 {q:'Pior frase de engate que já ouviram aqui?',o:['"Não costumo vir cá"','"Conheço o DJ"','"Tens lume? Não fumo, mas tens?"']},
 {q:'O que fazem quando toca uma música que odeiam?',o:['Vão ao bar, estrategicamente','Dançam na mesma, sem alma','Olham para o telemóvel como se fosse urgente']},
];
const GORDER=[['elas','eles'],['eles','elas']];
function guessStep(){const g=comp.g;if(g.i>=2)return mimeStep();const [ans,gs]=GORDER[g.i],q=GQ[(g.i*2+Math.floor(Math.random()*2))%GQ.length];
  const render=(phase)=>{const team=phase==='secret'?ans:gs;const w=$('#g-who');w.textContent=phase==='secret'?T(team)+' respondem em segredo':T(team)+' adivinham';w.className='who '+team;
    $('#g-tag').textContent='Ronda 2 · '+(g.i+1)+' de 2';$('#g-q').textContent=q.q;$('#g-hint').textContent=phase==='secret'?T(gs)+', olhem para o tecto. A sério.':'O que é que '+ans+' responderam?';
    const o=$('#g-opts');o.innerHTML='';q.o.forEach((l,k)=>{const b=document.createElement('button');b.className='opt';b.innerHTML='<span>'+l+'</span>';
      b.onclick=()=>{buzz(25);if(phase==='secret'){g.secret=k;render('guess')}else{const hit=k===g.secret;if(hit)comp[gs]++;comp.round=2;g.i++;
        showScore(hit?T(gs)+' acertaram.':T(gs)+' falharam.','Resposta secreta: <b style="color:var(--sun)">'+q.o[g.secret]+'</b>. '+(hit?'Assustadoramente compatíveis.':'Ainda há muito para conhecer.'),()=>guessStep())}};o.appendChild(b)});go('s-guess')};
  render('secret')}

/* Ronda 3: mímica */
const MW=['Elétrico 28 à hora de ponta','Pastel de nata a sair do forno','Segurança do Lux às 6h','DJ que perdeu a pen','Táxi que não para no Cais do Sodré','Fila do bar sem dinheiro','Turista perdido em Alfama','Bacalhau a nadar','Sardinha na brasa','Mota de entregas contra o vento','Pessoa a fingir que atende o telemóvel na pista','Metro fechado às 2h'];
const MORDER=['eles','elas'];
function mimeStep(){const m=comp.m;if(m.i>=2)return compFinal();const team=MORDER[m.i],jury=team==='eles'?'elas':'eles';m.word=rnd(MW);m.left=20;
  const w=$('#m-who');w.textContent=T(team)+' fazem mímica · '+T(jury)+' julgam';w.className='who '+team;
  const wd=$('#m-word');wd.textContent=m.word;wd.classList.remove('show');$('#m-timer').hidden=true;$('#m-timer').textContent='20';$('#m-ctl').hidden=false;$('#m-judge').hidden=true;
  const st=$('#m-start');st.disabled=true;st.style.opacity=.35;$('#m-title').textContent='Só quem faz a mímica pode ver. Os outros olham para o tecto.';go('s-mime')}
$('#m-reveal').onclick=()=>{const wd=$('#m-word');wd.classList.add('show');buzz(20);setTimeout(()=>{wd.classList.remove('show');const st=$('#m-start');st.disabled=false;st.style.opacity=1},3000)};
$('#m-start').onclick=()=>{const m=comp.m;$('#m-ctl').hidden=true;$('#m-timer').hidden=false;$('#m-title').textContent='Sem falar. Sem apontar para coisas reais. Vai.';buzz(60);
  m.timer=setInterval(()=>{m.left--;$('#m-timer').textContent=m.left;if(m.left<=5)buzz(20);if(m.left<=0){clearInterval(m.timer);$('#m-timer').textContent='0';$('#m-title').textContent='Tempo. Júri, decidam.';$('#m-word').classList.add('show');$('#m-judge').hidden=false;buzz([80,40,80])}},1000)};
function mimeJudge(ok){const m=comp.m;clearInterval(m.timer);const team=MORDER[m.i];if(ok)comp[team]++;comp.round=3;m.i++;$('#m-judge').hidden=true;
  showScore(ok?T(team)+' acertaram a mímica.':T(team)+' falharam a mímica.','A palavra era <b style="color:var(--sun)">'+m.word+'</b>.',()=>mimeStep())}
$('#m-ok').onclick=()=>{buzz(30);mimeJudge(true)};$('#m-fail').onclick=()=>{buzz(30);mimeJudge(false)};

/* Final */
function compFinal(){$('#fc-eles').textContent=comp.eles;$('#fc-elas').textContent=comp.elas;
  const loser=comp.eles>comp.elas?'elas':comp.elas>comp.eles?'eles':null;comp.loser=loser;
  $('#fc-title').textContent=loser==='elas'?'Eles ganharam. Ninguém esperava.':loser==='eles'?'Elas ganharam. Toda a gente esperava.':'Empate. Castigo para os quatro.';
  fcCastigo();go('s-cfinal');confetti();buzz([60,40,60,40,120])}
function fcCastigo(){const l=comp.loser;const lv=l==='eles'?rnd([1,2,3]):1;const pick=rnd(C[lv]);
  $('#fc-who').textContent=l==='eles'?'Castigo para eles':l==='elas'?'Castigo para elas (ou delegam neles, direito adquirido)':'Castigo conjunto, nível leve';
  $('#fc-castigo').innerHTML='<b>'+pick[0]+'</b><br><span class="small">'+pick[1]+'</span>';
  $('#fc-note').textContent=l==='elas'?'Regra da casa: elas podem carregar em "Outro castigo" até aparecer um que eles mereçam.':'Sem recurso. O júri já foi para o bar.'}
$('#fc-again').onclick=()=>{buzz(20);fcCastigo()};$('#fc-restart').onclick=()=>{buzz(20);compReset();reflexPlayer()};
compReset();
'''
s=s.replace('/* ---------- CONFETTI ---------- */', js+'\n/* ---------- CONFETTI ---------- */',1)
open(p,'w',encoding='utf-8').write(s)
print('ok',len(s),'comp-start' in s,'s-cfinal' in s)
