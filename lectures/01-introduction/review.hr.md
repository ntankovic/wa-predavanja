# Pregled narativa — 2026-10-06

Pregledani su cijeli hrvatski slajdovi, skripta, govorne bilješke, vremenski plan, oznake dijagrama i demonstracijski kod. Polazište: studenti poznaju frontend i korištenje Firebase biblioteke, ali ne HTTP/TCP ni vlastiti backend. Status ostaje drafting; ovo nije predavačevo odobrenje.

## Nalazi i ispravci

| Problem | Ispravak |
| --- | --- |
| Početno pitanje očekivalo je stručne nazive prije poučavanja. | Prihvaćaju se odgovori običnim riječima: pokretanje dohvata, primitak podataka, prikaz. |
| Backend i SDK bili su prešutno poznati. | Objašnjeni uz poznati Firebase poziv. |
| Zaglavlje, tijelo i status pojavili su se bez uvoda. | Dodana kratka objašnjenja uz prve stvarne poruke; statusi najprije 200/404/503, zatim skupine. |
| URL odjeljak prerano je uvodio port, fragment i parametre. | Prvi prolaz ograničen na način pristupa, ime odredišta i putanju; port slijedi uz vezu. |
| Prijelaz DummyJSON → lokalni model bio je samo u bilješkama. | Na slajdu je izričit prijelaz i razlika objekt.products nasuprot lokalnom nizu. |
| Proxy je bio na početnoj karti prije objašnjenja. | Početna karta ima preglednik, backend i bazu. Proxy se uvodi prije četverodijelnog slijeda. |
| Node.js, proces, ruta i handler bili su korišteni prerano. | Objašnjeni prije analize koda. Konceptualni handler više ne uvodi repository/validateLimit/publicProducts bez objašnjenja. |
| fetch i Vue .value pretpostavljali su dodatno znanje. | Objašnjeni fetch, GET, await i json(); kod koristi obične varijable stanja, uz navedeni asinkroni kontekst. |
| Ispravak dohvata bio je udaljen od naivnog primjera. | Sada slijede naivan dohvat → stanja → ispravak → lokalna demonstracija. |
| Sesija se pojavljivala prije objašnjenja. | Cookie i primjer prijave uvode sesiju prije stateless i trajne veze. |
| DNS/TCP/TLS/TTFB te autentikacija/autorizacija bili su previše zgusnuti. | Dodana prva objašnjenja; CORS koristi obične riječi za identitet i dopuštenja. QUIC/UDP ostaju dodatna napomena u skripti. |
| Izmišljene vremenske vrijednosti i model arhitekture mogli su izgledati kao mjerenje stvarne usluge. | Vrijednosti su izričito izmišljene; karta opisuje nastavni model, ne unutrašnjost DummyJSON-a. |
| Bilješke i izvori koristili su stare redne brojeve. | Bilješke i tablica izvora povezuju stabilne oznake odjeljaka. |
| Fastify je bio neodlučeni izbor prikazan na 00. | Uklonjena rečenica s 00; izbor frameworka ostaje otvoren, pitanja za usmeni navode Express. |

## Konačna priča

Poznati Firebase poziv → zahtjev i odgovor → čitanje javnog HTML/JSON odgovora → vlastiti backend i njegove funkcije → pogrešan i poboljšani dohvat → četiri opažena ishoda → pronalaženje odredišta, veza i zaštita → posrednik → cijeli put poruke → stanje, sesija i veza → dijagnostika → prijedlog operacije naručivanja.

Svaka nova skupina pojmova ima konkretan razlog: pročitati poruku, razumjeti kod, pronaći odredište, povezati zahtjeve ili objasniti neuspjeh. Završni zadatak uvodi novu potrebu (narudžbu), bez očekivanja već poznatih transakcija ili zaštite od ponavljanja.

## Provjere i granice

- Prošla strukturna provjera: 39 istovjetno poredanih odjeljaka skripte/slajdova; 42 ukupna slajda, 38 sadržajnih; 119 minuta bez vremenskih praznina.
- Svaki sadržajni slajd povezan je sa stabilnim odjeljkom skripte; skripta sadrži odgovarajuće nastavničke vremenske oznake.
- Uspješni `just slides 00-course-introduction hr`, `just slides 01-introduction hr` i `just lecture 01-introduction hr` uz lokalni XeLaTeX.
- Ponovno provjereni službeni izvori za fetch, cookie i TTFB; detalji u sources.md.
- Potpuna vizualna provjera aktualnog HTML-a nije završena: headless Chrome je u prethodnoj provjeri završio sa SIGABRT. Desktop se prema predavačevoj uputi ne koristi. Raniji PDF slajdova i ranije QA snimke ne predstavljaju aktualnu verziju; mjerodavni su aktualni HTML i PDF skripte.
- 119 minuta je plan; prvo izvođenje treba potvrditi tempo. Skraćeni put za 90 minuta opisan je u briefu, ali nije zasebno izvezen.
- Predavačev pregled, izbor frameworka i engleski prijevod ostaju otvoreni. Nije potrebno odlučiti Express/Fastify da bi se izvelo predavanje 01: lokalni demo koristi ugrađeni Node.js HTTP modul.

2026-10-07 — Moved existing DNS section directly after URL/address in chapter and slides; introduced domain name, FQDN and IP, illustrated resolver lookup/cache and separate subsequent web connection. Original SVG/PDF source: assets/build_dns_diagram.py. Timings reordered, total unchanged at 119 min / 42 slides. Sources read: MDN DNS https://developer.mozilla.org/en-US/docs/Glossary/DNS and RFC 8499 §2 https://www.rfc-editor.org/rfc/rfc8499.html (FQDN terminology). No current IP for DummyJSON invented.

2026-10-07 — HTTP reference maps and original illustrations added; sources read: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status, https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers, https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html. Twenty selected statuses, not empirical popularity ranking; 10 headers in each direction, plain-language glosses, advanced mechanisms previewed rather than assumed. Original assets/build_http_examples.py renders SVG/PDF for content negotiation and fictional webshop price manipulation. Server must validate inputs and compute trusted prices. Teacher-led AI demo clarified. 46 slides / 120 min; lecturer review pending.
