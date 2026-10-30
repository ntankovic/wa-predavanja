# Current Web Applications review — 2026-10-06

The records below are archived source-course history, not current Web Applications decisions. The adapted Croatian deck uses no inherited course-specific diagrams or external images. Original assets remain preserved, unused. The shared FIPU branding is retained. Current checks and unresolved items are in README.md. English remains the inherited deck pending Croatian review.

---

# Introduction illustrations

## Course completion process

- Purpose: show parallel project/practical-class work, oral-exam exemption, defence, and the retry path after an unsuccessful exam.
- Source: lecturer-supplied Croatian `assets/hodogram_rs.png`, 2026-09-17; unchanged original. Supporting editable BPMN retained as `assets/hodogram-original.bpmn`.
- Placement: immediately after the plain-language process overview. This lecture has no chapter PDF by design.
- Dense annotations remain in the original; the HTML image opens in a lightbox for closer reading. Speaker notes explain the arrows, gateways, conditions, and deadlines.
- Review: verify HTML rendering and enlarged image. The original PNG is the full-resolution artifact for separate inspection or printing.

## Presence check-in

Shared slide 2 embeds `assets/shared/attendance-qr.svg`. The lecturer supplied the target URL. The check-in and welcome share the opening minute.

## Prijedlozi za doradu, 2026-09-17

Status: prioritetni dijagrami izrađeni i umetnuti 2026-09-17; fotografija ostaje neobvezan prijedlog. Brojevi se odnose na trenutačni raspored od 15 slajdova. Izvori: [zajednički popis](../../references/visual-sources.md). Najprije doraditi tri vizuala s najvećom nastavnom vrijednošću: pregled polaganja, rokove i odgovornost pri uporabi AI-ja.

| Prioritet | Slajd | Prijedlog i nastavna svrha | Izvedba i smještaj |
| --- | --- | --- | --- |
| 1 | 10 — How to pass the course: overview | Pojednostavljen dijagram: projekt i bodovi s vježbi odvijaju se paralelno; nakon predaje nastavnik odlučuje o oslobođenju; prijava ispitnog roka potrebna je na oba puta; slijedi unos ocjene ili obrana i usmeni. Prikazati povratak na prijavu nakon negativnog ishoda. | Izvorni SVG prema nastavnikovu BPMN-u, umjesto postojećeg popisa. Oznake strelica i odluka moraju biti izričite. Na slajdu 11 ostaje cjelovit izvorni BPMN. Ne prikazati oslobođenje kao automatsko. |
| 1 | 12 — Submission, exemption, and defence | Vizualni prikaz rokova: termin postaje dostupan 10 dana unaprijed; predaja najmanje 7 dana prije ispitnog roka; obrana najmanje 3 radna dana nakon predaje, a najkasnije na dan roka. Razlikovati ispitni rok od termina obrane. | Izvorni SVG s dvjema povezanim vremenskim crtama ili označenim intervalima, umjesto dugih rečenica o rokovima. Ne pretvarati radne dane u kalendarske. Dostupnost termina ne vezati automatski uz datum ispitnog roka. Uvjeti oslobođenja ostaju jasno vidljivi uz prikaz. |
| 1 | 14 — AI use and your responsibility | Student postavlja zahtjeve i bira arhitekturu; AI predlaže kod; student pregledava, testira i obrazlaže odluke. Povratna strelica pokazuje doradu. Naglasak: student vodi i može objasniti izbor. | Izvorni SVG s tri koraka i povratnom vezom. Zadržati pravilo o dopuštenim tehnologijama i završnu rečenicu o informiranim odlukama. Bez generičke slike robota. |
| 2 | 6 — From lectures to practical work | Dva mala primjera: klijent i dvije povezane usluge; skup podataka podijeljen radnicima pa objedinjeni rezultat. Objašnjavaju što studenti konkretno implementiraju. | Izvorni SVG, kratke hrvatske oznake prije prijevoda. Zamijeniti dva tekstualna primjera dijagramima; označiti tok zahtjeva odnosno podataka. Prikaz je primjer, ne obvezna projektna arhitektura. |
| 3 | 4 — What this course is about | Jedna fotografija stvarne poslužiteljske opreme uz kratko pitanje: koje komponente surađuju i što se događa kad jedna otkaže? Fotografija daje stvarni kontekst. | Unsplash ili Pexels; pojmovi za ručnu pretragu: “server racks”, “data centre”. Fotografija desno, sažeti ciljevi lijevo. Ne sugerirati da raspodijeljeni sustavi postoje samo u podatkovnim centrima; nije zamjena za dijagram komunikacije. |

### Gdje ne dodavati ilustracije

- Naslov i QR slajd već imaju jasnu vizualnu funkciju.
- Tablicu nastavnika, programske preduvjete i poveznice zadržati jednostavnima.
- Ne dodavati nasumične ikone svakoj stavci ni stock fotografije uz pravila polaganja.
- unDraw ostaje opcija za potrebnu konceptualnu scenu, ali u ovoj prezentaciji konkretni dijagrami daju više nastavne vrijednosti.

### Provjera prije primjene

Ovo su vizualne zamjene unutar postojećih slajdova; zadržati 15 slajdova i 20 minuta. Sačuvati izvorni BPMN i pripisati izvedene dijagrame nastavnikovu izvoru. Nove oznake najprije napisati na hrvatskom, zatim prevesti nakon pregleda. Dodati alternativni tekst; provjeriti čitljivost i rubove u HTML-u te eventualnom PDF izvozu slajdova. Predavanje 00 nema poglavlje u knjizi ni zaseban PDF poglavlja.

## Izvedeno 2026-09-17

Pet izvornih dijagrama: `practical-work`, `attendance-explained`, `course-completion`, `deadlines`, `ai-responsibility`. Svaki ima hrvatski i engleski SVG te vektorski PDF u `assets/`. Uredivi zajednički izvor: `assets/build_diagrams.py`. Hrvatski nazivi prethode engleskima u izvoru; engleske oznake ostaju za jezični pregled nastavnika.

- Slajd 8: otvaranje poveznice ili QR-a, evidencija prisutnosti, sudjelovanje u raspravi. Ne uvodi obvezni dolazak niti izmišljene korake obrasca.
- Slajdovi 6, 10, 12 i 14 zamjenjuju dio teksta dijagramima iz gornjeg plana.
- Izvorni BPMN na slajdu 11 sačuvan; uz njega ostaje ispravak na 3 radna dana.
- Plan ostaje 15 slajdova / 20 minuta. Slajd 2 zadržava zajednički QR.
- Fotografija nije dodana: ovaj prolaz daje prednost objašnjenju procesa.

2026-09-17 — Nastavnik je zatražio uklanjanje pojednostavljenog pregleda polaganja. `course-completion` više se ne koristi u prezentaciji; izvorni BPMN ostaje jedini dijagram polaganja. Objašnjenje prisutnosti premješteno je na slajd 2, ispred QR-a na slajdu 3, bez URL-a, uz potvrdu da dolazak nije obvezan. Trenutačno 14 slajdova / 20 minuta.

## Stock artwork applied, 2026-09-17

Attendance now uses unDraw Teaching instead of the three-step attendance diagram, with optional attendance stated explicitly. Course goals use the imgix server-rack photo from Unsplash. Course information uses unDraw Online learning and the official YouTube icon linked to the playlist. Source links, licenses, originals, and modifications are recorded in `sources.md`. All assets are embedded in the standalone HTML. Timing and slide count unchanged.

## Current attendance QR — 2026-10-06

`assets/attendance-wa.png`: original image supplied by lecturer, copied unchanged. Attendance slide, right column, clickable image and text link to https://bit.ly/wa-tu-sam. Source provenance in sources.md. This supersedes the earlier no-images description for the current Croatian draft. HTML/PDF visual QA pending missing Quarto.

2026-10-06 — Lecturer approved matching RS 00 layout. Restored separate large QR slide and attendance illustration, reused existing attributed AI artwork; added original editable request/evidence/live-change SVGs with vector PDF derivatives in assets/build_wa_diagrams.py. 17 slides, 20 minutes. Previously recorded 16-slide counts are superseded.

2026-10-06 — Unified original Croatian box-and-arrow diagrams using `scripts/diagram_style.py`: pale cards, subtle borders, consistent padding, aligned title/subtitle areas and rounded arrowheads. Lecture generators remain editable sources; regenerated SVG and vector PDF derivatives. Representative SVG and PDF renders inspected; HTML builds pass, full browser review remains blocked by Chrome startup failure.

2026-10-06 — Restyled the Croatian AI responsibility loop with the shared card/arrow style. Content and original attribution retained; current editable source is `assets/build_wa_diagrams.py`. Archived generator no longer overwrites this Croatian asset. SVG and PDF inspected visually; all box-and-arrow figures referenced by current HR slides 00/01 now use the shared style. HTML rebuilt with `just slides 00-course-introduction hr`; browser QA remains pending the headless runtime installation.

2026-10-07 — Lecturer supplied 30 September academic-year end and 20 July–25 August annual leave. Original calendar-card illustration `assets/academic-year.hr.svg` / `.pdf`, editable in `assets/build_orientation_visuals.py`; placed on the existing repeat-project slide. Timing unchanged.

2026-10-07 — Shared diagram style refined with layered subtle shadows, restrained blue accent, lighter border and compact filled arrowheads; all current shared-style SVG/PDF diagrams regenerated.

2026-10-07 — Lecturer requested more prominent connectors: shared arrows 3.2 px, 18 px markers; inset 5 px card accents. Three-step orientation cards reduced to 260×130 with 100 px gaps. SVG/PDF assets regenerated; request and sequence diagrams inspected.
