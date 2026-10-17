# (num, nome, link, elemento, pegou, [(poke, meta, mortos)], combina)
N=[
(7,"Talia","G9d2mFX","🌿 Grama / floresta / deserto",True,[("Breloom",8),("Shiftry",8),("Cacturne",7),("Tropius",7)],"Nerida (já em andamento)"),
(2,"Nerida","xg5rMPJ","🌊 Água / mar",True,[("Wailord",6),("Whiscash",6),("Crawdaunt",6),("Luvdisc",6),("Clamperl",6)],"Maera (mar fundo: Clamperl ↔ Huntail/Gorebyss/Relicanth)"),
(18,"Maera","wVfbJ3e","🌊 Água / mar fundo",True,[("Milotic",8),("Huntail",8),("Gorebyss",7),("Relicanth",7)],"Glacis (Walrein é água/gelo)"),
(10,"Glacis","0e03YqH","❄️ Gelo / água",False,[("Glalie",15),("Walrein",15)],"Orlan (Pelipper fica no litoral)"),
(16,"Orlan","Vb1w5mD","🌊 Água + 🐉 Dragão/voador",False,[("Pelipper",15),("Altaria",15)],"Draven (Altaria ↔ Flygon/Salamence)"),
(5,"Draven","UvZJqKw","🐉 Dragão / deserto",False,[("Flygon",15),("Salamence",15)],"Verdra (Cradily/Roselia — pedra e grama)"),
(3,"Verdra","zvLFSgR","🌿 Grama + 🪨 Pedra",False,[("Roselia",15),("Cradily",15)],"Kaela (Sceptile na floresta)"),
(15,"Kaela","tJym2M8","🌿🔥🌊 Iniciais",False,[("Sceptile",10),("Blaziken",10),("Swampert",10)],"Calder (Blaziken ↔ fogo/vulcão)"),
(14,"Calder","vqSpNqd","🔥 Fogo / vulcão",False,[("Camerupt",15),("Torkoal",15)],"Ferris (caverna/montanha)"),
(6,"Ferris","PKI4Fgs","⚙️ Aço / caverna",False,[("Aggron",10),("Mawile",10),("Metagross",10)],"Selene (Claydol/Lunatone/Solrock em caverna)"),
(17,"Selene","IWLKYmI","🔮 Psíquico / pedra",False,[("Gardevoir",5),("Grumpig",5),("Chimecho",5),("Claydol",5),("Lunatone",5),("Solrock",5)],"Hadriel (Medicham é psíquico)"),
(11,"Hadriel","ocIvomr","🥊 Lutador / normal",False,[("Hariyama",10),("Medicham",10),("Slaking",10)],"Lucine (Slaking ↔ normais de rota)"),
(12,"Lucine","aLVehVK","⚪ Normal / rota",False,[("Linoone",8),("Delcatty",8),("Swellow",7),("Kecleon",7)],"Rohgar (pokes de campo/rota)"),
(4,"Rohgar","SJ6dfJN","🌑 Sombrio / campo",True,[("Mightyena",6),("Zangoose",6),("Seviper",6),("Absol",6),("Sharpedo",6)],"Veska (rota/mato). Obs: Sharpedo é de água, pode sair junto com Nerida/Maera"),
(13,"Veska","IEHYSjh","🐛 Inseto",False,[("Beautifly",5),("Dustox",5),("Masquerain",4),("Ninjask",4),("Volbeat",4),("Illumise",4),("Shedinja",4)],"Nyxen (Shedinja é fantasma)"),
(8,"Nyxen","xSn4850","👻 Fantasma / caverna escura",False,[("Sableye",10),("Banette",10),("Dusclops",10)],"Voltrix (último, sozinho)"),
(9,"Voltrix","UanfcaO","⚡ Elétrico",True,[("Manectric",30)],"— (fim). Volbeat/Illumise da Veska podem nascer perto"),
]
TIERS={
"Mítico":"Slaking",
"Lendário":"Flygon Absol",
"Ultra raro":"Milotic Glalie Salamence Tropius Sceptile Blaziken Swampert Torkoal Metagross Manectric Mightyena Gardevoir",
"Super raro":"Walrein Altaria Aggron Swellow Seviper Sharpedo",
"T1":"Whiscash Wailord Crawdaunt Huntail Gorebyss Relicanth Pelipper Breloom Shiftry Cacturne Camerupt Roselia Cradily Mawile Grumpig Chimecho Claydol Lunatone Solrock Hariyama Medicham Delcatty Kecleon Zangoose Beautifly Dustox Masquerain Ninjask Shedinja Sableye Banette Dusclops",
"T2":"Luvdisc Clamperl Linoone Volbeat Illumise",
}
ORDEM=["T2","T1","Super raro","Ultra raro","Lendário","Mítico"]  # mais fácil -> mais difícil
ICON={"T2":"⚪","T1":"🟢","Super raro":"🔵","Ultra raro":"🟣","Lendário":"🟠","Mítico":"🔴"}
TIER={p:t for t,ps in TIERS.items() for p in ps.split()}
SOLO={"T2","T1","Super raro"}
MORTOS={"Tropius":7,"Manectric":30,"Milotic":8,"Mightyena":6,"Absol":6,"Crawdaunt":6,"Luvdisc":6,"Gorebyss":7,"Clamperl":6,"Huntail":8}
todos=[p for n in N for p,_ in n[5]]
assert set(todos)==set(TIER), set(todos)^set(TIER)
def rank(p): return ORDEM.index(TIER[p])
def tier_txt(p): return f"{ICON[TIER[p]]} {TIER[p]}"
def modo(p): return "🟢 Sozinho (respawn)" if TIER[p] in SOLO else "🔴 Hunt lv alto"
def mortos(p,m): return min(MORTOS.get(p,0),m)
def hard_left(n): return [(p,m-mortos(p,m)) for p,m in n[5] if TIER[p] not in SOLO and mortos(p,m)<m]
solo=[n for n in N if not hard_left(n)]
duro=sorted([n for n in N if hard_left(n)],key=lambda n:(max(rank(p) for p,_ in hard_left(n)),sum(f for _,f in hard_left(n))))
N=solo+duro
RECOMPENSA=set()  # NPCs que já entregaram a recompensa
def pede(n): return ", ".join(f"{m} {p} ✅" if mortos(p,m)>=m else (f"{m-mortos(p,m)}/{m} {p}" if mortos(p,m) else f"{m} {p}") for p,m in sorted(n[5],key=lambda x:rank(x[0])))
def feito(n): return all(mortos(p,m)>=m for p,m in n[5])
done=[n for n in N if feito(n)]
solo=[n for n in solo if not feito(n)]
N=solo+duro
o=[]
def prog(n): return sum(mortos(p,m) for p,m in n[5]), sum(m for _,m in n[5])
def status(n):
    f,t=prog(n)
    return "✅" if f==t else "🔄" if n[4] else "⏳"
tot=sum(prog(n)[1] for n in N+done); feitos=sum(prog(n)[0] for n in N+done)
o+=["# Tasks de Hazard — PokeAlliance","",
"Cada NPC dá a sua própria quest.","",
"> ⚠️ O elemento/área de cada NPC é **suposição por tipo do Pokémon** — confirme no jogo e me avise para corrigir.","",
"**Status:** ✅ concluída · 🔄 em andamento · ⏳ pendente","",
"**Raridade (do jogo, mais fácil → mais difícil):** "+" · ".join(f"{ICON[t]} {t}" for t in ORDEM),"",
"- 🟢 **Sozinho (respawn):** T2, T1 e Super raro",
"- 🔴 **Hunt lv alto (difícil):** Ultra raro, Lendário e Mítico","",
"Dentro de cada NPC os pokes estão do mais fácil pro mais difícil.",""]
o+=["## Ordem e checklist das missões","",
"Primeiro os NPCs que dá pra fazer **sozinho** (só T2, T1 e Super raro). Por último os que têm qualquer poke de **hunt lv alto** (Ultra raro, Lendário, Mítico), do mais fácil pro mais difícil.",""]
HDR=["| Ordem | NPC | Status | Missão pega | Mapa | Pokes (✅ = já matou) | Hunt difícil | Progresso |","|---|---|---|---|---|---|---|---|"]
for i,n in enumerate(N,1):
    if i==1: o+=["### 🟢 Sozinho no respawn",""]+HDR
    if i==len(solo)+1: o+=["","### 🔴 Têm hunt de level alto (deixar por último)",""]+HDR
    f,t=prog(n)
    dif=[f"{p} ({TIER[p]})" for p,_ in hard_left(n)]
    o.append(f"| {i}º | {n[1]} (#{n[0]}) | {status(n)} | {'☑️' if n[4] else '⬜'} | [ver no mapa](https://imgur.com/a/{n[2]}) | {pede(n)} | {'🔴 '+', '.join(dif) if dif else '🟢 nenhuma'} | {f} / {t} |")
o+=["","### ✅ Concluídas (kills completas)",""]
if done:
    o+=["| NPC | Mapa | Pokes | Recompensa |","|---|---|---|---|"]
    for n in done: o.append(f"| {n[1]} (#{n[0]}) | [ver no mapa](https://imgur.com/a/{n[2]}) | {pede(n)} | {'✅ entregue' if n[1] in RECOMPENSA else '🎁 falta pegar'} |")
else: o.append("- nenhuma ainda")
o+=["",f"**Missões pegas: {sum(n[4] for n in N+done)} / {len(N)+len(done)}** · **Total: {feitos} / {tot} shinies**",""]
o+=["## 🔴 Hunts de level alto (todas as NPCs)","","Para juntar e fazer quando tiver time/level.","",
"| Pokémon | Raridade | NPC | Faltam |","|---|---|---|--:|"]
dur=[(p,m,n) for n in N+done for p,m in n[5] if TIER[p] not in SOLO]
for p,m,n in sorted(dur,key=lambda x:-rank(x[0])):
    f=m-mortos(p,m)
    o.append(f"| Sh {p} | {tier_txt(p)} | {n[1]} | {'✅ 0' if f==0 else f} |")
o.append("")
for i,n in enumerate(N,1):
    o+=[f"## {i}º · {n[1]} (NPC #{n[0]}) {status(n)}","",
        f"- [{'x' if n[4] else ' '}] Missão pega",
        f"- 📍 Mapa: [ver no mapa](https://imgur.com/a/{n[2]})",
        f"- Elemento: {n[3]}",
        f"- Pokes: {pede(n)}",
        f"- ➡️ Próximo: {N[i][1] if i<len(N) else '— (última)'}","",
        "| Pokémon | Raridade | Como | Meta | Mortos | Faltam |","|---|---|---|--:|--:|--:|"]
    for p,m in sorted(n[5],key=lambda x:rank(x[0])):
        k=mortos(p,m); f=m-k
        o.append(f"| Sh {p} | {tier_txt(p)} | {modo(p)} | {m} | {k} | {'✅ 0' if f==0 else f} |")
    o.append("")
open(__import__("os").path.join(__import__("os").path.dirname(__file__),"README.md"),"w").write("\n".join(o))
