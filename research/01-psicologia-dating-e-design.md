# Relatório 1: Ciência + Design para uma "dating app" de paródia no Lux Frágil

Research analyst, 2026-09-12.

## 1. Psicologia da atração e primeiro contacto

- **Humor vence quase sempre em contexto casual.** Investigação da Universidade do Kansas mostra que aberturas humorísticas/flippant superam abordagens diretas e inócuas em bares/festas, desde que entregues com confiança e sinal claro de que a pessoa "está na piada". Fazer rir supera qualquer outra tática de flirt, em ambos os géneros.
- **Benign Violation Theory (McGraw & Warren):** algo é engraçado quando é simultaneamente uma "violação" (transgride uma norma, expectativa ou tabu ligeiro) e é "benigno" (seguro, sem consequências reais). Aplicação: a app deve violar a norma "dating apps são a sério" (algoritmos absurdos, vereditos ridículos) mantendo tudo inofensivo e reversível. Nunca tocar em temas sensíveis (corpo, aparência séria, etnia).
- **Misattribution of arousal:** em ambientes ruidosos e de excitação física, as pessoas atribuem a ativação fisiológica à pessoa à frente em vez do ambiente. Um clube como o Lux já cria esse estado. A app só precisa de dar um pretexto social.
- **Reciprocidade de autorrevelação (Aron's 36 Questions / Fast Friends):** perguntas cada vez mais pessoais, em turnos, criam proximidade rápida. 3 a 5 perguntas rápidas e leves já geram o efeito quebra-gelo.

Ideias acionáveis:
1. Auto-ironia na copy da própria app ("Feito por 2 gajos em 25 minutos, sem investidores, sem propósito sério").
2. Perguntas tipo Aron mas absurdas/leves: "Qual é a tua ordem de karaoke de emergência?"
3. Veredicto final sempre positivo e engraçado, nunca um "não combinam" seco.
4. Nunca pedir dados reais. A app é o pretexto, a conversa acontece fora dela.

## 2. Design emocional: seguro, divertido, não-creepy

Recusar deve ser tão fácil e visível como aceitar. Nunca esconder o "não" atrás de links pequenos; nunca contagens decrescentes que pressionem.

1. Botão "Não, obrigada" do mesmo tamanho/cor que o "Sim".
2. Se ela recusar, ecrã de vitória: "Resposta certa. +10 pontos de inteligência emocional."
3. Primeira frase: "60 segundos, sem dados, sem pressão. Adoramos um 'não' bem dado."
4. Nunca pedir foto, nunca guardar nada, dizer isso no ecrã.
5. Interação iniciada pelo rapaz a mostrar o telemóvel, nunca insistindo.

## 3. Ângulo paródia/sátira

Exagerar tropos reconhecíveis: swipe, % pseudocientífica, selos "verificado", bios genéricas, "premium" ridículo.

1. "Match: 97%, algoritmo treinado por dois gajos e três imperiais."
2. Selo "Verificado ✅ (por um segurança do Lux)".
3. "Premium: desbloqueia a opção de ele pagar-te um shot" (sempre grátis, piada meta).
4. Bio automática em 1 clique: "Bailarina profissional de after-party, alérgica a conversa de trabalho."
5. Calculadora de compatibilidade com inputs absurdos (signo, música, pastel de nata vs bolo de chocolate).

## 4. UI/UX de nightclub

1. Fundo preto, texto branco/neon, tipografia gigante (mín. 28 px), 1 pergunta por ecrã.
2. Botões enormes, metade do ecrã cada, um único gesto (tap, não swipe fino).
3. Micro-interação visual (confetti, emoji a saltar) em vez de som; vibração como feedback silencioso.
4. Zero inputs de texto livre.
5. App num único ficheiro HTML, sem dependências de rede.

## 5. Mecânicas para reações variadas (ranqueadas)

1. "Roast me" situacional (nunca físico). Reação forte, risco baixo.
2. Calculadora de compatibilidade absurda.
3. Modo a dois (ela + ele respondem às cegas e comparam).
4. Veredicto científico falso ("Universidade de Alfama conclui: 73% de hipótese de dançar a mesma música").
5. Escolhe-a-tua-aventura de 3 cliques com final sempre positivo.

## 6. Lisboa / Lux Frágil

Público jovem, artístico, alternativo, LGBTQ+ friendly, misto, sofisticado mas descontraído. Valoriza inteligência e ironia.

1. Português informal de Lisboa, opção EN discreta.
2. Referências locais: pastel de nata, elétrico 28, Tejo, rooftop do Lux.
3. Inclusividade de género explícita.
4. Tom sarcástico, cool, autoconsciente, anti-dating-app.
5. Sem clichés de "boa noite linda".

## 7. Guardrails éticos

- Nunca simular match; nunca falsa urgência ou escassez.
- Nunca comentar corpo, peso, idade, etnia.
- Zero fotos.
- Amigas a observar: humor sobre a situação, nunca humilhação.
- 20-45: evitar gíria geracional de nicho.
- Se ela diz não, fecha-se leve, sem insistir.
- Nunca pedir número ou Instagram dentro da app.

## Top 10 prontas a implementar em 30 min

| # | Ideia | Reação | Esforço |
|---|-------|--------|---------|
| 1 | "Sim" / "Não, obrigada" iguais, vitória no "Não" | Alta | Muito baixo |
| 2 | Veredicto pseudocientífico com % e estudo falso | Alta | Baixo |
| 3 | "Match 97%, algoritmo treinado por 2 gajos e 3 imperiais" | Alta | Muito baixo |
| 4 | Roast situacional | Alta | Baixo |
| 5 | Calculadora de compatibilidade absurda | Média-alta | Médio |
| 6 | Confetti + vibração no fim | Alta | Baixo |
| 7 | Modo a dois | Alta | Médio |
| 8 | Selo "Verificado por um segurança do Lux" | Média | Muito baixo |
| 9 | Bio automática em 1 clique | Média | Baixo |
| 10 | Referências locais na copy | Média | Muito baixo |

Prioridade: 1 → 3 → 2 → 6 → 4.

## Fontes
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6593112/
- https://humorresearchlab.com/benign-violation-theory/
- https://en.wikipedia.org/wiki/Misattribution_of_arousal
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0183531
- https://theconversation.com/can-36-questions-really-change-your-love-life-273611
- https://ggia.berkeley.edu/practice/36_questions_for_increasing_closeness
- https://www.letsrun.com/forum/flat_read.php?thread=2052286
- https://punsio.com/dating-sites-jokes/
- https://auto-swiper.ch/blog/dating-profile-examples-funny
- https://uxmag.com/articles/consent-theater-are-users-really-in-control
- https://cookie-script.com/guides/ux-patterns-for-high-consent-rates
- https://www.travelgay.com/venue/lux-fragil
- https://www.misterbandb.com/gay-guide/portugal/lisbon/50-bars-clubs/10658-lux-fragil
- https://preply.com/pt/blog/humor-portugues/
- https://pt.wikipedia.org/wiki/Autodeprecia%C3%A7%C3%A3o
