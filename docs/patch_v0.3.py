import re
root=r'C:\Users\JSJ\David\AI\Projects\David\David - Projects\DAtingFun'
src=open(root+r'\luxder.html',encoding='utf-8').read()
s=src

# ---------- iOS-safe CSS ----------
s=s.replace('''  --r:22px; --bg1:#2a1440; --bg2:#0d2a3a; --shadow:0 6px 0 #00000080;
}''','''  --r:22px; --bg1:#2a1440; --bg2:#0d2a3a; --shadow:0 6px 0 #00000080;
  --aG1:rgba(255,79,163,.25); --aG2:rgba(255,79,163,.45); --bG1:rgba(201,255,58,.25); --bG2:rgba(201,255,58,.55); --bPad:#2f3a1c; --tagA:#2b1636; --tagB:#1f2a0b;
}''',1)
s=s.replace('''  --r:999px; --bg1:#3a4bff; --bg2:#0a10a0; --shadow:0 6px 0 #000;
}''','''  --r:999px; --bg1:#3a4bff; --bg2:#0a10a0; --shadow:0 6px 0 #000;
  --aG1:rgba(255,106,0,.3); --aG2:rgba(255,106,0,.5); --bG1:rgba(245,255,0,.3); --bG2:rgba(245,255,0,.6); --bPad:#3a44c0; --tagA:#2a1a00; --tagB:#2a2a00;
}''',1)
s=s.replace('*{box-sizing:border-box}','*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}\n[hidden]{display:none!important}',1)
s=s.replace('.app{max-width:440px;margin:0 auto;min-height:100vh;','.app{max-width:440px;margin:0 auto;min-height:100vh;min-height:100dvh;padding-bottom:env(safe-area-inset-bottom);',1)
s=s.replace('.pad.hot{border-color:var(--a);box-shadow:0 0 0 12px color-mix(in srgb,var(--a) 25%,transparent),0 0 60px color-mix(in srgb,var(--a) 45%,transparent)}','.pad.hot{border-color:var(--a);box-shadow:0 0 0 12px var(--aG1),0 0 60px var(--aG2)}',1)
s=s.replace('.pad.go{border-color:var(--b);background:color-mix(in srgb,var(--b) 25%,var(--card));box-shadow:0 0 0 14px color-mix(in srgb,var(--b) 25%,transparent),0 0 80px color-mix(in srgb,var(--b) 55%,transparent)}','.pad.go{border-color:var(--b);background:var(--bPad);box-shadow:0 0 0 14px var(--bG1),0 0 80px var(--bG2)}',1)
s=s.replace('touch-action:none;user-select:none;-webkit-user-select:none}','touch-action:none;user-select:none;-webkit-user-select:none;-webkit-touch-callout:none}',1)
s=s.replace('.tag{display:inline-block;background:color-mix(in srgb,var(--a) 20%,var(--ink));','.tag{display:inline-block;background:var(--tagA);',1)
s=s.replace('.tag.lime{background:color-mix(in srgb,var(--b) 15%,var(--ink));','.tag.lime{background:var(--tagB);',1)
s=s.replace('button{font-family:var(--display);','button{-webkit-appearance:none;appearance:none;touch-action:manipulation;font-family:var(--display);',1)
s=s.replace('.dare{}','')
s=s.replace('canvas#fx{','.daretxt{font-family:var(--display);font-size:clamp(28px,8vw,40px);line-height:1.05;letter-spacing:.03em;color:var(--d);text-align:center}\n.prize{color:var(--d);text-align:center;font-size:16px}\ncanvas#fx{',1)

# ---------- screens ----------
s=s.replace('''    <h2 id="sc-title"></h2>
    <p class="verdict" id="sc-text"></p>''','''    <h2 id="sc-title"></h2>
    <p class="verdict" id="sc-text"></p>
    <p class="prize" id="sc-prize"></p>''',1)
s=s.replace('  <section class="screen" id="s-final">','''  <section class="screen" id="s-dare">
    <span class="tag lime" data-i="d.tag"></span>
    <div class="who" id="d-who"></div>
    <div class="card"><p class="daretxt" id="d-text"></p><p class="small center" id="d-sub"></p></div>
    <div class="timer" id="d-timer">10</div>
    <div class="btns col" id="d-ctl"><button class="yes" id="d-start" data-i="d.start"></button></div>
    <div class="btns" id="d-judge" hidden><button class="yes" id="d-ok" data-i="d.ok"></button><button class="no" id="d-fail" data-i="d.fail"></button></div>
    <p class="small center" data-i="d.hint"></p>
  </section>

  <section class="screen" id="s-final">''',1)
s=s.replace('''<div class="btns"><button class="ghost" id="f-again" data-i="f.again"></button><button class="yes" id="f-rematch" data-i="f.rematch"></button></div>''','''<div class="btns"><button class="ghost" id="f-again" data-i="f.again"></button><button class="ghost" id="f-prize2" data-i="f.prize2"></button></div>
    <div class="btns col"><button class="yes" id="f-rematch" data-i="f.rematch"></button></div>''',1)

# ---------- i18n additions ----------
s=s.replace(" 'f.tag':B('Resultado final','Final result'),",""" 'd.tag':B('Ronda · Parvoíces','Round · Silly stuff'),'d.start':B('Começar 10 s','Start 10 s'),'d.ok':B('Conseguiu','Did it'),'d.fail':B('Falhou','Failed'),'d.hint':B('Os outros julgam. Vale 1 ponto. Não vale a pena discutir.','The others judge. Worth 1 point. Not worth arguing.'),
 'f.prize2':B('Outro prémio','Another prize'),
 'f.tag':B('Resultado final','Final result'),""",1)

s=s.replace(" duoTie:B('Desempate: quem chegar primeiro ao bar.','Tiebreak: first to reach the bar.'),",""" duoTie:B('Desempate: quem chegar primeiro ao bar.','Tiebreak: first to reach the bar.'),
 miniPrize:B('Prémio da ronda','Round prize'),dareTurn:B('{p}, parvoíce para ti','{p}, silly task for you'),dOk:B('{p} conseguiu. Ponto para {t}.','{p} did it. Point for {t}.'),dFail:B('{p} falhou. Com dignidade.','{p} failed. With dignity.'),
 dSub:B('10 segundos. Sem ensaio.','10 seconds. No rehearsal.'),""",1)

# richer prizes
s=re.sub(r" fPrize:\[.*?\],\n",""" fPrize:[B('Uma bicicleta. Sem travões. Como esta noite.','A bike. No brakes. Like tonight.'),B('Bicicleta tandem. Quem vai à frente decide-se no táxi.','Tandem bike. Who rides in front gets decided in the taxi.'),B('Bicicleta imaginária, mas o orgulho é real.','Imaginary bike, but the pride is real.'),B('A bicicleta será entregue às 6h, à porta do Lux. Provavelmente não.','The bike will be delivered at 6am at the Lux door. Probably not.'),
  B('Uma bicicleta e um pastel de nata amassado no bolso.','A bike and a squashed pastel de nata in a pocket.'),B('Bicicleta com cesto para os arrependimentos da noite.','A bike with a basket for tonight\\'s regrets.'),B('Bicicleta e o título honorário de Pessoa Menos Confusa do Lux.','A bike and the honorary title of Least Confused Person at Lux.'),
  B('Bicicleta com campainha. A campainha é o perdedor a dizer "trim".','A bike with a bell. The bell is the loser saying "ring".'),B('Uma bicicleta e o direito de escolher a próxima música, que ninguém vai ouvir.','A bike and the right to pick the next song, which nobody will hear.'),B('Bicicleta e um copo de água real. O mais valioso dos dois.','A bike and a real glass of water. The more valuable of the two.'),
  B('Bicicleta e a primeira ronda paga pelos perdedores. Moralmente.','A bike and the first round on the losers. Morally.'),B('Bicicleta elétrica. A bateria é a energia do perdedor.','An e-bike. The battery is the loser\\'s energy.')],
 mini:[B('um high-five sem contacto','a contactless high-five'),B('um "boa" dito com convicção','a "nice" said with conviction'),B('5 segundos de aplausos dos perdedores','5 seconds of applause from the losers'),B('o direito de escolher quem faz a próxima parvoíce','the right to pick who does the next silly task'),B('um elogio inventado na hora','an on-the-spot invented compliment'),B('uma vénia lenta dos adversários','a slow bow from the opponents'),B('um brinde com o que houver','a toast with whatever is at hand'),B('o lugar de honra no táxi (à frente)','the seat of honor in the taxi (front)'),B('uma dedicatória imaginária do DJ','an imaginary DJ shout-out'),B('nada. O prémio é a jornada.','nothing. The prize is the journey.')],
""",s,count=1,flags=re.S)

# ---------- more questions & challenges ----------
s=s.replace(" {q:B('Objeto mais estranho na tua mala ou bolso agora?',",""" {q:B('Se tivesses de tatuar uma palavra portuguesa, qual?','If you had to tattoo one Portuguese word, which?'),o:[B('Saudade, obviamente','Saudade, obviously'),B('Bifana','Bifana'),B('Desenrascanço','Desenrascanço')]},
 {q:B('O teu talento secreto mais inútil?','Your most useless secret talent?'),o:[B('Imitar o som do metro a fechar','Imitating the metro doors closing'),B('Adivinhar o final de filmes maus','Guessing the ending of bad movies'),B('Encontrar sempre o Wi-Fi mais fraco','Always finding the weakest Wi-Fi')]},
 {q:B('Primeira coisa que fazes ao chegar a casa às 6h?','First thing you do getting home at 6am?'),o:[B('Torradas com muita manteiga','Toast with too much butter'),B('Ver o ecrã do telemóvel a arrepender-me','Stare at the phone regretting'),B('Prometer que foi a última vez','Promise it was the last time')]},
 {q:B('Se fosses um bairro de Lisboa?','If you were a Lisbon neighborhood?'),o:[B('Alfama, com fado a mais','Alfama, too much fado'),B('Cais do Sodré, a fingir que não','Cais do Sodré, pretending otherwise'),B('Benfica, sinceramente','Benfica, honestly')]},
 {q:B('Qual destas mentiras já contaste esta noite?','Which of these lies have you told tonight?'),o:[B('"Só bebo mais um"','"Just one more"'),B('"Vou-me embora daqui a 10 minutos"','"Leaving in 10 minutes"'),B('"Conheço esta música"','"I know this song"')]},
 {q:B('Dança de emergência quando ninguém está a ver?','Emergency dance when nobody is watching?'),o:[B('O robot, mal feito','The robot, badly done'),B('Só ombros','Shoulders only'),B('Apontar para o tecto com convicção','Pointing at the ceiling with conviction')]},
 {q:B('Objeto mais estranho na tua mala ou bolso agora?',""",1)

s=s.replace(" B('Desafio: pose de estátua de Lisboa, o outro adivinha qual',",""" B('Mímica: pastel de nata a sair do forno','Mime: pastel de nata leaving the oven'),B('Mímica: turista perdido em Alfama com mapa de papel','Mime: tourist lost in Alfama with a paper map'),B('Mímica: gaivota a roubar uma sandes','Mime: seagull stealing a sandwich'),B('Mímica: fila do bar às 4h','Mime: bar queue at 4am'),
 B('Desafio: recitar um poema de 4 versos sobre a imperial morna','Challenge: recite a 4-line poem about warm beer'),B('Desafio: vender a bicicleta ao júri como se fosse um carro de luxo','Challenge: pitch the bike to the jury like it is a luxury car'),B('Desafio: fazer a voz de GPS a dar direções para o bar','Challenge: do a GPS voice giving directions to the bar'),
 B('Desafio: cantarolar uma música com a boca fechada, o par adivinha','Challenge: hum a song with mouth closed, partner guesses'),B('Desafio: contar uma história de 20 s em que tudo corre bem (impossível)','Challenge: tell a 20 s story where everything goes well (impossible)'),B('Desafio: imitar o segurança a recusar a entrada a um pombo','Challenge: impersonate the bouncer denying entry to a pigeon'),
 B('Desafio: pose de estátua de Lisboa, o outro adivinha qual',""",1)

# ---------- dares list + rounds engine ----------
s=s.replace("/* round 3: challenge */","""/* dares: small silly tasks for anyone (benign, no contact, no drinking) */
const DARES=[
 B('Língua no nariz. 5 segundos de tentativa séria.','Tongue to nose. 5 seconds of serious effort.'),B('Falar 10 segundos só com palavras que começam por R.','Speak 10 seconds using only words starting with R.'),B('Olhar fixamente para quem está à frente 10 s sem rir.','Stare at the person in front for 10 s without laughing.'),
 B('Alfabeto ao contrário até ao M.','Alphabet backwards down to M.'),B('Cara de foto de passaporte durante 10 s. Sem pestanejar.','Passport-photo face for 10 s. No blinking.'),B('Imitar um gato a pedir comida às 6h da manhã.','Impersonate a cat begging for food at 6am.'),
 B('Contar até 10 em alemão inventado.','Count to 10 in made-up German.'),B('Dançar só com as sobrancelhas 10 s.','Dance with eyebrows only for 10 s.'),B('Estátua que se derrete lentamente.','A statue slowly melting.'),
 B('Beber um gole do que tiveres com o mindinho no ar e cara de crítico.','Take a sip of whatever you have, pinky up, critic face.'),B('Dizer "Lux Frágil" com sotaque brasileiro, espanhol e russo.','Say "Lux Frágil" in Brazilian, Spanish and Russian accents.'),B('Aplaudir a ti próprio 10 s como o teu maior fã.','Applaud yourself for 10 s like your biggest fan.'),
 B('Vénia lenta e solene ao segurança, à distância.','Slow, solemn bow to the bouncer, from afar.'),B('Piscar o olho ao teu reflexo no telemóvel e dizer "boa".','Wink at your reflection in the phone and say "nice".'),B('5 passos em câmara lenta, com cara de filme de ação.','5 steps in slow motion, action-movie face.'),
 B('Voz de GPS: "recalculando" 3 vezes com emoção crescente.','GPS voice: "recalculating" 3 times with rising emotion.'),B('Cantarolar uma música de boca fechada. Os outros adivinham.','Hum a song with mouth closed. The others guess.'),B('Telemóvel como walkie-talkie: reportar a situação ao QG.','Phone as walkie-talkie: report the situation to HQ.'),
 B('Sorriso de anúncio de pasta de dentes durante 10 s.','Toothpaste-ad smile for 10 s.'),B('Tocar no cotovelo com a língua. É impossível. Tenta na mesma.','Touch your elbow with your tongue. Impossible. Try anyway.'),B('Fingir que apanhas um táxi que não para, 10 s.','Pretend to hail a taxi that never stops, 10 s.'),
 B('Dizer "obrigado" a um objeto por tudo o que fez por ti esta noite.','Thank an object for everything it did for you tonight.'),B('Imitar o som do metro a fechar as portas, com aviso.','Imitate the metro doors closing, with the announcement.'),B('Apresentar-te ao grupo com um nome de DJ inventado.','Introduce yourself to the group with a made-up DJ name.'),
 B('Fazer de pombo do Rossio a decidir se rouba uma batata.','Be a Rossio pigeon deciding whether to steal a fry.'),B('Andar como se o chão fosse lava, 5 passos.','Walk as if the floor is lava, 5 steps.'),
];
function dareStart(){G.d={list:G.teams.flatMap((t,ti)=>t.map(pi=>[ti,pi])).sort(()=>Math.random()-.5),i:0,used:G.d?G.d.used:[],timer:null};dareStep()}
function dareStep(){const d=G.d;if(d.i>=d.list.length)return nextRound();const [ti,pi]=d.list[d.i],p=G.players[pi];const pool=DARES.filter(x=>!d.used.includes(x));d.cur=rnd(pool.length?pool:DARES);d.used.push(d.cur);
  const w=$('#d-who');w.textContent=L(TX.dareTurn).replace('{p}',pname(p));w.className='who '+p.g;$('#d-text').textContent=L(d.cur);$('#d-sub').textContent=L(TX.dSub);
  $('#d-timer').textContent='10';$('#d-ctl').hidden=false;$('#d-judge').hidden=true;go('s-dare')}
$('#d-start').onclick=()=>{const d=G.d;let left=10;$('#d-ctl').hidden=true;buzz(60);clearInterval(d.timer);d.timer=setInterval(()=>{left--;$('#d-timer').textContent=left;if(left<=3)buzz(20);if(left<=0){clearInterval(d.timer);$('#d-judge').hidden=false;buzz([80,40,80])}},1000)};
function dareJudge(ok){const d=G.d;clearInterval(d.timer);const [ti,pi]=d.list[d.i],p=G.players[pi];if(ok)G.score[ti]++;d.i++;
  showScore(L(ok?TX.dOk:TX.dFail).replace('{p}',pname(p)).replace('{t}',tname(G.teams[ti])),'',()=>dareStep())}
$('#d-ok').onclick=()=>{buzz(30);dareJudge(true)};$('#d-fail').onclick=()=>{buzz(30);dareJudge(false)};

/* rounds engine: ~25 minutes */
const ROUNDS=['reflex','guess','dare','chal','guess','dare','chal','reflex'];
function nextRound(){if(G.ri>=ROUNDS.length)return gameFinal();const r=ROUNDS[G.ri++];G.round=G.ri;({reflex:reflexStart,guess:guessStart,chal:chalStart,dare:dareStart})[r]()}
function gameStart(){G.ri=0;G.round=0;G.d=null;nextRound()}

/* round 3: challenge */""",1)

# wire engine
s=s.replace("  G.score=G.teams.map(()=>0);G.round=0;reflexStart()};","  G.score=G.teams.map(()=>0);gameStart()};",1)
s=s.replace("$('#prs-go').onclick=()=>{buzz(20);reflexStart()};","$('#prs-go').onclick=()=>{buzz(20);gameStart()};",1)
s=s.replace("G.round=1;\n  showScore(winnerText(win),G.teams.map((t,i)=>`${tname(t)}: <b>${best[i]} ms</b>`).join('<br>'),()=>guessStart())}","\n  showScore(winnerText(win),G.teams.map((t,i)=>`${tname(t)}: <b>${best[i]} ms</b>`).join('<br>'),()=>nextRound())}",1)
s=s.replace("function guessEnd(){chalStart()}","function guessEnd(){nextRound()}",1)
s=s.replace("function chalStep(){const c=G.ch;if(c.i>=G.teams.length)return gameFinal();","function chalStep(){const c=G.ch;if(c.i>=G.teams.length)return nextRound();",1)
s=s.replace("function chalStart(){G.ch={i:0,timer:null,left:20,used:[]};chalStep()}","function chalStart(){G.ch={i:0,timer:null,left:20,used:G.ch?G.ch.used:[]};chalStep()}",1)
s=s.replace("G.round=2;g.i++;","g.i++;",1)
s=s.replace("G.round=3;c.i++;","c.i++;",1)
s=s.replace("$('#sc-tag').textContent=`${L(TX.round)} ${G.round}`;","$('#sc-tag').textContent=`${L(TX.round)} ${G.round}/${ROUNDS.length}`;$('#sc-prize').textContent=L(TX.miniPrize)+': '+L(rnd(TX.mini));",1)
s=s.replace("$('#f-rematch').onclick=()=>{buzz(20);G.score=G.teams.map(()=>0);G.round=0;reflexStart()};","$('#f-rematch').onclick=()=>{buzz(20);G.score=G.teams.map(()=>0);gameStart()};\n$('#f-prize2').onclick=()=>{buzz(20);$('#f-prize').textContent=L(rnd(TX.fPrize))};",1)
s=s.replace("function gReset(){G={players:[],teams:[],judge:null,mode:null,score:[],round:0,","function gReset(){G={players:[],teams:[],judge:null,mode:null,score:[],round:0,ri:0,",1)
# guess round: with judge, ask 2 per team to fill time
s=s.replace("  if(G.judge!==null)T.forEach((t,ti)=>G.gs.order.push({ans:[G.judge],gs:t,team:ti}));","  if(G.judge!==null)T.forEach((t,ti)=>{G.gs.order.push({ans:[G.judge],gs:t,team:ti});G.gs.order.push({ans:t,gs:[G.judge],team:ti})});",1)
# prevent context menu on pads (iOS long press)
s=s.replace("reset();applyI();","document.addEventListener('contextmenu',e=>{if(e.target.closest('.pad'))e.preventDefault()});\nreset();applyI();",1)

assert 'nextRound' in s and 's-dare' in s and 'color-mix' not in s, 'patch failed'

# ---------- write artifact fragment (luxder.html) and full doc (index.html) ----------
open(root+r'\luxder.html','w',encoding='utf-8').write(s)
head='''<!doctype html>
<html lang="pt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Luxder">
<meta name="theme-color" content="#0B0A16">
<meta name="robots" content="noindex">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🦆</text></svg>">
<link rel="apple-touch-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%230B0A16'/><text y='.9em' font-size='80' x='8'>🦆</text></svg>">
'''
body_start=s.index('<canvas id="fx">')
full=head+s[:body_start]+'</head>\n<body>\n'+s[body_start:]+'\n</body>\n</html>\n'
open(root+r'\index.html','w',encoding='utf-8').write(full)
print('ok',len(s),len(full))
