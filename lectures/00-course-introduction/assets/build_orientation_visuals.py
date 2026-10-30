from pathlib import Path
from html import escape
import subprocess
D=Path(__file__).resolve().parent
def svg(name,body,w=100,h=100):
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'+body+'</svg>'
 p=D/(name+'.svg');p.write_text(s)
 subprocess.run(['rsvg-convert','-f','pdf','-o',str(p.with_suffix('.pdf')),str(p)],check=True)
def t(x,y,v,size=22,color='#20384d',weight=400):
 return f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(v)}</text>'
# Original simplified visual identifiers; not official logo files.
svg('tech-js','<rect x="6" y="6" width="88" height="88" rx="16" fill="#f7df1e"/>'+t(28,73,'JS',44,'#242424',700))
svg('tech-vue','<path d="M5 15 H25 L50 58 75 15 H95 L50 93Z" fill="#42b883"/><path d="M25 15 H40 L50 32 60 15 H75 L50 58Z" fill="#35495e"/>')
svg('tech-pinia','<path d="M48 32 Q22 14 28 6 Q46 9 49 24 Q49 5 62 3 Q67 19 58 29 Q75 15 82 21 Q77 37 60 40Z" fill="#59a86d"/><rect x="22" y="30" width="57" height="64" rx="26" fill="#ffd665" stroke="#e9ad32" stroke-width="2"/><path d="M31 43 L68 81 M28 61 L55 88 M49 37 L74 63 M70 42 L34 82 M75 59 L50 89 M50 36 L27 61" stroke="#e9b343" stroke-width="2"/><circle cx="41" cy="57" r="3" fill="#35495e"/><circle cx="61" cy="57" r="3" fill="#35495e"/><path d="M46 65 Q51 70 56 65" fill="none" stroke="#35495e" stroke-width="2"/>')
svg('tech-firebase','<path d="M20 78 L30 9 50 47 61 25 82 80 51 96Z" fill="#ffca28"/><path d="M20 78 L50 47 61 25 69 58 51 96Z" fill="#ffa000"/><path d="M20 78 L78 16 82 80 51 96Z" fill="#f57c00"/>')
svg('tech-http','<rect x="5" y="14" width="90" height="72" rx="14" fill="#e4eff7"/>'+t(17,44,'HTTP',23,'#2d6688',700)+'<path d="M22 58 H77 L69 51 M77 68 H22 L30 75" fill="none" stroke="#3886ad" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
body='<rect x="1" y="1" width="1038" height="358" rx="16" fill="#fff" stroke="#d4e3ec"/><path d="M1 55 H1039" stroke="#d4e3ec"/>'
body+=t(24,36,'projekt / Povijest commitova',24,weight=700)+t(688,36,'Ilustrativni primjer · 6 commitova',18,'#637585')
rows=[('Ana','A','Dodaje prikaz proizvoda','a31f902','#dceef9'),('Marko','M','Sprema narudžbu u bazu','b62e140','#e3f2e8'),('Iva','I','Provjerava unos narudžbe','c83a215','#f1e8fa'),('Ana','A','Ispravlja prikaz prazne košarice','d94b326','#dceef9'),('Marko','M','Dodaje provjeru zalihe','e15c437','#e3f2e8'),('Ana','A','Dodaje poruku o pogrešci','f26d548','#dceef9')]
for i,(name,initial,msg,sha,color) in enumerate(rows):
 y=83+i*44
 body+=f'<circle cx="38" cy="{y-6}" r="15" fill="{color}"/>'+t(32,y,initial,16,weight=700)+t(65,y,name,18,weight=700)+t(154,y,msg,18)+t(569,y,sha,16,'#637585')
body+='<path d="M681 71 V333" stroke="#d4e3ec"/>'+t(711,91,'Commitovi po autoru',20,weight=700)
for i,(name,count,color) in enumerate([('Ana',3,'#3886ad'),('Marko',2,'#58a074'),('Iva',1,'#9d7abe')]):
 y=132+i*65
 body+=t(711,y,name,20)+t(981,y,str(count),20,weight=700)+f'<rect x="711" y="{y+10}" width="290" height="10" rx="5" fill="#edf2f6"/><rect x="711" y="{y+10}" width="{count*90}" height="10" rx="5" fill="{color}"/>'
svg('github-history.hr',body,1040,360)

body=t(22,31,'Primjer: ispit u srijedu → predaja najkasnije prethodni petak',24,weight=700)
days=[('PET','3','PREDAJA','#dfedf5'),('SUB','—','ne broji se','#f0f1f3'),('NED','—','ne broji se','#f0f1f3'),('PON','2','radni dan','#e7f2eb'),('UTO','1','radni dan','#e7f2eb'),('SRI','ISPIT','ispitni rok','#dfedf5')]
for i,(day,count,label,color) in enumerate(days):
 x=22+i*169
 body+=f'<rect x="{x}" y="61" width="151" height="151" rx="14" fill="{color}"/>'
 body+=t(x+16,91,day,20,weight=700)+t(x+16,148,count,34,weight=700)+t(x+16,190,label,17)
body+=t(22,253,'Brojimo unatrag: utorak 1 → ponedjeljak 2 → petak 3.',22)
body+=t(22,287,'Subotu i nedjelju preskačemo. Primjer je bez blagdana.',20,'#637585')
svg('submission-calendar.hr',body,1040,310)

# Dates supplied by the lecturer; calendar cards do not imply exam availability.
body='<rect width="1040" height="210" fill="white"/>'
for x,accent,bg,date,title,detail in [
 (10,'#ad7840','#fcf5e9','20. 7. – 25. 8.','Godišnji odmor nastavnika','Planirajte komunikaciju i završetak projekta.'),
 (540,'#3886ad','#f3f8fb','30. 9.','Završetak akademske godine','Projekt treba obraniti u tekućoj ak. godini.')]:
 body+=f'<rect x="{x}" y="12" width="490" height="180" rx="16" fill="{bg}" stroke="#d4e3ec"/>'
 body+=f'<rect x="{x+22}" y="37" width="42" height="40" rx="6" fill="none" stroke="{accent}" stroke-width="2.5"/><path d="M{x+22} 49 H{x+64} M{x+32} 31 V42 M{x+54} 31 V42" fill="none" stroke="{accent}" stroke-width="2.5" stroke-linecap="round"/>'
 body+=t(x+83,68,date,32,accent,700)+t(x+22,116,title,25,weight=700)+t(x+22,156,detail,20,'#536b7b')
svg('academic-year.hr',body,1040,210)
