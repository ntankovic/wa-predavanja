# Predavanje 01: Klijent, poslužitelj i HTTP

- Owner: current session
- Status: drafting; Croatian lecturer review pending
- English translation: not started; existing English files remain scaffolds
- Duration: 120 minutes, including demonstration, discussion and recap
- Slides: 42 total; 42 substantive, plus title, outcomes and two references
- Prerequisites: frontend programming and using Firebase. No HTTP, TCP, Network tools or backend knowledge assumed.

## Learning outcomes

- Explain how the browser requests data and receives a response.
- Read a simple HTTP request and response.
- Trace a request through the browser, backend and database.
- Identify component responsibilities and stored state.
- Suggest evidence to locate a delay or failure.

## Teaching sequence

Start with a familiar Firebase library call and the missing-products scenario. Introduce client, server, request and response in ordinary language. Guide students through Network before asking them to interpret protocol fields. Explain the address, then domain names/FQDN, IP and DNS, then GET and /products separately, then the response, status codes and headers. Then make the switch to our own backend visible, define API, Node.js, process, route and handler, and inspect a naive fetch. Keep state modelling, corrected fetch and the local four-outcome demonstration together. Return to the resolved address and trace TCP, TLS and the newly introduced proxy; follow the complete request in four visual stages. State leads to cookies and sessions before statelessness and connection reuse. Diagnosis and the final ordering challenge close the story.

The Firebase bridge does not claim that each SDK call maps to one GET request or a particular transport. The lecturer has not specified the Firebase product used previously. The local demo uses a simulated repository, not Firebase or a real database.

## Timing

The authoritative per-slide plan is `timing.json`; matching timings are in speaker notes. Default total: 120 minutes. Lecturer-requested reference/example slides bring the total to 49 slides (46 substantive); the status/header maps are brief recognition aids. A 90-minute delivery needs the abbreviated route below, not faster reading of every slide: assign methods (3 min), trust boundary (3), cookies/stateless/session comparison (9), CORS (3), lost response (3), and the misconceptions exercise (4) as guided reading; shorten pair diagnosis from 6 to 3 minutes and the opening vote from 3 to 2 (30 minutes total). In that route remove the CORS row from the pair exercise, omit session from the recap and postpone the cookie/session discussion. The default exported deck remains the full 120-minute route; a separate 90-minute export has not been prepared.

## Demo and sources

The first Network demonstration uses https://dummyjson.com/ and https://dummyjson.com/products with no local installation. Later controlled failures use the local demo: run `node assets/demo.mjs` from this directory and open `http://127.0.0.1:3000`. First use the successful data-fetch button; inspect other cases only after response codes and bodies have been introduced. `sources.md` records verified documentation and the prerequisite corrections. Stable section IDs link the reordered chapter and slides; source mappings use stable section IDs.

## Review checklist

- [x] Script supports 90–120 minutes and includes 3–6 explicit outcomes.
- [x] Slides communicate one main idea each and map directly to the script.
- [x] Important mechanisms follow problem → naive code → failure → reason → correction.
- [x] A concrete execution is traced step by step where required.
- [ ] Misconceptions, student questions and AI-code review tasks are included.
- [x] Concepts, patterns and product-specific behavior are distinguished.
- [x] Continuity with the evolving application is explicit.
- [x] Guarantees are attributed to the component actually providing them.
- [x] `lecture.json` and `timing.json` agree with the brief and notes.

- [x] Learning outcomes are covered by the chapter and slides.
- [x] Chapter is understandable without the slides.
- [ ] Technical claims, examples, and sources have been checked.
- [x] Assumptions, failure models, and tradeoffs are explicit where relevant.
- [x] Exercises and discussion prompts align with the outcomes.
- [x] Terminology and notation match the shared dictionary.
- [ ] Croatian chapter and slides have passed lecturer review.
- [ ] English translation reflects the recorded Croatian revision.
- [ ] Lecturer translation choices are recorded in the dictionary and applied consistently.
- [ ] Both language exports have passed visual review.
- [x] Slide sequence and speaker notes support classroom teaching.
- [ ] Diagrams are readable and asset provenance is recorded.
- [ ] Essential visual steps are understandable in the static PDF as well as the slides.
- [x] Timing totals 90–120 minutes, including student participation.
- [ ] Lecturer and faculty names are correct.
- [x] Review findings and remaining issues are recorded below.

## Review notes

2026-10-06: revised prerequisite assumptions with the lecturer; added Firebase-to-HTTP bridge and beginner Network exploration, reordered first message reading before fetch analysis. Croatian content review remains pending.

Full narrative audit and remaining limits: [review.hr.md](review.hr.md).

2026-10-07 — Added 20-status family map, separate ten-header request/response maps, Accept/Content-Type illustration and webshop price trust example. 46 slides, 120 min. One minute removed from each of outcomes, opening vote, demo, pair diagnosis and misconception discussion to accommodate six minutes of additions. Demo explicitly lecturer-led with checked AI-generated code. Earlier timing/review snapshots are superseded.

2026-10-27 — Lecturer requested an HTTP introduction: added `web-povijest` (origin of the web, HTTP acronym, HTTP/0.9 to HTTP/3 timeline, 3 min) and `prvi-webovi` (restored first website, line-mode simulator, WorldWideWeb rebuild, Space Jam 1996, 3 min) to the Croatian chapter and slides. Six minutes recovered: Firebase 3→2, HTTP request/response 4→3 (acronym moved), naive fetch 5→4, four-outcome demo 5→4, pair diagnosis 5→4, closing design challenge 4→3. Total remains 120 min. English translation pending.

2026-10-27 — `s03` renamed „Naš nastavni backend”: states explicitly that DummyJSON is someone else's backend and the teaching backend is `assets/demo.mjs` on the lecturer's computer (127.0.0.1:3000), developed all semester, real database from Lecture 04. Added `rucni-zahtjev` demonstration (4 min): typing GET /products with nc (macOS `-c`, Linux `-C`) or Windows telnet; 200, missing Host 400, unknown path 404. Verified locally against demo.mjs with nc on macOS; Linux and Windows commands not tested. Time recovered: s03 3→2, s09 3→2, s12 3→2, misconceptions 3→2. Total 120 min.

2026-10-27 — Lecturer decision: the teaching backend lives in the shared top-level `code/` folder (Node.js 20+, no dependencies, `cd code && npm start`). `assets/demo.mjs` and `assets/demo.html` moved to `code/server.mjs` and `code/public/index.html`; behaviour unchanged. Slides and chapter now give `cd code`, `npm start`. `code/` is the week-01 state and will evolve with later lectures.

2026-10-27 — Lecturer correction: code is kept per lecture. Moved to `code/01-introduction/` (own package.json, README); top-level `code/README.md` indexes lecture copies. Later lectures copy the previous folder and change only what they introduce. Slides/chapter now say `cd code/01-introduction`, `npm start`.

2026-10-27 — `s05` (was „HTML aplikacije i podaci proizvoda”, lecturer: unclear) rewritten as „Okvir stranice i podaci stižu odvojeno”: table of app load (GET /, .js, .css), data request (GET /products from JavaScript) and rendering (no request); explicitly linked to the opening question. Timing unchanged.

2026-10-27 — `s33` retitled „Isti zahtjev, četiri ishoda”: removed third-person lecturer reference and stale „AI-generated code” wording; demo now explicitly uses code/01-introduction. Backend responses are given; students predict the display state (loading/data/empty/error) from the s30 code, answers in notes.

2026-10-27 — Lecturer flagged abrupt transition into `s16`. Moved „Veza i port” directly after `rucni-zahtjev` (it explains the nc 127.0.0.1 3000 connection just opened); added bridge sentence to `s17` HTTPS (from one computer to the internet, plain HTTP text readable en route). Timing reordered, total unchanged.

2026-10-27 — Lecturer asked for a clear program/process/computer explanation. `s04` replaced by „Program, proces i računalo” with new original diagram `assets/program-process.hr.svg` (one computer; server.mjs on disk; two node processes on ports 3000/3001 with separate memory; browser and nc also processes; no proxy) and a live demo (npm start, PORT=3001 npm start, ps / Activity Monitor / Task Manager). The proxy diagram `s04a` moved after `s18`; its label now uses server.mjs and drops unexplained n values. s04 1→3 min; trust boundary 3→2, persistent connection vs session 3→2. Windows PowerShell PORT syntax and process-listing commands untested.
