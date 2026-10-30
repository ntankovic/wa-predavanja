from pathlib import Path
from html import escape
import subprocess,sys
D=Path(__file__).resolve().parent
sys.path.insert(0,str(D.parents[2]/'scripts'))
from diagram_style import text,box,arrow,markers

def save(name,b,h):
 p=D/(name+'.hr.svg');p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{h}" viewBox="0 0 1040 {h}">'+markers()+f'<rect width="1040" height="{h}" fill="white"/>'+b+'</svg>');subprocess.run(['rsvg-convert','-f','pdf','-o',str(p.with_suffix('.pdf')),str(p)],check=True)
b=box(20,15,240,66,'Preglednik')+box(780,15,240,66,'Poslužitelj')
b+=arrow(140,136,900,136,'Zahtjev: Accept: application/json')
b+=text(520,170,'„Kao odgovor prihvaćam JSON.”',22,'#536b7b')
b+=arrow(900,240,140,240,'Odgovor: Content-Type: application/json',dash=True)
b+=text(520,279,'Tijelo odgovora: {"products": []}',23)
b+=text(520,321,'Content-Type opisuje tijelo i u zahtjevu, ako ga šaljemo.',21,'#536b7b')
save('http-content-types',b,340)
b=text(520,30,'Proizvod #7: cijena u bazi 100 € · kupac šalje cijenu 1 €',25,weight=600)
for x,title,color,bg,lines in [(10,'LOŠA PRAKSA','#b63842','#fff4f3',['Klijent šalje: proizvod 7, količina 1, cijena 1 €','Backend prihvaća poslanu cijenu.','Narudžba: 1 × 1 € = 1 €','Posljedica: trgovina gubi 99 €.']), (535,'DOBRA PRAKSA','#277b59','#f1f8f4',['Klijent bira proizvod 7 i količinu 1.','Backend provjerava unos; cijenu čita iz baze.','Narudžba: 1 × 100 € = 100 €','Izmijenjena cijena ne određuje iznos.'])]:
 b+=f'<rect x="{x}" y="58" width="495" height="270" rx="16" fill="{bg}" stroke="{color}" stroke-opacity=".3"/>'
 b+=text(x+247,92,title,22,color,600)
 for i,line in enumerate(lines):b+=text(x+247,137+i*52,line,19,color if i==3 else '#20384d',600 if i==2 else 400)
 b+=arrow(x+247,150,x+247,167,color=color if color=='#b63842' else '#3886ad')
b+=text(520,365,'Klijent bira što želi. Backend provjerava pravila i računa cijenu.',23,weight=600)
save('webshop-price-trust',b,390)
