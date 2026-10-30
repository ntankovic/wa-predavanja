"""Editable bilingual SVG figures for introduction slides; no external artwork."""
from pathlib import Path
from html import escape
from math import hypot
ROOT=Path(__file__).parent
BLUE='#1585b4'; DARK='#18344b'; GRAY='#546573'
class Figure:
 def __init__(self,h=400):
  self.h=h; self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{h}" viewBox="0 0 1040 {h}"><defs><marker id="arrow" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="12" refX="12" refY="6" orient="auto"><path d="M1 1 Q0 0 2 1 L12 5.3 Q13 6 12 6.7 L2 11 Q0 12 1 11 L3 6 Z" fill="{BLUE}"/></marker></defs><rect width="1040" height="{h}" fill="white"/>']
 def text(self,x,y,lines,size=25,color=DARK,weight=400,anchor='middle'):
  if isinstance(lines,str):lines=[lines]
  for i,line in enumerate(lines):self.parts.append(f'<text x="{x}" y="{y+i*(size+8)}" text-anchor="{anchor}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(line)}</text>')
 def box(self,x,y,w,h,lines,fill='#edf7fb',size=25):
  self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{BLUE}" stroke-width="2"/>')
  n=1 if isinstance(lines,str) else len(lines);self.text(x+w/2,y+h/2-(n-1)*(size+8)/2+size*.34,lines,size)
 def arrow(self,points,label=None,lx=0,ly=0):
  path = f'M {points[0][0]} {points[0][1]}'
  for i in range(1, len(points)-1):
   previous, corner, following = points[i-1], points[i], points[i+1]
   incoming = hypot(corner[0]-previous[0], corner[1]-previous[1])
   outgoing = hypot(following[0]-corner[0], following[1]-corner[1])
   if not incoming or not outgoing:
    continue
   radius = min(9, incoming/2, outgoing/2)
   before = [corner[j] + (previous[j]-corner[j])*radius/incoming for j in (0,1)]
   after = [corner[j] + (following[j]-corner[j])*radius/outgoing for j in (0,1)]
   path += f' L {before[0]} {before[1]} Q {corner[0]} {corner[1]} {after[0]} {after[1]}'
  path += f' L {points[-1][0]} {points[-1][1]}'
  self.parts.append(f'<path d="{path}" fill="none" stroke="{BLUE}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow)"/>')
  if label:self.text(lx,ly,label,20,GRAY)
 def line(self,x1,y1,x2,y2):self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{BLUE}" stroke-width="3"/>')
 def save(self,name,lang):
  # Current Croatian AI figure is maintained in build_wa_diagrams.py.
  if name == 'ai-responsibility' and lang == 'hr': return
  (ROOT/f'{name}.{lang}.svg').write_text(''.join(self.parts)+'</svg>')
for lang in ['hr','en']:
 def tr(hr,en):return hr if lang=='hr' else en
 # Attendance: process and discussion, without inventing form fields or attendance rules.
 f=Figure(340)
 steps=[tr(['Otvorite poveznicu','ili skenirajte QR'],['Open the link','or scan the QR']),tr(['Evidentirajte','prisutnost'],['Record','your presence']),tr(['Sudjelujte','u raspravi'],['Join','the discussion'])]
 for i,lines in enumerate(steps):
  x=35+i*345;f.text(x+135,52,str(i+1),30,BLUE,700);f.box(x,82,270,110,lines)
  if i<2:f.arrow([(x+270,137),(x+330,137)])
 f.text(520,258,tr('Pitajte · usporedite alternative · objasnite odluke','Ask questions · compare alternatives · explain decisions'),25)
 f.text(520,310,tr('Strelice prikazuju redoslijed koraka.','Arrows show the order of steps.'),18,GRAY);f.save('attendance-explained',lang)
 # Practical work: two distinct concrete flows.
 f=Figure(410);f.text(25,34,tr('Mikroservisi: tok zahtjeva','Microservices: request flow'),27,DARK,700,'start')
 for x,lines in [(35,tr('Klijent','Client')),(390,tr('Usluga A','Service A')),(745,tr('Usluga B','Service B'))]:f.box(x,65,260,78,lines)
 f.arrow([(295,104),(385,104)]);f.arrow([(650,104),(740,104)]);f.text(520,178,tr('Prikazani su zahtjevi; odgovori su izostavljeni.','Requests are shown; replies are omitted.'),19,GRAY)
 f.text(25,228,tr('Analiza podataka: podijeli, obradi, objedini','Data analysis: split, process, combine'),27,DARK,700,'start')
 f.box(35,275,235,80,tr('Podaci','Data'));f.box(400,255,225,60,tr('Proces 1','Process 1'));f.box(400,335,225,60,tr('Proces 2','Process 2'));f.box(765,290,240,80,tr('Rezultat','Result'))
 for y in [285,365]: f.arrow([(270,315),(330,315),(330,y),(395,y)]);f.arrow([(625,y),(695,y),(695,330),(760,330)])
 f.save('practical-work',lang)
 # AI ownership loop.
 f=Figure(290)
 boxes=[tr(['VI određujete','zahtjeve i arhitekturu'],['YOU set requirements','and choose architecture']),tr(['AI predlaže','kod'],['AI proposes','code']),tr(['VI provjeravate,','testirate i obrazlažete'],['YOU review, test,','and justify choices'])]
 for i,lines in enumerate(boxes):
  x=15+i*350;f.box(x,35,310,120,lines,size=23)
  if i<2:f.arrow([(x+310,95),(x+340,95)])
 f.arrow([(870,155),(870,225),(170,225),(170,160)]);f.text(520,212,tr('Vi vodite sljedeću doradu','You guide the next revision'),22,GRAY)
 f.text(520,280,tr('Strelice prikazuju tijek rada i doradu.','Arrows show the workflow and revision loop.'),18,GRAY);f.save('ai-responsibility',lang)
 # Course passing: two parallel inputs and alternative completion paths.
 f=Figure(450)
 f.box(15,30,230,80,tr(['Prijavite projekt','i radite na njemu'],['Register a project','and work on it']),size=22)
 f.box(15,145,230,80,tr(['Skupljajte bodove','na vježbama'],['Collect points','in practical classes']),size=22)
 f.arrow([(245,70),(275,70),(275,128),(310,128)]);f.arrow([(245,185),(275,185),(275,128)])
 f.box(315,85,240,85,tr(['Predajte','projekt'],['Submit','the project']))
 f.arrow([(555,128),(605,128)])
 f.box(610,65,405,125,tr(['Nastavnik odlučuje o oslobođenju','Prijavite ispitni rok na oba puta'],['Lecturer decides exemption','Register for an exam date either way']),size=22)
 f.arrow([(815,190),(815,245),(675,245),(675,278)],tr('Nema oslobođenja','Not exempt'),805,230)
 f.arrow([(1015,130),(1030,130),(1030,330),(1010,330)],tr('Oslobođeni','Exempt'),953,263)
 f.box(525,283,290,94,tr(['Rezervirajte obranu','Obrana i usmeni ispit'],['Book the defence','Defence + oral exam']),size=22)
 f.box(865,290,145,80,tr(['Ocjena','u ISVU'],['Grade','in ISVU']),size=22)
 f.arrow([(815,330),(860,330)]);f.text(839,305,tr('Prolaz','Pass'),17,GRAY)
 f.arrow([(575,377),(575,418),(370,418),(370,210),(650,210),(650,195)],None)
 f.text(250,348,tr(['Neuspjeh: ponovno','prijavite ispitni rok'],['Unsuccessful: register','for another exam date']),21,GRAY)
 f.text(520,436,tr('Strelice prikazuju slijed; dvije početne grane teku paralelno.','Arrows show sequence; the first two branches run in parallel.'),18,GRAY)
 f.save('course-completion',lang)
 # Deadlines use constraints, no invented calendar dates or equal spacing.
 f=Figure(230)
 f.text(15,28,tr('PREDAJA I OBRANA','SUBMISSION AND DEFENCE'),20,BLUE,700,'start')
 for x,label in [(15,tr('Predaja','Submission')),(425,tr('Obrana','Defence')),(835,tr('Ispitni rok','Exam date'))]:f.box(x,60,190,64,label,size=23)
 f.arrow([(205,92),(420,92)],tr('≥ 3 radna dana','≥ 3 working days'),315,65)
 f.arrow([(615,92),(830,92)],tr('najkasnije do','no later than'),725,65)
 f.text(15,184,tr('REZERVACIJE','BOOKING'),20,BLUE,700,'start')
 f.text(230,184,tr('Termini postaju dostupni 10 dana unaprijed.','Appointments become available 10 days in advance.'),23,DARK,400,'start')
 f.text(520,225,tr('Uvjeti vremena; razmaci nisu u mjerilu.','Timing constraints; spacing is not to scale.'),18,GRAY);f.save('deadlines',lang)
