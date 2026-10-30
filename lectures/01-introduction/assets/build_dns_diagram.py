from pathlib import Path
import sys,subprocess
D=Path(__file__).resolve().parent
sys.path.insert(0,str(D.parents[2]/'scripts'))
from diagram_style import box,arrow,text,markers
b=markers()+'<rect width="1040" height="320" fill="white"/>'
for x,label in [(20,'Naše računalo'),(390,'DNS resolver'),(760,'Web poslužitelj')]:
 b+=box(x,10,260,62,label)
 b+=f'<path d="M{x+130} 82 V282" stroke="#d4e3ec" stroke-width="2" stroke-dasharray="4 5"/>'
b+=arrow(150,120,520,120,'1. Koja je IP adresa za ime?')
b+=arrow(520,184,150,184,'2. IP adresa odredišta',dash=True)
b+=arrow(150,258,890,258,'3. Povezivanje s dobivenom adresom i HTTP razmjena')
b+=text(520,311,'DNS upit treba samo ako odgovor već nije spremljen. /products nije dio DNS upita.',19,'#536b7b')
p=D/'dns-lookup.hr.svg';p.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="320" viewBox="0 0 1040 320">'+b+'</svg>')
subprocess.run(['rsvg-convert','-f','pdf','-o',str(p.with_suffix('.pdf')),str(p)],check=True)
