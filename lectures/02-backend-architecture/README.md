# Predavanje 02: Arhitektura backend aplikacije

- English title: Backend Application Architecture
- Owner: current session
- Status: drafting (prvi cjeloviti hrvatski nacrt 2026-10-27, slides v1.0)
- Authoring language: Croatian
- Croatian content review: pending (lecturer)
- English translation review: not started
- Croatian revision translated: none; English files are structural placeholders only
- Duration: 105 minutes (lecturer decision 2026-10-27); per-slide timing in `timing.json`
- Slides: 39 (37 substantive; target 30–40)
- Prerequisites: Predavanje 01 (zahtjev, odgovor, status, handler, proces, port); `async`/`await`, ES moduli.
- Incoming state: `code/01-introduction` — jedan `server.mjs`, samo `GET /products`.
- Outgoing state: `code/02-backend-architecture` — `POST /orders` razdvojen na usmjeravanje, HTTP sloj, servis, katalog/pohranu i obavijest; konfiguracija iz okruženja; uredno gašenje; podaci i dalje u memoriji.

## Odluke predavača (2026-10-27)

- Backend ostaje na čistom `node:http` (bez paketa); Fastify se na kraju samo prikazuje (slajdovi 34–35), bez pokretanja.
- 105 minuta.
- Narudžbe i zaliha u memoriji iza repozitorija (`createMemoryCatalog`, `createMemoryOrders`); u 4. predavanju ista sučelja dobivaju PostgreSQL implementaciju.

## Ishodi (nacrt, revidirana Bloomova taksonomija)

- Razumijevanje: objasniti zašto zajedničko stanje ne smije biti u memoriji procesa
- Primjena: konfigurirati backend iz okruženja i uredno ga ugasiti
- Primjena: testirati pravila servisa s lažnim ovisnostima, bez HTTP-a
- Analiza: razložiti `POST /orders` na usmjeravanje, HTTP sloj, pravila, podatke i vanjske usluge
- Vrednovanje: obrazložiti u koji dio koda pripada novo pravilo

Stvaranje (osmisliti) vježba se u završnom zadatku „Osmislite sljedeći korak”, ali nije zaseban ishod.

## Skraćivanje i proširenje

- **90 min:** izostaviti Fastify (s32–s33, −5 min), skratiti AI pregled na 2 min (−2), spojiti „Zamjena implementacije” u „Dokaz: test” (−2), „Monolit nije pogreška” izreći uz modularni monolit (−2), „Tko koga poziva” samo pokazati (−1), skratiti vježbu „Gdje pripada pravilo?” na 1 min (−3).
- **120 min:** uživo dodati pravilo „najviše 5 komada” u servis s testom (+8) i pokrenuti Fastify skicu ako je paket instaliran (+7).

## Kontinuitet

- Iz 01: handler/ruta (s31 u 01), proces i port, dva procesa iza proxyja, Webshop (cijena od klijenta), izgubljeni odgovor.
- Za 03: „Osmislite sljedeći korak” traži ugovor API-ja za druge klijente; oblik grešaka i statusi (400/409/422) ostaju otvoreni.
- Za 04: `createPostgresCatalog()` s istim funkcijama; jedan redak u `server.mjs`.
- Za 05: komentar o check-then-act utrci u `order-service.mjs`; zadnji ruksak (zaliha 1).
- Za 08: `NOTIFIER=slow` pokazuje da e-pošta produljuje odgovor.

## Scope supplied by the lecturer

Backend responsibilities; routing; controllers/handlers; business logic; services; data-access layer and repositories; dependency direction; separation of concerns; configuration, environment variables and secrets; dependency injection as a concept; startup and shutdown; stateless application servers; monoliths and modular monoliths; architecture as applications grow.

## Otvorena pitanja

- Pregled predavača: hrvatska skripta i slajdovi.
- Fastify skica (s32) nije pokrenuta: u ovoj sesiji mreža je blokirana, pa `npm install fastify` nije moguć. Provjeriti s aktualnom verzijom.
- Vanjski izvori (Fowler, Dijkstra, Twelve-Factor, OWASP, Node.js i Fastify dokumentacija) navedeni su bez otvaranja u ovoj sesiji; vidi `sources.md`.
- Naredbe za Windows (PowerShell `$env:PORT=3001; npm start`) nisu isprobane.
- Engleski prijevod.

## Language workflow

Write `chapter.hr.qmd` and `slides.hr.qmd` first. After Croatian review, translate into `chapter.qmd` and `slides.qmd`. Record the source revision/date translated and any later changes requiring retranslation. Keep language-specific diagram labels and alternative text consistent.

## Review checklist

- [ ] Script supports 90–120 minutes and includes 3–6 explicit outcomes.
- [ ] Slides communicate one main idea each and map directly to the script.
- [ ] Important mechanisms follow problem → naive code → failure → reason → correction.
- [ ] A concrete execution is traced step by step where required.
- [ ] Misconceptions, student questions and AI-code review tasks are included.
- [ ] Concepts, patterns and product-specific behavior are distinguished.
- [ ] Continuity with the evolving application is explicit.
- [ ] Guarantees are attributed to the component actually providing them.
- [ ] `lecture.json` and `timing.json` agree with the brief and notes.

- [ ] Learning outcomes are covered by the chapter and slides.
- [ ] Chapter is understandable without the slides.
- [ ] Technical claims, examples, and sources have been checked.
- [ ] Assumptions, failure models, and tradeoffs are explicit where relevant.
- [ ] Exercises and discussion prompts align with the outcomes.
- [ ] Terminology and notation match the shared dictionary.
- [ ] Croatian chapter and slides have passed lecturer review.
- [ ] English translation reflects the recorded Croatian revision.
- [ ] Lecturer translation choices are recorded in the dictionary and applied consistently.
- [ ] Both language exports have passed visual review.
- [ ] Slide sequence and speaker notes support classroom teaching.
- [ ] Diagrams are readable and asset provenance is recorded.
- [ ] Essential visual steps are understandable in the static PDF as well as the slides.
- [ ] Timing totals 90–120 minutes, including student participation.
- [ ] Lecturer and faculty names are correct.
- [ ] Review findings and remaining issues are recorded below.

## Review notes

2026-10-27 (agent): build `just render 02-backend-architecture hr` i `just browser-check 02-backend-architecture hr` prolaze (39 slajdova). Sav kod u `code/02-backend-architecture` pokrenut lokalno (Node 20.11): `npm test` 5/5; svi statusi u tablicama provjereni `curl` zahtjevima; naivni poslužitelj (četiri zahtjeva, djelomično umanjenje zalihe, pad procesa); `NOTIFIER=fail|slow`; neispravna konfiguracija i zauzet port (exit 1); uredno gašenje (dovršen zahtjev, odbijena nova veza, neaktivna keep-alive veza ne odgađa izlaz); dva procesa prodaju isti ruksak; `--env-file` ne ispisuje tajnu. Pregled predavača nije obavljen.
