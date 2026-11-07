import math
T=16.0
K={"build":"#db2777","data":"#0891b2","auth":"#7c3aed","approve":"#d97706","pay":"#059669","deploy":"#64748b"}
# id,x,y,w,h,title,sub,kind,glyph
N=[
 ("A0",30,10,170,56,"Triggers","webhooks · schedules","deploy","bolt"),
 ("A1",30,80,170,64,"Exchange APIs","REST · HMAC · OAuth","data","lock"),
 ("A2",30,158,170,64,"Market / macro data","feeds · on-chain · news","data","chart"),
 ("A3",30,236,170,64,"Research docs","PDF · reports","data","doc"),
 ("A4",30,314,170,64,"Users","web app · 7 languages","auth","globe"),
 ("B1",270,10,175,64,"Make","scenarios · webhooks","data","gear"),
 ("B2",270,88,175,64,"Workers / cron","content engine · VPS","data","server"),
 ("B3",270,166,175,64,"Claude agents","LLM · prompts · agents","approve","orbit"),
 ("B4",270,244,175,56,"Human approval","Telegram gate","approve","check"),
 ("B5",270,322,175,64,"Quant engine","backtests · risk scoring","data","bars"),
 ("D1",775,10,190,64,"Stripe","subscriptions · webhooks","pay","card"),
 ("D2",775,88,190,64,"Sheets / APIs","Google · reports","data","grid"),
 ("D3",775,166,190,64,"Discord / Telegram","bots · community","approve","bubble"),
 ("D4",775,244,190,64,"X API","scheduled publishing","approve","x"),
 ("D5",775,322,190,64,"Netlify / CDN","edge · signed URLs","deploy","cloud"),
 ("E0",30,498,170,64,"Budget caps","API cost guards","deploy","shield"),
 ("E1",270,498,190,64,"Monitoring / backups","errors · alerts","deploy","eye"),
 ("E2",515,498,190,64,"Actions / cron","GitHub · CI/CD · dispatch","deploy","branch"),
 ("E3",775,498,190,64,"Lovable / Netlify","auto-deploy from main","deploy","cloud"),
 ("S0",26,-182,160,76,"Discovery","client sessions · specs","build","bubble","workflows · ADRs"),
 ("S1",216,-182,160,76,"Design","UX flows · copy","build","pen","design system"),
 ("S2",406,-182,160,76,"Build","TypeScript · Python","build","code","SQL · React · Tailwind"),
 ("S3",596,-182,160,76,"QA / testing","Vitest · a11y","build","check","security · race-condition"),
 ("S4",786,-182,160,76,"Release","migrations · rollbacks","build","rocket","CI/CD · auto-deploy"),
]
ND={n[0]:n for n in N}
E=[
 ("e0","M200 38 C 235 38,240 42,270 42","data",2,3.0),
 ("e1","M200 112 C 380 112,440 100,515 100","data",3,4.2),
 ("e2","M200 190 C 235 190,240 120,270 120","data",2,3.0),
 ("e2b","M200 268 C 235 290,240 354,270 354","data",2,3.2),
 ("e4","M200 346 C 330 400,440 250,515 250","auth",3,4.8),
 ("e5","M445 42 C 480 42,490 66,515 66","data",2,3.0),
 ("e3","M445 120 C 480 120,490 130,515 130","data",2,3.0),
 ("e6","M357 152 L357 166","data",1,1.4),
 ("e6c","M357 230 L357 244","approve",1,1.4),
 ("e8","M445 198 C 480 198,490 188,515 188","data",2,3.0),
 ("e7","M445 272 C 600 400,700 232,775 205","approve",3,5.2),
 ("e7x","M445 288 C 560 440,720 440,775 280","approve",3,5.6),
 ("e16","M445 354 C 480 354,490 298,515 290","data",3,3.6),
 ("e20","M445 372 C 620 480,730 170,775 128","data",3,5.4),
 ("e9","M705 66 C 740 66,745 42,775 42","pay",3,2.6),
 ("e10","M705 130 C 740 130,745 110,775 112","data",2,3.0),
 ("e11","M705 198 C 740 198,745 198,775 198","data",2,3.0),
 ("e12","M705 280 C 740 300,745 354,775 354","auth",2,3.4),
 ("e15","M610 498 L610 310","deploy",3,3.6),
 ("e13","M870 498 L870 386","deploy",3,2.6),
 ("e14","M705 530 L775 530","deploy",2,1.8),
 ("e18","M515 530 L460 530","deploy",2,1.8),
 ("e19","M200 530 L270 530","deploy",1,1.4),
 ("e17","M530 310 C 500 440,480 470,440 498","deploy",2,4.2),
 ("s0","M186 -144 L216 -144","build",2,2.0),
 ("s1","M376 -144 L406 -144","build",2,2.0),
 ("s2","M566 -144 L596 -144","build",2,2.0),
 ("s3","M756 -144 L786 -144","build",2,2.0),
 ("fb","M30 346 H6 V-144 H26","build",3,7.0),
 ("rel","M946 -144 H994 V530 H965","build",3,7.0),
]
N=[n for n in N if not n[0].startswith("S")]
E=[e for e in E if e[0] not in ("s0","s1","s2","s3","fb","rel")]
def fx(x):
    if x<=200: off=0
    elif x<=270: off=30*(x-200)/70
    elif x<=445: off=30
    elif x<=515: off=30+36*(x-445)/70
    elif x<=705: off=66
    elif x<=775: off=66+36*(x-705)/70
    else: off=102
    return x+off
import re as _r
def map_path(d):
    toks=_r.split(r"(-?\d+\.?\d*)",d);out=[];i=0
    for t in toks:
        if _r.fullmatch(r"-?\d+\.?\d*",t):
            v=float(t)
            out.append(f"{fx(v):.1f}" if i%2==0 else t);i+=1
        else: out.append(t)
    return "".join(out)
N=[(n[0],fx(n[1]))+tuple(n[2:]) for n in N]
E=[(e[0],map_path(e[1]))+tuple(e[2:]) for e in E]
E+=[("fb","M30 346 L4 346","build",2,1.8),("rel","M1067 530 L1097 530","build",2,1.8)]
def kt(a,b):
    a=max(a,0.01);b=min(b,T)
    att=min(0.3,(b-a)*0.4);rel=min(0.15,(b-a)*0.3)
    t1=a+att;t2=max(b-rel,t1)
    return f'values="0;0;1;1;0;0" keyTimes="0;{a/T:.4f};{t1/T:.4f};{t2/T:.4f};{b/T:.4f};1" dur="{T}s" repeatCount="indefinite"'
o=[]
W=1180
import sys as _s0
_s0.path.insert(0,'.')
import handsketch as _hs0
_HB,_HT=_hs0.hand()
WRX,WRY,ROT=684.0,379.0,-38.0
_tips=[_hs0.rotp(t,ROT) for n,t in _HT]
_maxy=max(t[1] for t in _tips)+WRY
OFF=int(_maxy+118+92)
H=OFF+640
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Lior Dawit — Systems and Automation Builder. A hand conducting a live system map connecting exchange APIs, Make, Claude agents, Supabase, Stripe, Google Workspace, Discord, Telegram, X, Netlify, VPS and GitHub Actions.">')
o.append('''<style>
svg{--node:#ffffff;--node2:#f8fafc;--txt:#0f172a;--sub:#64748b;--lane:rgba(15,23,42,0.035);--lane-s:rgba(15,23,42,0.08);--grid:rgba(15,23,42,0.05);--shadow:rgba(15,23,42,0.14)}
@media (prefers-color-scheme: dark){svg{--node:#0f172a;--node2:#111c33;--txt:#f1f5f9;--sub:#94a3b8;--lane:rgba(148,163,184,0.06);--lane-s:rgba(148,163,184,0.14);--grid:rgba(148,163,184,0.07);--shadow:rgba(0,0,0,0.5)}}
.nf{fill:var(--node)}.nf2{fill:var(--node2)}.tt{fill:var(--txt)}.ss{fill:var(--sub)}.ln{fill:var(--lane);stroke:var(--lane-s)}.gd{stroke:var(--grid)}.gh{stroke:var(--node);stroke-width:5px;paint-order:stroke;stroke-linejoin:round}
text{font-family:'Segoe UI',-apple-system,Helvetica,Arial,sans-serif}
</style>''')
o.append('''<defs>
<linearGradient id="gb" x1="0" x2="1"><stop offset="0" stop-color="#0891b2"/><stop offset="1" stop-color="#7c3aed"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.14"/></filter>
<filter id="gl" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="2.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<radialGradient id="orbc"><stop offset="0" stop-color="#06b6d4" stop-opacity="0.55"/><stop offset="1" stop-color="#06b6d4" stop-opacity="0"/></radialGradient><radialGradient id="orbv"><stop offset="0" stop-color="#8b5cf6" stop-opacity="0.5"/><stop offset="1" stop-color="#8b5cf6" stop-opacity="0"/></radialGradient><radialGradient id="slit" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#050a14" stop-opacity="0.95"/><stop offset="1" stop-color="#050a14" stop-opacity="0"/></radialGradient><clipPath id="bclip"><rect x="0" y="0" width="1000" height="290" rx="20"/></clipPath><pattern id="grid" width="26" height="26" patternUnits="userSpaceOnUse"><path d="M26 0H0V26" fill="none" class="gd" stroke-width="1"/></pattern>
</defs>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')
BANNER_INNER=open('/Users/liordawit/Documents/My agent/job-hunt/github-profile/assets/banner.svg',encoding='utf-8').read()
BANNER_INNER=BANNER_INNER[BANNER_INNER.index('>')+1:BANNER_INNER.rindex('</svg>')]
BANNER_INNER=BANNER_INNER.replace('<circle cx="220" cy="150" r="130" fill="#06b6d4" opacity="0.24" filter="url(#blur)">','<circle cx="220" cy="150" r="190" fill="url(#orbc)" opacity="0.9">').replace('<circle cx="780" cy="190" r="140" fill="#8b5cf6" opacity="0.24" filter="url(#blur)">','<circle cx="780" cy="190" r="200" fill="url(#orbv)" opacity="0.9">')
import re as _rx
_parts=BANNER_INNER.split('<line ')
BANNER_INNER=_parts[0]+''.join(('<line '+p) for i,p in enumerate(_parts[1:]) if i%3==0)
BANNER_INNER=_rx.sub(r'\s*\n\s*','',BANNER_INNER)
o.append('<rect x="52" y="10" width="1074" height="312" rx="22" class="nf" fill-opacity="0.55" stroke="url(#gb)" stroke-opacity="0.5" stroke-width="1.6"/>')
o.append('<g transform="translate(52,10) scale(1.074)" clip-path="url(#bclip)">'+BANNER_INNER+'</g>')
o.append('<g transform="translate(38,'+str(OFF)+')">')
# lanes
lanes=[(14,-8,206,430,"SOURCES"),(284,-8,216,430,"ORCHESTRATION"),(562,-8,224,430,"CORE"),(858,-8,230,430,"SERVICES"),(14,484,1074,92,"OPERATIONS")]
for x,y,w,h,t in lanes:
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" class="ln" stroke-width="1"/>')
    o.append(f'<text x="{x+w/2}" y="{y-8 if y<0 else y-8}" text-anchor="middle" font-size="10.5" font-weight="700" letter-spacing="2.4" class="ss">{t}</text>')

# ---------- PROCESS CHAIN (horizontal cards) + GATES BETWEEN THE LAYERS ----------
PK="#db2777"
GATES=[(-14,"Discovery &amp; specs",(12.0,12.9),422),(252,"Build · test · repeat",(12.9,13.8),422),(531,"Integrate · test · repeat",(13.8,14.7),422),(822,"QA · security · a11y",(14.7,15.5),422),(1115,"Release",(15.5,16.0),576)]
CARDS=[]
for cx,lab,slot,bot in GATES:
    w=len(lab.replace("&amp;","&"))*7.0+58
    cabs=max(6+w/2,min(1174-w/2,cx+38))
    CARDS.append((cabs,w,lab,cx))
for gi,(cabs,w,lab,cx) in enumerate(CARDS):
    slot=GATES[gi][2];bot=GATES[gi][3]
    cg=cabs-38;ht=bot-(-8)
    # gate pill (no text)
    o.append(f'<rect x="{cx-18}" y="-8" width="36" height="{ht}" rx="18" fill="{PK}" fill-opacity="0.06" stroke="{PK}" stroke-opacity="0.5" stroke-width="1.4"/>')
    for yy in (14,bot-22):
        o.append(f'<g transform="translate({cx},{yy})"><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="{3+gi*0.4:.1f}s" repeatCount="indefinite"/><path d="M-6.5 0 A6.5 6.5 0 1 1 0 6.5" fill="none" stroke="{PK}" stroke-width="1.8" stroke-linecap="round"/><path d="M-2.5 3.5 L0 6.5 L3 3.5" fill="none" stroke="{PK}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></g></g>')
    o.append(f'<circle cx="{cx}" r="3.4" fill="{PK}" filter="url(#gl)"><animate attributeName="cy" values="34;{bot-40};34" dur="{4+gi*0.6:.1f}s" repeatCount="indefinite"/></circle>')
    a,b=slot
    o.append(f'<rect x="{cx-18}" y="-8" width="36" height="{ht}" rx="18" fill="none" stroke="{PK}" stroke-width="3.6" opacity="0" filter="url(#gl)"><animate attributeName="opacity" {kt(a,b)}/></rect>')
    # stem from the card down to the pill
    o.append(f'<path d="M{cx} -62 L{cx} -8" stroke="{PK}" stroke-opacity="0.6" stroke-width="1.4" stroke-dasharray="3 5" fill="none"/>')
    # horizontal label card
    o.append(f'<g filter="url(#sh)"><rect x="{cg-w/2:.1f}" y="-92" width="{w:.1f}" height="30" rx="15" class="nf" stroke="{PK}" stroke-opacity="0.8" stroke-width="1.5"/></g>')
    o.append(f'<g transform="translate({cg-w/2+19:.1f},-77)"><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="{3+gi*0.4:.1f}s" repeatCount="indefinite"/><path d="M-5.5 0 A5.5 5.5 0 1 1 0 5.5" fill="none" stroke="{PK}" stroke-width="1.7" stroke-linecap="round"/><path d="M-2 3 L0 5.5 L2.5 3" fill="none" stroke="{PK}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></g></g>')
    o.append(f'<text x="{cg-w/2+34:.1f}" y="-72" font-size="12.5" font-weight="700" fill="{PK}">{lab}</text>')
    o.append(f'<rect x="{cg-w/2:.1f}" y="-92" width="{w:.1f}" height="30" rx="15" fill="none" stroke="{PK}" stroke-width="3.4" opacity="0" filter="url(#gl)"><animate attributeName="opacity" {kt(a,b)}/></rect>')
# iteration chain between neighbouring cards
for gi in range(4):
    x1=CARDS[gi][0]-38+CARDS[gi][1]/2;x2=CARDS[gi+1][0]-38-CARDS[gi+1][1]/2
    o.append(f'<path id="arc{gi}" d="M{x1:.1f} -77 L{x2:.1f} -77" fill="none" stroke="{PK}" stroke-opacity="0.6" stroke-width="1.6" stroke-dasharray="4 6"><animate attributeName="stroke-dashoffset" from="20" to="0" dur="1.6s" repeatCount="indefinite"/></path>')
    o.append(f'<circle r="3.4" fill="{PK}" filter="url(#gl)"><animateMotion dur="{3.2+gi*0.5:.1f}s" repeatCount="indefinite" keyPoints="0;1;0" keyTimes="0;0.5;1" calcMode="linear"><mpath href="#arc{gi}"/></animateMotion></circle>')
# ripples around core
o.append('<g transform="translate(66,0)">')
for i in range(3):
    o.append(f'<rect x="515" y="40" width="190" height="270" rx="16" fill="none" stroke="#7c3aed" stroke-width="1.5" opacity="0"><animate attributeName="opacity" values="0;0.5;0" dur="4.5s" begin="{i*1.5}s" repeatCount="indefinite"/><animate attributeName="x" values="515;497" dur="4.5s" begin="{i*1.5}s" repeatCount="indefinite"/><animate attributeName="y" values="40;22" dur="4.5s" begin="{i*1.5}s" repeatCount="indefinite"/><animate attributeName="width" values="190;226" dur="4.5s" begin="{i*1.5}s" repeatCount="indefinite"/><animate attributeName="height" values="270;306" dur="4.5s" begin="{i*1.5}s" repeatCount="indefinite"/></rect>')
o.append('</g>')
# edges base (marching dashes)
o.append('<g fill="none" stroke-width="1.8" stroke-linecap="round">')
for eid,d,k,cnt,dur in E:
    o.append(f'<path id="{eid}" d="{d}" stroke="{K[k]}" stroke-opacity="0.5" stroke-dasharray="5 7"><animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.6s" repeatCount="indefinite"/></path>')
o.append('</g>')
# story highlight edges
SEQ=[("e1",0.6,1.2),("e12",2.4,3.1),("e2",4.6,5.1),("e6",5.7,6.1),("e6c",6.7,7.0),("e7",7.6,8.2),("e7x",7.6,8.2),("e2b",9.5,10.0),("e20",10.6,11.3)]
o.append('<g fill="none" stroke-linecap="round" filter="url(#gl)">')
for eid,a,b in SEQ:
    col=[v for (i,d,v,c,du) in E if i==eid][0]
    d=[d for (i,d,v,c,du) in E if i==eid][0]
    o.append(f'<path d="{d}" stroke="{K[col]}" stroke-width="4" opacity="0"><animate attributeName="opacity" {kt(a,b)}/></path>')
o.append('</g>')
# core supabase
o.append('<g transform="translate(66,0)">')
o.append('''<g filter="url(#sh)"><rect x="515" y="40" width="190" height="270" rx="16" class="nf" stroke="url(#gb)" stroke-width="2.6"/></g>
<rect x="515" y="40" width="190" height="270" rx="16" fill="url(#gb)" opacity="0.06"/>
<text x="610" y="72" text-anchor="middle" font-size="18" font-weight="800" class="tt">Supabase</text>
<text x="610" y="90" text-anchor="middle" font-size="11" class="ss">the core backend</text>''')
chips=[("PostgreSQL","#0891b2",(2.0,3.0)),("Row-level security","#7c3aed",None),("Edge Functions","#0891b2",(2.0,3.0)),("Scheduled jobs","#059669",None),("Audit-log triggers","#7c3aed",None)]
# order chips so storyline lights Edge Functions then PostgreSQL
chips=[("Edge Functions","#0891b2",(1.2,1.8)),("PostgreSQL","#0891b2",(1.8,2.4)),("Row-level security","#7c3aed",None),("Scheduled jobs","#059669",None),("Audit-log triggers","#7c3aed",None)]
for i,(t,c,slot) in enumerate(chips):
    y=104+i*40
    o.append(f'<rect x="533" y="{y}" width="154" height="30" rx="9" class="nf2" stroke="{c}" stroke-opacity="0.75"/>')
    o.append(f'<circle cx="549" cy="{y+15}" r="3.4" fill="{c}"><animate attributeName="opacity" values="1;0.3;1" dur="{2+i*0.4}s" repeatCount="indefinite"/></circle>')
    o.append(f'<text x="562" y="{y+19.5}" font-size="12.5" class="tt">{t}</text>')
    if slot:
        a,b=slot
        o.append(f'<rect x="533" y="{y}" width="154" height="30" rx="9" fill="none" stroke="{c}" stroke-width="3.2" opacity="0" filter="url(#gl)"><animate attributeName="opacity" {kt(a,b)}/></rect>')
o.append('</g>')
# nodes
def glyph(g,cx,cy,c):
    s=f'stroke="{c}" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    s3=s.replace('stroke-width="1.8"','stroke-width="3"'); s24=s.replace('stroke-width="1.8"','stroke-width="2.4"')
    if g=="bolt": return f'<path d="M{cx} {cy-9} l-6 10 h5 l-2 8 l7 -11 h-5 z" {s}/>'
    if g=="lock": return f'<rect x="{cx-6}" y="{cy-2}" width="12" height="9" rx="2" {s}/><path d="M{cx-4} {cy-2} v-3 a4 4 0 0 1 8 0 v3" {s}/>'
    if g=="chart": return f'<path d="M{cx-8} {cy+6} l5 -6 l4 3 l7 -9" {s}/>'
    if g=="doc": return f'<path d="M{cx-6} {cy-8} h8 l4 4 v12 h-12 z" {s}/><path d="M{cx-3} {cy} h6 M{cx-3} {cy+4} h6" {s}/>'
    if g=="globe": return f'<circle cx="{cx}" cy="{cy}" r="8" {s}/><ellipse cx="{cx}" cy="{cy}" rx="3.5" ry="8" {s}/><path d="M{cx-8} {cy} h16" {s}/>'
    if g in("gear","gear2"):
        d=7 if g=="gear" else -7
        return f'<g transform="translate({cx},{cy})"><g><animateTransform attributeName="transform" type="rotate" from="0" to="{360 if g=="gear" else -360}" dur="{d if d>0 else 9}s" repeatCount="indefinite"/><circle r="7.5" stroke="{c}" fill="none" stroke-width="3.6" stroke-dasharray="3.1 2.5"/><circle r="3" stroke="{c}" fill="none" stroke-width="1.8"/></g></g>'
    if g=="orbit": return f'<g transform="translate({cx},{cy})"><circle r="2.8" fill="{c}"/><circle r="8" fill="none" stroke="{c}" stroke-opacity="0.35"/><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="3.2s" repeatCount="indefinite"/><circle cx="8" cy="0" r="2.2" fill="{c}"/><circle cx="-4" cy="-6.9" r="1.8" fill="{c}"/></g></g>'
    if g=="check": return f'<circle cx="{cx}" cy="{cy}" r="8" {s}/><path d="M{cx-4} {cy} l3 3 l5 -6" {s}/>'
    if g=="bars": return f'<path d="M{cx-7} {cy+7} v-5 M{cx-2} {cy+7} v-11 M{cx+3} {cy+7} v-8 M{cx+8} {cy+7} v-14" {s3}/>'
    if g=="card": return f'<rect x="{cx-9}" y="{cy-6}" width="18" height="12" rx="2.5" {s}/><path d="M{cx-9} {cy-2} h18" {s}/>'
    if g=="grid": return f'<rect x="{cx-8}" y="{cy-8}" width="16" height="16" rx="2" {s}/><path d="M{cx-8} {cy} h16 M{cx} {cy-8} v16" {s}/>'
    if g=="bubble": return f'<path d="M{cx-9} {cy-7} h18 v11 h-9 l-5 5 v-5 h-4 z" {s}/>'
    if g=="x": return f'<path d="M{cx-7} {cy-7} l14 14 M{cx+7} {cy-7} l-14 14" {s24}/>'
    if g=="cloud": return f'<path d="M{cx-8} {cy+5} a5 5 0 0 1 1 -9 a6 6 0 0 1 11 1 a4 4 0 0 1 0 8 z" {s}/>'
    if g=="shield": return f'<path d="M{cx} {cy-9} l8 3 v6 c0 5 -4 8 -8 10 c-4 -2 -8 -5 -8 -10 v-6 z" {s}/>'
    if g=="eye": return f'<path d="M{cx-9} {cy} c3 -6 15 -6 18 0 c-3 6 -15 6 -18 0 z" {s}/><circle cx="{cx}" cy="{cy}" r="2.6" fill="{c}"/>'
    if g=="server": return f'<rect x="{cx-8}" y="{cy-8}" width="16" height="6" rx="2" {s}/><rect x="{cx-8}" y="{cy+2}" width="16" height="6" rx="2" {s}/><circle cx="{cx+4}" cy="{cy-5}" r="1" fill="{c}"/><circle cx="{cx+4}" cy="{cy+5}" r="1" fill="{c}"/>'
    if g=="branch": return f'<circle cx="{cx-5}" cy="{cy-6}" r="2.4" {s}/><circle cx="{cx-5}" cy="{cy+6}" r="2.4" {s}/><circle cx="{cx+6}" cy="{cy-2}" r="2.4" {s}/><path d="M{cx-5} {cy-3.6} v7.2 M{cx-5} {cy+1} c0 -3 11 -1 11 -4" {s}/>'
    if g=="code": return f'<path d="M{cx-4} {cy-6} l-6 6 l6 6 M{cx+4} {cy-6} l6 6 l-6 6" {s}/>'
    if g=="pen": return f'<path d="M{cx-7} {cy+7} l1 -5 l9 -9 l4 4 l-9 9 z" {s}/>'
    if g=="rocket": return f'<path d="M{cx} {cy-9} c4 3 5 9 3 13 h-6 c-2 -4 -1 -10 3 -13 z" {s}/><path d="M{cx-3} {cy+6} l-3 3 M{cx+3} {cy+6} l3 3" {s}/>'
    return ""
NSLOT={"A1":(0.0,0.6),"D5":(3.1,4.0),"A2":(4.0,4.6),"B2":(5.1,5.7),"B3":(6.1,6.7),"B4":(7.0,7.6),"D3":(8.2,9.0),"D4":(8.2,9.0),"A3":(9.0,9.5),"B5":(10.0,10.6),"D2":(11.3,12.0)}
for nd in N:
    nid,x,y,w,h,t,s,k,g=nd[:9]; s2=nd[9] if len(nd)>9 else None
    c=K[k]
    o.append(f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="nf" stroke="{c}" stroke-opacity="0.7" stroke-width="1.5"/></g>')
    o.append(f'<rect x="{x}" y="{y+12}" width="3.5" height="{h-24}" rx="1.7" fill="{c}"/>')
    o.append(f'<text x="{x+16}" y="{y+(24 if h>=60 else 22)}" font-size="14" font-weight="700" class="tt">{t}</text>')
    o.append(f'<text x="{x+16}" y="{y+(43 if h>=60 else 40)}" font-size="11" class="ss">{s}</text>')
    if s2: o.append(f'<text x="{x+16}" y="{y+58}" font-size="10.5" class="ss">{s2}</text>')
    o.append(glyph(g,x+w-24,y+(24 if s2 else h/2),c))
    if nid in NSLOT:
        a,b=NSLOT[nid]
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="none" stroke="{c}" stroke-width="3.4" opacity="0" filter="url(#gl)"><animate attributeName="opacity" {kt(a,b)}/></rect>')
# packets
o.append('<g filter="url(#gl)">')
for eid,d,k,cnt,dur in E:
    for j in range(cnt):
        bg=f"{j*dur/cnt:.2f}"
        o.append(f'<circle r="3.8" fill="{K[k]}"><animateMotion dur="{dur}s" repeatCount="indefinite" begin="{bg}s"><mpath href="#{eid}"/></animateMotion><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.9;1" dur="{dur}s" begin="{bg}s" repeatCount="indefinite"/></circle>')
o.append('</g>')
# legend
leg=[("data / sync","data"),("auth &amp; access","auth"),("approval gate","approve"),("payments","pay"),("deploy &amp; ops","deploy"),("build &amp; QA","build")]
x=34
for t,k in leg:
    o.append(f'<circle cx="{x}" cy="604" r="4.5" fill="{K[k]}" filter="url(#gl)"/><text x="{x+12}" y="608" font-size="11.5" class="ss">{t}</text>')
    x+=len(t.replace("&amp;","&"))*7+46
o.append('</g>')

# ---------- THE HAND: pen-and-ink, bursting out of the banner ----------
import sys,math as _mm
sys.path.insert(0,'.')
import handsketch as hs
HBODY,HTIPS=hs.hand()
ARM=hs.arm()
pass
o.append('<g id="hand-layer">')
# slit the arm comes out of
o.append('<ellipse cx="640" cy="323" rx="64" ry="11" fill="url(#slit)"/><path d="M580 323 C 610 316, 670 316, 700 323" fill="none" stroke="var(--txt)" stroke-width="1.4" opacity="0.55"/>')
# strings (behind the hand), from the tied fingertips to the process cards
cols=["#db2777","#7c3aed","#0891b2","#7c3aed","#db2777"]
durs=[3.6,3.0,2.6,3.2,3.8]
order=["pinky","ring","middle","index","thumb"]
tipmap=dict(HTIPS)
for k,nm in enumerate(order):
    lx,ly=tipmap[nm]
    ax,ay=hs.rotp((lx,ly),ROT)
    ax+=WRX;ay+=WRY
    bx,by=CARDS[k][0],OFF-92
    d=f"M{ax:.1f} {ay:.1f} C {ax:.1f} {ay+100:.1f}, {bx:.1f} {by-120:.1f}, {bx:.1f} {by:.1f}"
    sway=f'<animateTransform attributeName="transform" type="rotate" values="0 {ax:.1f} {ay:.1f};0.3 {ax:.1f} {ay:.1f};0 {ax:.1f} {ay:.1f};-0.3 {ax:.1f} {ay:.1f};0 {ax:.1f} {ay:.1f}" dur="{durs[k]+1.5}s" repeatCount="indefinite"/>'
    o.append(f'<g>{sway}<path id="str{k}" d="{d}" fill="none" stroke="var(--txt)" stroke-width="1.1" stroke-opacity="0.85" stroke-linecap="round"/>'
             f'<circle cx="{bx:.1f}" cy="{by}" r="3.4" fill="var(--node)" stroke="var(--txt)" stroke-width="1.2"/>'
             f'<circle cx="{bx:.1f}" cy="{by}" r="3" fill="none" stroke="{cols[k]}" stroke-width="1.6" opacity="0"><animate attributeName="r" values="3;16" dur="{durs[k]}s" begin="{durs[k]*0.82+k*0.4:.2f}s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.9;0" dur="{durs[k]}s" begin="{durs[k]*0.82+k*0.4:.2f}s" repeatCount="indefinite"/></circle>'
             f'<circle r="3.2" fill="{cols[k]}" filter="url(#gl)"><animateMotion dur="{durs[k]}s" repeatCount="indefinite" begin="{k*0.4:.1f}s"><mpath href="#str{k}"/></animateMotion><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.12;0.88;1" dur="{durs[k]}s" begin="{k*0.4:.1f}s" repeatCount="indefinite"/></circle></g>')
# arm + hand, gently bobbing
o.append(f'<g transform="translate({WRX},{WRY}) rotate({ROT})"><g><animateTransform attributeName="transform" type="translate" values="0 0;0 2.5;0 0;0 -1.5;0 0" dur="5s" repeatCount="indefinite"/>{ARM}{HBODY}</g></g>')
o.append('</g>')
o.append('</svg>')
open("system-map.svg","w",encoding="utf-8").write("\n".join(o))
print(len("\n".join(o)))
