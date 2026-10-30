"""Conceptual remote-data retrieval; not Firebase's internal protocol."""
from pathlib import Path
import sys, subprocess
D=Path(__file__).resolve().parent
sys.path.insert(0,str(D.parents[2]/'scripts'))
from diagram_style import box, arrow, text, markers
body=markers()+'<rect width="1040" height="310" fill="white"/>'
body+='<rect x="10" y="10" width="610" height="247" rx="18" fill="#fafcfe" stroke="#cbdce7"/>'
body+=text(315,45,'V PREGLEDNIKU'.replace('V P','U P'),20,'#536b7b',600)
body+=text(891,45,'NA POSLUŽITELJU',20,'#536b7b',600)
body+=box(30,78,230,148,'Naš JavaScript','klik i prikaz podataka')
body+=box(370,78,230,148,'Firebase SDK','biblioteka u pregledniku')
body+=box(770,78,260,148,'Firebase usluga','udaljena obrada i podaci')
body+=arrow(271,127,359,127)+text(315,112,'poziv',17,'#3886ad')
body+=arrow(359,191,271,191,dash=True)+text(315,176,'rezultat',17,'#3886ad')
body+=arrow(632,127,758,127)+text(695,112,'dohvat',17,'#3886ad')
body+=arrow(758,191,632,191,dash=True)+text(695,176,'podaci',17,'#3886ad')
body+=text(520,290,'Kad trebamo podatke s poslužitelja, biblioteka obavlja komunikaciju za nas.',21,'#536b7b')
p=D/'firebase-bridge.hr.svg';p.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="310" viewBox="0 0 1040 310">'+body+'</svg>')
subprocess.run(['rsvg-convert','-f','pdf','-o',str(p.with_suffix('.pdf')),str(p)],check=True)
