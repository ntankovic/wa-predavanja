"""Original diagrams for Lecture 02 (backend architecture); SVG and vector PDF share geometry."""
from pathlib import Path
from html import escape
import subprocess, sys
D = Path(__file__).parent
sys.path.insert(0, str(D.parents[2] / 'scripts'))
from diagram_style import BLUE, INK, RED, text, box, arrow, markers

GREY = '#627786'
GREEN = '#277b59'

def save(name, body, h=440):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{h}" viewBox="0 0 1040 {h}">'
           f'{markers()}<rect width="1040" height="{h}" fill="white"/>' + body + '</svg>')
    p = D / (name + '.hr.svg'); p.write_text(svg)
    subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', str(p.with_suffix('.pdf')), str(p)], check=True)

def mono(x, y, value, size=17, color=INK, anchor='start'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Menlo, Consolas, monospace" '
            f'font-size="{size}" fill="{color}">{escape(value)}</text>')

def lifelines(names, xs, top=8, bottom=500, w=150):
    r = ''
    for x, n in zip(xs, names):
        r += box(x - w / 2, top, w, 58, n)
        r += f'<path d="M{x},{top+62} V{bottom}" stroke="#b8cbd5" stroke-dasharray="6 5"/>'
    return r

def xmark(x, y, s=11):
    return f'<path d="M{x-s},{y-s} L{x+s},{y+s} M{x+s},{y-s} L{x-s},{y+s}" stroke="{RED}" stroke-width="4" stroke-linecap="round"/>'

# 1. One naive handler mixes jobs that change for different reasons.
rows = [
    ('for await (…) JSON.parse(text)', 'čitanje HTTP tijela', 'drugi format ili framework'),
    ('if (!body.email …) → 400', 'provjera ulaza', 'nova pravila unosa'),
    ('products.find(p => …)', 'pristup podacima', 'baza umjesto niza (4. tj.)'),
    ('if (product.stock < quantity)', 'poslovno pravilo', 'popust, najviše 5 komada'),
    ('product.stock -= …; orders.push', 'promjena podataka', 'transakcija (5. tj.)'),
    ("console.log('Šaljem e-poštu…')", 'vanjska usluga', 'pravi pružatelj e-pošte'),
    ('res.writeHead(201, …)', 'HTTP odgovor', 'dogovor o statusima (3. tj.)'),
]
body = text(240, 30, 'Naivni handler', 20, INK, 600) + text(590, 30, 'Posao', 20, INK, 600) + text(870, 30, 'Mijenja se kad…', 20, INK, 600)
for i, (code, job, reason) in enumerate(rows):
    y = 50 + i * 56
    fill = '#f3f8fb' if i % 2 == 0 else '#ffffff'
    body += f'<rect x="30" y="{y}" width="420" height="48" rx="6" fill="{fill}" stroke="#d4e3ec"/>' + mono(46, y + 30, code, 16)
    body += f'<path d="M450,{y+24} H500" stroke="#b8cbd5" stroke-width="2"/>'
    body += f'<rect x="500" y="{y+4}" width="180" height="40" rx="20" fill="#e7f3fb" stroke="#8cbad7"/>' + text(590, y + 30, job, 17)
    body += f'<path d="M680,{y+24} H730" stroke="#b8cbd5" stroke-width="2"/>' + f'<text x="740" y="{y+30}" font-family="Arial, sans-serif" font-size="17" fill="{GREY}">{escape(reason)}</text>'
body += text(520, 465, 'Sedam poslova u jednoj funkciji; svaki se mijenja iz drugog razloga.', 20)
save('one-handler', body, 485)

# 2. Responsibilities after splitting: who calls whom.
body = box(345, 10, 350, 70, 'Usmjeravanje', '') + box(345, 120, 350, 70, 'HTTP sloj (handler)') + box(345, 230, 350, 70, 'Servis (pravila)')
for x, l in [(60, 'Katalog'), (370, 'Narudžbe'), (680, 'Obavijest')]:
    body += box(x, 360, 300, 70, l)
body += arrow(520, 82, 520, 112) + arrow(520, 192, 520, 222)
body += arrow(470, 302, 230, 352) + arrow(520, 302, 520, 352) + arrow(570, 302, 810, 352)
for y, t in [(45, 'metoda + putanja → handler'), (155, 'čita zahtjev, piše odgovor, bira status'), (265, 'ne zna za HTTP ni za vrstu pohrane')]:
    body += f'<text x="715" y="{y+5}" font-family="Arial, sans-serif" font-size="17" fill="{GREY}">{escape(t)}</text>'
body += text(520, 470, 'Strelica: poziva. Gornji dio zna za HTTP, donji za podatke i vanjske usluge.', 18, GREY)
save('layers', body, 490)

# 3. POST /orders through the parts (sequence; time downwards).
names = ['Handler', 'Servis', 'Katalog', 'Narudžbe', 'Obavijest']
xs = [150, 345, 540, 735, 930]
body = lifelines(names, xs, bottom=560, w=170)
body += arrow(15, 115, 150, 115, 'POST /orders')
ev = [
    (0, 1, 'placeOrder(body)', False), (1, 2, 'findById(7)', False),
    (2, 1, 'proizvod, zaliha 5', True), (1, 2, 'decreaseStock(7, 2)', False), (1, 3, 'save(narudžba)', False),
    (3, 1, '{ id: 1, … }', True), (1, 4, 'orderPlaced(…)', False), (1, 0, 'narudžba', True),
]
for i, (a, b, l, dash) in enumerate(ev):
    y = 165 + i * 46
    body += arrow(xs[a], y, xs[b], y, l, dash=dash)
body += arrow(150, 545, 15, 545, '201 + JSON', dash=True)
body += text(520, 595, 'Pune strelice: pozivi funkcija; isprekidane: povratne vrijednosti. Vrijeme teče prema dolje.', 17, GREY)
save('order-sequence', body, 610)

# 4. Dependency direction: the service receives its dependencies; server.mjs composes.
body = box(30, 60, 250, 80, 'HTTP sloj') + box(395, 60, 250, 80, 'Servis') + box(760, 40, 250, 120, 'Ovisnosti', 'katalog, narudžbe, obavijest')
body += arrow(282, 100, 387, 100, 'poziva') + arrow(647, 100, 752, 100, 'poziva')
body += box(270, 300, 500, 80, 'server.mjs', '')
for x in (155, 520, 885):
    body += arrow(520 + (x - 520) * 0.55, 296, x, 168, dash=True)
body += text(300, 225, 'stvara i predaje', 18, GREY)
body += text(520, 420, 'Servis ne uvozi node:http ni memory-catalog.mjs: radi s onim što dobije.', 20)
body += text(520, 452, 'Samo server.mjs zna koje se konkretne implementacije koriste.', 18, GREY)
save('dependency-direction', body, 475)

# 5. Swap the implementation behind the same functions.
body = box(395, 10, 250, 70, 'Servis') + f'<rect x="300" y="125" width="440" height="80" rx="12" fill="#fff" stroke="{BLUE}" stroke-width="2" stroke-dasharray="8 5"/>'
body += text(520, 158, 'katalog', 21, INK, 600) + mono(520, 186, 'findById(id) · decreaseStock(id, n)', 16, INK, 'middle')
body += arrow(520, 82, 520, 118, '')
for x, l, s in [(40, 'Memorija', 'danas (02)'), (395, 'PostgreSQL', '4. predavanje'), (750, 'Lažni katalog', 'u testu')]:
    body += box(x, 290, 250, 100, l, s) + arrow(x + 125, 284, 520 + (x + 125 - 520) * 0.3, 212, dash=True)
body += text(520, 440, 'Isprekidana strelica: ostvaruje iste funkcije. Servis se ne mijenja.', 19, GREY)
save('swap-implementation', body, 460)

# 6. Process lifecycle with failure exits.
steps = [(30, 'Konfiguracija', 'čitanje i provjera'), (290, 'Sastavljanje', 'stvaranje ovisnosti'), (550, 'listen', 'tek sada stižu zahtjevi'), (810, 'Rad', 'obrada zahtjeva')]
body = text(520, 28, 'Pokretanje', 20, INK, 600)
for i, (x, l, s) in enumerate(steps):
    body += box(x, 45, 200, 100, l, s)
    if i < 3: body += arrow(x + 202, 95, x + 282, 95)
for x, l in [(130, 'neispravno → exit 1'), (650, 'port zauzet → exit 1')]:
    body += arrow(x, 150, x, 205, color=RED) + text(x, 230, l, 17, RED)
body += text(520, 298, 'Gašenje (SIGINT / SIGTERM)', 20, INK, 600)
g = [(30, 'server.close()', 'nema novih veza'), (290, 'Dovrši započete', 'odgovori ih šalju do kraja'), (550, 'exit 0', 'uredan kraj')]
for i, (x, l, s) in enumerate(g):
    body += box(x, 315, 200, 100, l, s)
    if i < 2: body += arrow(x + 202, 365, x + 282, 365)
body += f'<path d="M910,147 V265 H130 V280" fill="none" stroke="{BLUE}" stroke-width="3"/>' + arrow(130, 278, 130, 307)
body += arrow(390, 420, 390, 450, color=RED) + text(390, 472, 'traje > 10 s → exit 1', 17, RED)
save('lifecycle', body, 490)

# 7. Graceful shutdown timeline (measured locally: NOTIFIER=slow, Node 20.11).
names = ['Klijent A', 'Proces', 'Klijent B']; xs = [170, 520, 870]
body = lifelines(names, xs, bottom=450, w=200)
body += arrow(170, 115, 520, 115, 'POST /orders (t = 0 s)')
body += text(640, 160, 'obavijest traje 3 s', 17, GREY, 400)
body += f'<rect x="440" y="185" width="160" height="40" rx="8" fill="#fff4e5" stroke="#d9a441"/>' + text(520, 211, 'Ctrl+C (t = 1 s)', 17)
body += text(705, 205, 'ne primam nove veze', 17, GREY)
body += arrow(870, 265, 540, 265, 'GET /products', color=RED) + xmark(560, 265) + text(705, 295, 'veza odbijena', 17, RED)
body += arrow(520, 345, 170, 345, '201 + narudžba (t = 3 s)', dash=True)
body += text(520, 400, 'zapis: „Svi zahtjevi dovršeni. Izlazim.” → exit 0', 18)
body += text(520, 480, 'Izmjereno lokalno (Node 20.11): započeti zahtjev dovršen je, novi nije primljen.', 17, GREY)
save('shutdown-timeline', body, 500)

# 8. Two processes, one backpack (measured locally): each process has its own stock in memory.
body = box(40, 30, 230, 70, 'Klijent A') + box(770, 30, 230, 70, 'Klijent B')
for x, port in [(40, 3000), (770, 3001)]:
    body += f'<rect x="{x-10}" y="160" width="250" height="170" rx="14" fill="#fafcfd" stroke="#b8cbd5"/>'
    body += text(x + 115, 192, f'Proces na portu {port}', 19, INK, 600)
    body += text(x + 115, 240, 'ruksak: zaliha 1 → 0', 18) + text(x + 115, 275, 'narudžba id 1', 18) + text(x + 115, 310, 'vlastita memorija', 16, GREY)
body += arrow(155, 102, 155, 152) + arrow(885, 102, 885, 152)
body += f'<text x="170" y="135" font-family="Arial, sans-serif" font-size="18" fill="{BLUE}">POST /orders</text><text x="870" y="135" text-anchor="end" font-family="Arial, sans-serif" font-size="18" fill="{BLUE}">POST /orders</text>'
body += text(520, 245, 'oba vraćaju', 18, GREY) + text(520, 275, '201', 26, RED, 600)
body += f'<rect x="250" y="370" width="540" height="60" rx="10" fill="#fdecee" stroke="{RED}"/>' + text(520, 408, 'Prodana 2 ruksaka, a postoji samo 1.', 21, RED, 600)
body += text(520, 470, 'Stanje koje mora biti zajedničko ne smije živjeti u memoriji jednog procesa.', 18, GREY)
save('two-processes', body, 490)

# 9. Modular monolith: one process, modules with small public interfaces.
body = f'<rect x="20" y="20" width="1000" height="400" rx="18" fill="#fafcfd" stroke="#8aa7b8" stroke-width="2"/>'
body += text(520, 55, 'Jedan proces, jedno pokretanje (monolit)', 21, INK, 600)
mods = [(45, 'Proizvodi', ['handler', 'katalog']), (395, 'Narudžbe', ['handler', 'servis', 'pohrana']), (745, 'Obavijesti', ['notifier'])]
for x, t, parts in mods:
    body += f'<rect x="{x}" y="85" width="250" height="250" rx="14" fill="white" stroke="#c6dbe8" stroke-width="1.5"/>' + text(x + 125, 120, t, 21, INK, 600)
    for i, ptxt in enumerate(parts):
        body += f'<rect x="{x+30}" y="{140+i*58}" width="190" height="44" rx="8" fill="#f3f8fb" stroke="#d4e3ec"/>' + text(x + 125, 168 + i * 58, ptxt, 17)
body += arrow(393, 260, 302, 260) + text(347, 245, 'findById', 15, BLUE) + arrow(647, 260, 738, 260) + text(692, 245, 'orderPlaced', 15, BLUE)
body += text(520, 380, 'Modul drugome nudi nekoliko funkcija; ostalo je njegova unutarnja stvar.', 19)
body += text(520, 455, 'Mape src/products, src/orders i src/notifications u code/02-backend-architecture.', 17, GREY)
save('modular-monolith', body, 475)
