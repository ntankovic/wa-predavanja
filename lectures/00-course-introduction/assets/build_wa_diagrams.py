from pathlib import Path
import subprocess
import sys
D = Path(__file__).parent
sys.path.insert(0, str(D.parents[2] / 'scripts'))
from diagram_style import box, arrow, text, markers

def diagram(name, labels, sub, legend):
    w, h = 1040, 280
    bw, gap, y, bh = 260, 100, 35, 130
    body = markers() + '<rect width="1040" height="280" fill="white"/>'
    for i, (label, detail) in enumerate(zip(labels, sub)):
        x = 30 + i*(bw+gap)
        body += box(x, y, bw, bh, label, detail)
        if i < len(labels)-1:
            body += arrow(x+bw+12, y+bh/2, x+bw+gap-12, y+bh/2)
    body += text(520, 235, legend, 20, '#536b7b')
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">' + body + '</svg>'
    p = D / (name + '.hr.svg')
    p.write_text(svg)
    subprocess.run(['rsvg-convert','-f','pdf','-o',str(p.with_suffix('.pdf')),str(p)],check=True)
diagram('wa-request',['Preglednik','Backend','Baza podataka'],['zahtjev za proizvode','pravila i pristup podacima','pohranjeni proizvodi'],'Strelice pokazuju pozive. Odgovori se vraćaju obrnutim putem.')
diagram('wa-evidence',['Predvidi','Pokaži','Objasni'],['očekivani rezultat','kod i stvarni zahtjev','rezultat i uzrok greške'],'Slijeva nadesno: koraci demonstracije jedne funkcionalnosti na usmenom.')
diagram('wa-change',['Odredi opseg','Promijeni','Provjeri'],['frontend, API, baza','jednu funkcionalnost','rezultat i rubni slučaj'],'Slijeva nadesno: koraci izmjene koda uživo, lokalno na testnim podacima.')
# Explaining a change on one's own code replaces the live code change (lecturer, 2026-10-13); wa-change is kept unused.
diagram('wa-design-change',['Gdje?','Kako?','Posljedice?'],['dijelovi sustava, datoteke','koraci izmjene','greške, stanje, testiranje'],'Slijeva nadesno: objašnjenje dorade na vlastitom kodu, uz potpitanja nastavnika.')

# AI responsibility loop, adapted from the existing attributed course figure.
def ai_responsibility():
    w, h = 1040, 340
    body = markers() + f'<rect width="{w}" height="{h}" fill="white"/>'
    for i, (title, detail) in enumerate([
        ('Vi određujete', 'zahtjeve i arhitekturu'),
        ('AI predlaže', 'kod'),
        ('Vi provjeravate', 'testirate i obrazlažete'),
    ]):
        x = 30 + i*350
        body += box(x, 25, 280, 145, title, detail)
        if i < 2:
            body += arrow(x+292, 97.5, x+338, 97.5)
    body += ('<path d="M870,182 V228 Q870,240 858,240 H182 '
             'Q170,240 170,228 V182" fill="none" stroke="#3886ad" '
             'stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" '
             'marker-end="url(#arrow-blue)"/>')
    body += text(520, 222, 'Vi vodite sljedeću doradu', 20, '#536b7b')
    body += text(520, 305, 'Strelice prikazuju tijek rada i doradu.', 20, '#536b7b')
    p = D / 'ai-responsibility.hr.svg'
    p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">' + body + '</svg>')
    subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', str(p.with_suffix('.pdf')), str(p)], check=True)

ai_responsibility()
