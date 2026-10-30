"""Original editable program/process/server diagram; SVG and vector PDF share geometry."""
from pathlib import Path
import subprocess
import sys
D = Path(__file__).parent
sys.path.insert(0, str(D.parents[2] / 'scripts'))
from diagram_style import text, box, arrow, markers

W, H = 1040, 460
body = f'<rect x="250" y="20" width="770" height="345" rx="14" fill="#fafcfd" stroke="#b8cbd5" stroke-width="1.5"/>'
body += text(635, 54, 'Računalo: CPU, memorija i disk', 20, '#536b7b', 600)
body += box(25, 150, 200, 100, 'Preglednik', 'GET /products')
body += box(275, 150, 180, 100, 'Proxy', 'javna adresa (URL)')
body += box(520, 75, 250, 110, 'Proces A', 'port 3000 · vlastita memorija')
body += box(520, 215, 250, 110, 'Proces B', 'port 3001 · vlastita memorija')
body += box(830, 150, 170, 100, 'Program', 'server.mjs na disku')
body += arrow(225, 200, 268, 200)
body += arrow(455, 185, 512, 135) + arrow(455, 215, 512, 265)
body += arrow(830, 185, 778, 135, dash=True) + arrow(830, 215, 778, 265, dash=True)
body += text(645, 352, 'Uloga poslužitelja: proces sluša i obrađuje zahtjeve.', 18, '#536b7b')
body += text(520, 405, 'Pune strelice: zahtjev. Isprekidane: pokretanje programa (npm start).', 19)
body += text(520, 442, 'Isti URL može doći do bilo kojeg procesa; procesi ne dijele memoriju.', 22)

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
       f'{markers()}<rect width="{W}" height="{H}" fill="white"/>{body}</svg>')
p = D / 'process-server.hr.svg'
p.write_text(svg)
subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', str(p.with_suffix('.pdf')), str(p)], check=True)

# Program vs process on one computer, without proxy (introduced before the proxy slide).
W2, H2 = 1040, 490
b = '<rect x="15" y="10" width="1010" height="395" rx="14" fill="#fafcfd" stroke="#b8cbd5" stroke-width="1.5"/>'
b += text(520, 40, 'Jedno računalo', 21, '#536b7b', 600)
b += '<rect x="35" y="55" width="255" height="330" rx="12" fill="white" stroke="#c6dbe8" stroke-dasharray="6 5"/>'
b += text(162, 82, 'Disk: datoteke', 19, '#536b7b', 600)
b += '<rect x="330" y="55" width="675" height="330" rx="12" fill="white" stroke="#c6dbe8" stroke-dasharray="6 5"/>'
b += text(667, 82, 'Radna memorija: procesi koji se izvršavaju', 19, '#536b7b', 600)
b += box(50, 165, 225, 120, 'Program', 'server.mjs · zapisan kod, sam ne radi ništa')
b += box(355, 100, 300, 120, 'Proces A: node', 'port 3000 · vlastiti podaci u memoriji')
b += box(355, 250, 300, 120, 'Proces B: node', 'port 3001 · vlastiti podaci u memoriji')
b += box(745, 100, 240, 120, 'Preglednik', 'i on je proces')
b += box(745, 250, 240, 120, 'Terminal: nc', 'i on je proces')
b += arrow(275, 205, 347, 165, dash=True) + arrow(275, 245, 347, 305, dash=True)
b += arrow(745, 160, 663, 160) + arrow(745, 310, 663, 160)
b += text(520, 440, 'Isprekidane strelice: pokretanje (npm start, zatim PORT=3001 npm start).', 19)
b += text(520, 472, 'Pune strelice: zahtjev na port 3000 stiže samo procesu A.', 19)
svg2 = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W2}" height="{H2}" viewBox="0 0 {W2} {H2}">'
        f'{markers()}<rect width="{W2}" height="{H2}" fill="white"/>{b}</svg>')
p2 = D / 'program-process.hr.svg'
p2.write_text(svg2)
subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', str(p2.with_suffix('.pdf')), str(p2)], check=True)
