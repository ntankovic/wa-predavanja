"""Original editable request-lifecycle diagrams; SVG and vector PDF share geometry."""
from pathlib import Path
from html import escape
import subprocess
D=Path(__file__).parent
import sys
sys.path.insert(0, str(D.parents[2] / 'scripts'))
from diagram_style import BLUE, INK, RED, text, box, arrow, markers
def save(name,body,h=440):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{h}" viewBox="0 0 1040 {h}">{markers()}<rect width="1040" height="{h}" fill="white"/>'+body+'</svg>'
 p=D/(name+'.hr.svg');p.write_text(svg);subprocess.run(['rsvg-convert','-f','pdf','-o',str(p.with_suffix('.pdf')),str(p)],check=True)
body=''
for x,l,sub in [(40,'Preglednik','prikaz i korisnikov unos'),(395,'Backend','obrada zahtjeva'),(750,'Baza','pohranjeni podaci')]:
 body+=box(x,65,250,105,l,sub)
body+=arrow(295,110,385,110)+arrow(650,110,740,110)
body+=text(520,225,'Strelice: tko koga poziva; odgovor se vraća obrnutim putem.',21)
body+=text(520,270,'Lokalni demo umjesto baze koristi testne podatke u memoriji.',21)
save('architecture',body,305)
labels=['Preglednik','Proxy','Backend','Baza'];xs=[105,375,645,915]
events=[(0,1,'GET /products'),(1,2,'proslijedi zahtjev'),(2,3,'dohvati proizvode'),(3,2,'zapisi proizvoda'),(2,1,'200 + JSON'),(1,0,'odgovor pregledniku')]
for phase in range(1,5):
 body=''
 for x,l in zip(xs,labels):body+=box(x-98,5,196,60,l)+f'<path d="M{x},70 V400" stroke="#b8cbd5" stroke-dasharray="6 5"/>'
 limits=[1,3,5,6];limit=limits[phase-1]
 for i,(a,b,label) in enumerate(events[:limit]):body+=arrow(xs[a],103+i*48,xs[b],103+i*48,label,dash=i>=3)
 body+=text(520,435,'Vrijeme teče prema dolje. Pune strelice: pozivi; isprekidane: odgovori.',19)
 save('sequence-'+str(phase),body,460)
body=box(50,75,270,110,'Preglednik','popis, loading, error')+box(385,75,270,110,'Backend','privremeni rezultat')+box(720,75,270,110,'Baza','trajni zapisi')
body+=text(185,240,'Zatvori karticu',22)+text(520,240,'Ponovno pokreni proces',22)+text(855,240,'Ponovno učitaj podatke',22)+text(520,315,'Pitaj: što nestaje, što ostaje i gdje postoji druga kopija?',23)
save('state',body,350)
body=box(60,35,240,70,'Preglednik')+box(740,35,240,70,'Poslužitelj')
body+=f'<rect x="45" y="130" width="950" height="250" rx="12" fill="#fafcfd" stroke="#b8cbd5"/>'+text(520,160,'jedna TCP veza (keep-alive)',19)
body+=arrow(180,205,860,205,'zahtjev A: GET /products')+arrow(860,255,180,255,'odgovor A',dash=True)+arrow(180,310,860,310,'zahtjev B: GET /products?case=empty')+arrow(860,360,180,360,'odgovor B',dash=True)+text(520,420,'Nakon odgovora veza ostaje otvorena; sljedeći zahtjev ne otvara novu.',22)
save('connection',body,450)
# CORS sequence: request reaches backend, browser withholds the response from JS (verified in headless Chrome).
# Both the page's JavaScript and the browser's network/CORS part run inside one browser (frame).
xs=[150,520,890]
body=f'<rect x="12" y="4" width="666" height="462" rx="16" fill="#f7fafc" stroke="#8aa7b8" stroke-width="2" stroke-dasharray="8 6"/>'+text(345,30,'Preglednik',20,INK,600)
body+=box(25,42,250,78,'Naš JavaScript','stranica s :3001')+box(395,42,250,78,'Mrežni dio','fetch, provjera CORS-a')+box(765,42,250,78,'Backend :3000')
for x in xs: body+=f'<path d="M{x},124 V450" stroke="#b8cbd5" stroke-dasharray="6 5"/>'
body+=arrow(150,165,520,165,'fetch(\'…:3000/products\')')
body+=arrow(520,225,890,225,'GET /products')+text(705,253,'Origin: http://127.0.0.1:3001',17,'#536b7b')
body+=f'<circle cx="890" cy="285" r="7" fill="{BLUE}"/>'+text(890,316,'obrađeno: 200 u terminalu',18)
body+=arrow(890,360,520,360,'200 + JSON',dash=True)+text(705,388,'bez Access-Control-Allow-Origin',17,'#536b7b')
body+=f'<path d="M508,402 L532,426 M532,402 L508,426" stroke="{RED}" stroke-width="4" stroke-linecap="round"/>'
body+=arrow(510,438,160,438,'TypeError: Failed to fetch',color=RED)
body+=text(520,495,'Vrijeme teče prema dolje. Odgovor je stigao u preglednik, ali ga preglednik ne predaje našem kodu.',17,'#627786')
save('cors-sequence',body,515)
# Basic request/response exchange (first HTTP slide).
body=box(40,40,280,110,'Preglednik','klijent: započinje razmjenu')+box(720,40,280,110,'Poslužitelj','program koji odgovara')
body+=arrow(330,80,710,80,'zahtjev: „Pošalji popis proizvoda.”')
body+=arrow(710,125,330,125,'odgovor: „Uspjelo je; evo popisa.”',dash=True)
body+=text(520,215,'Pune strelice: zahtjevi; isprekidane: odgovori. Isti zapis koristimo cijelo predavanje.',18,'#627786')
save('request-response',body,240)
# Two phases of loading: frame first, data later (answers the opening question).
L,R=380,880
body=box(L-130,8,260,62,'Preglednik')+box(R-130,8,260,62,'Backend')
for x in (L,R): body+=f'<path d="M{x},74 V420" stroke="#b8cbd5" stroke-dasharray="6 5"/>'
body+=arrow(L,115,R,115,'1. GET /')+arrow(R,160,L,160,'HTML: okvir stranice',dash=True)
body+=text(165,166,'okvir vidljiv',20,INK,600)
body+=f'<rect x="40" y="200" width="250" height="44" rx="22" fill="#fff4e5" stroke="#d9a441"/>'+text(165,229,'„Učitavanje…”',20)
body+=arrow(L,255,R,255,'2. GET /products (fetch)')+arrow(R,300,L,300,'JSON s proizvodima',dash=True)
body+=text(165,346,'3. kartice proizvoda',20,INK,600)
body+=f'<path d="M300,222 H360" stroke="#d9a441" stroke-width="2" stroke-dasharray="4 4"/>'
body+=text(520,400,'Ako korak 2 ne uspije ili zapne, stranica ostaje na „Učitavanje…”.',21,RED)
body+=text(520,445,'Vrijeme teče prema dolje.',18,'#627786')
save('two-phase',body,465)
# Cookie carries session context; each request is interpreted on its own (illustrative values).
L,R=230,810
body=box(L-130,8,260,62,'Preglednik')+box(R-130,8,260,62,'Backend')
for x in (L,R): body+=f'<path d="M{x},74 V390" stroke="#b8cbd5" stroke-dasharray="6 5"/>'
body+=arrow(L,115,R,115,'POST /login')
body+=arrow(R,175,L,175,'200 + Set-Cookie: sid=abc123',dash=True)
body+=text(L,212,'pamti sid=abc123',18,'#536b7b')
body+=arrow(L,262,R,262,'GET /cart + Cookie: sid=abc123')
body+=text(R,298,'sid → sesija → košarica',18,'#536b7b')
body+=arrow(R,345,L,345,'200 + košarica tog korisnika',dash=True)
body+=text(520,425,'Kontekst putuje u svakom zahtjevu; HTTP sam ne pamti prethodni zahtjev.',21)
body+=text(520,458,'Izmišljen primjer: naš nastavni backend nema /login ni /cart.',17,'#627786')
save('cookie-session',body,480)
# The same request on the wire: HTTP readable, HTTPS not (destination still visible).
def wire(y,label,payload,color,note):
 r=box(20,y,190,70,'Preglednik')+box(830,y,190,70,'Poslužitelj')
 r+=f'<path d="M210,{y+35} H830" stroke="#b8cbd5" stroke-width="3"/>'
 for x,l in [(380,'Wi-Fi mreža'),(660,'pružatelj interneta')]:
  r+=f'<circle cx="{x}" cy="{y+35}" r="9" fill="#e9f1f6" stroke="#8aa7b8"/>'+text(x,y+70,l,16,'#627786')
 r+=text(520,y-28,label,21,INK,600)
 r+=f'<rect x="420" y="{y+2}" width="200" height="50" rx="8" fill="white" stroke="{color}" stroke-width="2"/>'
 for i,line in enumerate(payload): r+=f'<text x="430" y="{y+22+i*20}" font-family="Menlo, monospace" font-size="14" fill="{color}">{escape(line)}</text>'
 r+=text(520,y+100,note,18,color)
 return r
body=wire(60,'HTTP: poruka putuje kao čitljiv tekst',['GET /orders/17','Cookie: sid=abc123'],RED,'Svatko na putu može pročitati i izmijeniti poruku.')
body+=wire(250,'HTTPS: ista poruka, šifrirana TLS-om',['8f 2a c1 9e 07 d4 b3','5a e0 71 c8 2f 96 …'],BLUE,'Na putu se vidi odredište, ali ne putanja, zaglavlja ni tijelo.')
save('https-wire',body,390)
# View states of the product fetch as a state machine (slide s08).
body=f'<circle cx="30" cy="210" r="11" fill="{INK}"/>'+arrow(43,210,92,210)+text(66,192,'klik',16,'#627786')
body+=box(100,160,250,100,'Čekanje','„Učitavanje proizvoda…”')
body+=box(700,20,310,100,'Podaci','popis proizvoda')+box(700,160,310,100,'Prazno','„Nema proizvoda za ovaj upit”')+box(700,300,310,100,'Greška','„Dohvat nije uspio”')
body+=f'<rect x="700" y="300" width="310" height="100" rx="16" fill="none" stroke="{RED}" stroke-width="2.5"/>'
body+=f'<path d="M352,210 H400 M400,70 V350" fill="none" stroke="{BLUE}" stroke-width="3"/>'
body+=arrow(400,70,692,70,'200 + niz s proizvodima')+arrow(400,210,692,210,'200 + []')
body+=f'<path d="M400,350 H400" stroke="{RED}"/>'+arrow(400,350,692,350,'nije 2xx · mreža · nije JSON',color=RED)
body+=f'<path d="M855,402 V425 H225 V270" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="7 6" marker-end="url(#arrow-blue)"/>'+text(540,445,'ponovni dohvat (iz svakog završnog stanja)',17,'#627786')
save('view-states',body,460)
# Lost response: aligned lifelines, one explicit break, equal endpoint summaries.
body=box(110,20,260,64,'Preglednik')+box(670,20,260,64,'Backend')
for x in (240,800):
 body+=f'<path d="M{x},84 V320" stroke="#cbd8df" stroke-width="2" stroke-dasharray="5 6"/>'
body+=arrow(240,140,800,140,'GET /products')
body+=f'<circle cx="800" cy="205" r="6" fill="{BLUE}"/>'
body+=text(800,188,'Obrada završena',22)
body+=f'<path d="M800,265 H535" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="9 6"/>'
body+=text(660,247,'odgovor',21,RED)
body+=f'<path d="M514,255 L534,275 M534,255 L514,275" stroke="{RED}" stroke-width="4" stroke-linecap="round"/>'
body+=text(524,308,'Prekid prijenosa',22,RED)
body+=text(240,360,'Odgovor nije primljen',23,RED)
body+=text(800,360,'Zahtjev je obrađen',23)
body+='<path d="M110,395 H930" stroke="#dbe4e9" stroke-width="1.5"/>'
body+=text(520,433,'Bez odgovora ne znamo je li obrada završila.',25)
body+=text(520,472,'Vrijeme teče prema dolje.',18,'#627786')
save('lost-response',body,490)
# Fictional timings as a Network-style waterfall: segment width proportional to ms, colour = where time is spent.
segs=[('DNS',20,'mreža','#8aa7b8'),('Veza / TLS',40,'mreža','#5f93b3'),('Zahtjev putuje',50,'mreža','#3886ad'),
      ('Obrada + baza',100,'poslužitelj','#c97a1e'),('Prijenos odgovora',40,'mreža','#3886ad'),('Prikaz',70,'preglednik','#8660a4')]
X0,W,Y,H=60,920,140,64; total=sum(m for _,m,_,_ in segs); sc=W/total
body=text(520,34,'Izmišljeni primjer jednog dohvata: ukupno 320 ms',24,INK,600)
body+=text(520,62,'Širina odgovara trajanju; vrijednosti nisu mjerenje.',17,'#627786')
# legend
x=X0
for i,(name,ms,where,col) in enumerate(segs):
    w=ms*sc
    r=12 if i in (0,len(segs)-1) else 0
    body+=f'<rect x="{x+1}" y="{Y}" width="{w-2}" height="{H}" rx="6" fill="{col}"/>'
    body+=text(x+w/2,Y+40,f'{ms} ms',19 if w>70 else 16,'#ffffff',700)
    # label below, staggered for narrow segments
    ly=Y+H+30 if i%2==0 else Y+H+56
    body+=f'<path d="M{x+w/2},{Y+H+4} V{ly-18}" stroke="#b8cbd5" stroke-width="1.5"/>'+text(x+w/2,ly,name,17,INK)
    x+=w
# time axis
ay=Y+H+92
body+=f'<path d="M{X0},{ay} H{X0+W}" stroke="#8aa7b8" stroke-width="2"/>'
for t in range(0,321,40):
    tx=X0+t*sc
    body+=f'<path d="M{tx},{ay-5} V{ay+5}" stroke="#8aa7b8" stroke-width="2"/>'+text(tx,ay+24,f'{t}',15,'#627786')
body+=text(X0+W+2,ay+44,'ms',15,'#627786')
# first byte marker and TTFB bracket
fb=X0+(20+40+50+100)*sc
body+=f'<path d="M{fb},{Y-30} V{Y+H+8}" stroke="{RED}" stroke-width="2.5" stroke-dasharray="6 4"/>'+text(fb,Y-38,'prvi bajt odgovora',16,RED,600)
body+=f'<path d="M{X0},{Y-12} V{Y-20} H{fb-4} V{Y-12}" fill="none" stroke="{INK}" stroke-width="2"/>'+text((X0+fb)/2,Y-26,'TTFB ≈ 210 ms',18,INK,600)
lx=300
for name,col in [('mreža','#3886ad'),('poslužitelj','#c97a1e'),('preglednik','#8660a4')]:
    body+=f'<rect x="{lx}" y="{ay+48}" width="18" height="18" rx="4" fill="{col}"/>'+f'<text x="{lx+26}" y="{ay+63}" font-family="Arial, sans-serif" font-size="17" fill="{INK}">{name}</text>'
    lx+=170
body+=text(520,ay+105,'„Spor server” je samo 100 od 320 ms; ostatak su mreža i preglednik.',19,INK)
save('latency',body,ay+125)
