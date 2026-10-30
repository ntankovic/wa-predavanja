# Sources and verification — 2026-10-06

All URLs below were opened in full during drafting; public access without login. MDN pages are living documentation (no fixed edition); RFC 9110 is June 2022, Fielding, Nottingham and Reschke. Node API page observed as v26.10.0; local demo uses stable built-in HTTP APIs and is checked with local Node v20.11.0. No source prose or external diagrams copied.

| Source | Supported material / stable chapter IDs |
| --- | --- |
| [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) | `s09`, `s10`, `s24` |
| [MDN: Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) | `s03`, `s05`, `s16` |
| [MDN: Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) | `s07`, `s30`, `s33` |
| [MDN: Using HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies) | `s26` |
| [MDN: Connection management in HTTP/1.x](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Connection_management_in_HTTP_1.x) | `s25`, `s28` |
| [MDN: Proxy servers and tunneling](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Proxy_servers_and_tunneling) | `s03`, `s18` |
| [MDN: Transport Layer Security](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Transport_Layer_Security) | `s17` |
| [MDN: Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) | `s27` |
| [MDN: DNS](https://developer.mozilla.org/en-US/docs/Glossary/DNS) | `s15` |
| [MDN: TCP](https://developer.mozilla.org/en-US/docs/Glossary/TCP) | `s16` |
| [MDN: HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) | `s11` |
| [MDN: HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) | `s12`, `s13` |
| [MDN: Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) | `s12`, `s14` |
| [MDN: Accept](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept) | `s09`, `s14` |
| [Node.js: HTTP API](https://nodejs.org/api/http.html) | `s33` |

## Design provenance

Lecturer requested RS 01 as reference: `/Users/ntankovic/Dropbox/1_UNIPU/1_NASTAVA/FIPU-RS/rs-predavanja-v2/lectures/01-foundations/slides.hr.qmd`, its CSS and saved Croatian screenshots (3, 5, 18) inspected. Adopted the established palette, type scale, opening prediction question, sequential diagrams, teacher prompts and open closing challenge. No RS assessment rules, attendance QR, technical story or source diagrams copied.

All request/product examples, diagrams and exercises are original teaching scenarios, not production observations. `assets/build_diagrams.py` stores editable geometry and creates matching SVG/PDF. No image-license dependency. The Node demo simulates persistence and intentionally omits TLS/proxy/database deployment; it must not be used as evidence of those mechanisms.

## Pending review

Croatian lecturer content review pending; English files remain planning scaffolds. HTTP semantics are separated from product behavior. The approved observability wording is recorded in references/terminology.md; this lecture uses concrete logs and diagnosis examples.

## Correction: no prior HTTP knowledge — 2026-10-06

Lecturer clarified that students have not learned HTTP. Added `http-osnove` and `http-network` to chapter and slides; moved s07/s08 after s14 so status codes and message bodies precede fetch failure analysis. Existing section IDs remain stable; numeric section positions have changed. MDN contributors, *Overview of HTTP* (n.d.), full text rechecked 2026-10-06, supports client/server roles and request/response messages: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview . Plain-language product exchange and guided local-demo task are original teaching examples.

Lecturer clarified the actual prerequisite: frontend and Firebase library use only. Added `firebase-polaziste`, explained GET and /products separately, and moved the detailed architecture after first message reading. Firebase documentation *SDKs and client libraries*, full text checked 2026-10-06, supports the SDK abstraction: https://firebase.google.com/docs/firestore/client/libraries . No claim that every Firebase operation uses GET, one request, or TCP; exact prior Firebase product remains unspecified.

2026-10-06 — At lecturer request, adapted exercise/example heading badges from RS `lectures/01-foundations/assets/lecture.css`: rounded shape, padding, icon and color treatment; labels localized to Vježba and Primjer. Rebuilt Croatian HTML with just; embedded CSS checked. Browser visual verification remains blocked by the previously recorded headless Chrome launch failure; no desktop automation used.

2026-10-06 — Live first demonstration changed to https://dummyjson.com/ (HTML) and https://dummyjson.com/products (JSON). Both opened through web retrieval; Products documentation https://dummyjson.com/docs/products checked. Actual response has products array and title fields. Slides show an explicitly reduced field selection, not the complete response. Direct local curl could not resolve the host under the execution environment; the base products endpoint was independently retrieved by the web tool. Internal architecture remains an original local teaching model, not an assertion about DummyJSON.

## Narrative review — 2026-10-06

Reviewed all 42 slides, full Croatian chapter, notes, code examples and diagram labels against frontend/Firebase-only prerequisites. Stable source IDs above remain valid after reordering. Rechecked MDN Fetch, Cookies and Time to First Byte full pages during this review. TTFB source: https://developer.mozilla.org/en-US/docs/Glossary/Time_to_first_byte (MDN contributors, living document; accessed 2026-10-06), supports s28.

See `review.hr.md` for findings, corrections and remaining verification limits. No framework selection made; Fastify remains an unresolved course-plan proposal, not a teaching requirement.

2026-10-07 — Opening question follows the lecturer-supplied RS 01 pattern: illustrative UI plus colored answer chips. Chip CSS adapted from RS `01-foundations/assets/lecture.css`; original storefront illustration generated by `assets/build_loading_example.py`, SVG/PDF derivatives. Answers, teaching intent and timing unchanged.

2026-10-07 — Added original Firebase bridge diagram to HR chapter and slides; editable source `assets/build_firebase_diagram.py`, SVG/PDF derivatives, shared diagram style. Separates JavaScript/SDK in browser from remote service. Conceptual remote-data retrieval, not one-to-one network-message mapping or internal transport. Existing Firebase client-library source supports the explanation. Timing unchanged.

2026-10-07 — Moved existing DNS section directly after URL/address in chapter and slides; introduced domain name, FQDN and IP, illustrated resolver lookup/cache and separate subsequent web connection. Original SVG/PDF source: assets/build_dns_diagram.py. Timings reordered, total unchanged at 119 min / 42 slides. Sources read: MDN DNS https://developer.mozilla.org/en-US/docs/Glossary/DNS and RFC 8499 §2 https://www.rfc-editor.org/rfc/rfc8499.html (FQDN terminology). No current IP for DummyJSON invented.

2026-10-07 — HTTP reference maps and original illustrations added; sources read: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status, https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers, https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html. Twenty selected statuses, not empirical popularity ranking; 10 headers in each direction, plain-language glosses, advanced mechanisms previewed rather than assumed. Original assets/build_http_examples.py renders SVG/PDF for content negotiation and fictional webshop price manipulation. Server must validate inputs and compute trusted prices. Teacher-led AI demo clarified. 46 slides / 120 min; lecturer review pending.

2026-10-27 — Added `web-povijest` and `prvi-webovi`. Sources opened: CERN, *A short history of the Web*, https://home.cern/science/computing/the-birth-of-the-web/short-history-web/ (March 1989 proposal; end-1990 first server and browser on NeXT; info.cern.ch; August 1991 announcement; 30 April 1993 royalty-free release); Berners-Lee, *Information Management: A Proposal* (March 1989, May 1990), https://www.w3.org/History/1989/proposal.html ; W3C, *The Original HTTP as defined in 1991*, https://www.w3.org/Protocols/HTTP/AsImplemented.html (one-line GET request, HTML response, no status codes, connection closed by server); MDN, *Evolution of HTTP*, https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Evolution_of_HTTP (acronym, four building blocks, RFC 1945 / RFC 2068, HTTP/2 2015, RFC 9114); https://info.cern.ch/ (first-site and line-mode simulator links); https://worldwideweb.cern.ch/ (2019 rebuild of the WorldWideWeb browser). 2013 restoration of the first website: CERN, *Where the web was born*, https://home.cern/science/computing/the-birth-of-the-web/where-web-was-born/ — seen in a search summary only, full page not opened; verify before review. https://www.spacejam.com/1996/ opened; it appears to be a preserved copy with later link edits, so it is described as a preserved page, not the byte-identical original. CERN pages describe the 1993 release both as public domain and as royalty-free; the slide says "for free use". Accessed 2026-10-27.

2026-10-27 — `rucni-zahtjev`: behaviour observed locally (macOS 26.6, `/usr/bin/nc`, `man nc`: `-c` sends CRLF) against `assets/demo.mjs`: 200 with JSON and chunked encoding, 400 without Host, 404 for unknown path. Host requirement and CRLF line endings: RFC 9112 https://www.rfc-editor.org/rfc/rfc9112.html (§2.2, §3.2, §7.1) — cited from knowledge of the RFC, page not reopened in this session; verify section numbers. Linux `nc -C` (netcat-openbsd/ncat) and Windows Telnet Client enablement / `set localecho` are untested here and flagged in the notes.

2026-10-27 — Demo code moved to `code/server.mjs` (see `code/README.md`); earlier entries naming `assets/demo.mjs` refer to the same code. Rechecked with curl after the move: `/` serves `public/index.html`, `/products` returns 200 JSON.

- Slajd „Jedna TCP veza, više HTTP zahtjeva” (v1.18): ponašanje provjereno lokalno (Node v20.11.0, macOS `nc`): dva zahtjeva kroz istu vezu; odgovor sadrži `Connection: keep-alive` i `Keep-Alive: timeout=5`. **Neprovjereno (mreža blokirana):** URL-ovi MDN *Keep-Alive* (`/Web/HTTP/Reference/Headers/Keep-Alive`) i Node.js sidro `#serverkeepalivetimeout` navedeni su po sjećanju.

- Slajd „CORS na primjeru: zahtjev stiže, čitanje ne” (v1.19): provjereno u headless Chromeu (Playwright) s `code/01-introduction/server.mjs` na dva porta: `fetch` sa stranice drugog porta završava s `TypeError: Failed to fetch`, konzola javlja „No 'Access-Control-Allow-Origin' header is present”, a backend bilježi `GET /products` sa statusom 200. Tvrdnja o preflightu za ne-jednostavne zahtjeve oslanja se na MDN CORS (nije lokalno testirano).

- v1.20 (preslagivanje i dijagrami): novi originalni dijagrami `request-response`, `two-phase`, `cookie-session`, `https-wire` (generira `assets/build_diagrams.py`). `cookie-session` je izmišljen primjer (`/login`, `/cart` ne postoje u nastavnom backendu). Tvrdnja na `https-wire` da se uz HTTPS na putu vidi odredište, ali ne putanja, zaglavlja ni tijelo, oslanja se na opće ponašanje TLS-a (IP adresa i ime poslužitelja u SNI-ju ostaju vidljivi); nije posebno citirana — **provjeriti i dodati izvor** (npr. MDN TLS / RFC 8446).
