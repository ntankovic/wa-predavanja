# Web Applications — course plan and teaching requirements

## Course identity

- **Course (Croatian):** Web aplikacije
- **Course (English):** Web Applications
- **Lecturer:** assoc. prof. Nikola Tankovic, PhD
- **Faculty:** Faculty of Informatics, Juraj Dobrila University of Pula
- **Teaching languages:** Croatian first; English translated from the reviewed Croatian version, including chapters, slides, labels, exercises, and speaker notes.
- **Lecture duration:** 90–120 minutes, including examples, student questions, discussion, and recap.

Use these lecturer and faculty names on the book title page and the title slide of each lecture deck.

Standalone lecture PDFs must display **Web aplikacije, Predavanje NN** in Croatian and **Web Applications, Lecture NN** in English above the lecture topic, using the two-digit lecture number. Use **Web aplikacije** consistently for the Croatian course title, including title slides, book titles and footers.

## Croatian-first authoring and English translation

1. Develop and tune the Croatian chapter and derive Croatian slides from it. Review examples, pacing, diagrams, and wording with the lecturer.
2. Translate the reviewed Croatian material into English, preserving technical meaning, examples, citations, and teaching intent. Do not develop the two versions independently.
3. The lecturer reviews the English translation. Record preferred terms and rejected alternatives in [the shared terminology dictionary](references/terminology.md), then apply each decision consistently across existing translations and later lectures. Mark suggestions as provisional until the lecturer chooses them.
4. Track Croatian content review and English translation review separately in each lecture brief. A change to the Croatian source makes the affected English translation pending review again. Never mark a translation reviewed merely because it builds.
5. Consult the dictionary before every drafting, translation, and review pass. Keep grammatical inflections natural while retaining the approved term's meaning. Explain technical terms in familiar language when first introduced.

Store Croatian sources as `chapter.hr.qmd` and `slides.hr.qmd` beside the existing English `chapter.qmd` and `slides.qmd`. Keep assets together in the lecture directory; use `.hr` / `.en` suffixes for artwork whose labels differ. Shared editable geometry and source attribution remain common. Templates are scaffolding only; neither language is approved teaching material.

All rendering and verification commands default to English; select Croatian explicitly with `hr` (or `--lang hr` for Python scripts). The authoring workflow remains Croatian-first. English builds retain existing output paths. Croatian builds use `output/hr/` and must fail clearly when Croatian sources are missing, rather than substitute English. A Croatian book requires Croatian versions of all chapters in its assembly order. See `README.md` for language-specific commands.

## Course philosophy and scope

Teach durable **backend engineering principles**, using the question **“What actually happens when this request reaches the backend?”** as the recurring mental model. Extend it to concurrent requests, retries, slow/unavailable databases, permissions, crashes at specific points, and evidence of failure in production.

Students know frontend development and using Firebase through its library. Do not infer knowledge of HTTP, TCP, backend processes, Network tools or GET /products from that experience. Start with the known SDK call and explain what communication it hides. HTTP is not prerequisite knowledge (lecturer correction, 2026-10-06). Introduce clients, servers, requests and responses from scratch in Lecture 01, with a guided browser Network demonstration before methods, status codes, headers or fetch error analysis. Do not spend significant lecture time on JavaScript syntax, promises, Vue, HTML/CSS, SQL syntax, JSON, Git or Docker commands; provide brief context only when needed for a backend issue.

Practical stack: **Vue 3 / Pinia → REST API → Node.js backend → PostgreSQL or MongoDB**. Lecturer confirmed on 2026-10-06: cover the basics of both PostgreSQL and MongoDB; students may choose either for their project and should explain that choice. PostgreSQL remains the running relational example in the existing lecture plan; compare MongoDB on the same data and access patterns without implying identical guarantees. Fastify may be the primary backend framework. Redis, queues and Docker are optional implementation choices when the mechanism requires an example. Do not turn this into a framework tutorial, database course, DevOps course or cloud-provider tutorial. Students must transfer the principles to Spring Boot, ASP.NET Core, FastAPI, Django, Go and other ecosystems.

Distinguish three levels explicitly:

| Level | Examples | Teaching obligation |
| --- | --- | --- |
| Fundamental concepts | HTTP semantics, statelessness, API contracts, persistence, transactions, concurrency, authentication, authorization, trust boundaries, asynchronous processing, idempotency, latency/throughput, observability | Explain independently of a product. |
| Patterns and techniques | Layers, repositories, middleware, RBAC, workers, queues, retries/backoff, idempotency keys, cache-aside, structured logs, correlation IDs | Explain assumptions, guarantees, complexity and remaining failure modes. |
| Implementations/products | Node.js, Fastify, PostgreSQL, Redis, Docker, reverse proxies and cloud platforms | Use to demonstrate a concept; identify implementation-specific behavior. |

Teach caching and invalidation before Redis; identity and session state before comparing sessions/JWT; processes, configuration and lifecycle before containers. Avoid unqualified claims that one approach is “better”.

## Project technology approval

Lecturer decision, 2026-10-07: using project technologies different from those taught in lectures and practical classes requires prior explicit lecturer approval. PostgreSQL and MongoDB remain the two approved database choices. Transferability of concepts to other technologies does not authorize their use in the assessed project.

## Deliverables and teaching method

For each of the 12 weeks produce **two primary artifacts**:

1. A complete lecture script (`chapter.hr.qmd`, then reviewed translation `chapter.qmd`) for approximately **90–120 minutes**, also readable independently as a student book chapter. Include 3–6 explicit outcomes, prerequisites, progressively introduced concepts, worked scenarios, code where useful, diagrams, failure examples, counterexamples, misconceptions, student questions, links to previous weeks, and references. Mark lecturer cues clearly alongside the explanation; full explanations belong here, not in slide notes alone.
2. Corresponding slides (`slides.hr.qmd`, then `slides.qmd`), aiming for **30–40 substantive slides**; adjust when justified in the brief. Title/administrative/reference-only slides do not count toward that target. Each slide communicates one main idea, directly traceable to the script. Prefer diagrams, HTTP messages, schemas, small code snippets, timelines, comparisons and progressive states over paragraphs copied from the chapter.

For important mechanisms use **problem → naive implementation → failure → underlying reason → improved design**. Explain why a mechanism exists before showing configuration. Expose plausible code that fails under concurrency, retries, malicious input or infrastructure failure. Trace at least one execution step by step in transactions/concurrency, authentication, asynchronous processing and reliability/retry lectures.

For the last-item race, use separate visual states for initial stock, A reading, B reading, A writing, B writing, the violated invariant and the corrected implementation. Make accepted orders and remaining stock visible so the consequence of the interleaving is explicit.

Show assumptions, guarantees, added complexity and remaining risks when comparing designs. Explicitly distinguish guarantees provided by HTTP, the database, application code and a framework from engineering conventions. A diagram must teach a specific point and be technically correct. Use multiple slides for successive states of an execution; static PDF exports must retain every essential step.

Use student prompts repeatedly: Which component owns this rule? Where is state? Can the client enforce it? Can two requests violate the invariant? Is retrying safe? What if the dependency takes 30 seconds? What if the server crashes after the write but before the response? Can two backend instances run? What is the bottleneck? What evidence would explain the outcome?

## Timing and review

Plan a specific total within **90–120 minutes** in each brief, including participation, discussion and recap, and align slide notes with it. Scaffolds use a **provisional 105-minute planning budget**, not a completed teaching script. Record what can be shortened for 90 minutes and an optional extension to 120. Expand topics selectively; a long scope list is not a requirement to lecture equally on every term. Move supporting syntax and optional depth to reading or exercises.

When substantive authoring begins, change `scaffold` to `false` and `status` to `drafting` in `lecture.json`; do not retain the scaffold exemption for real teaching content. A drafted lecture must declare `duration_minutes` in `lecture.json` and provide per-slide `timing.json` entries (`slide`, `start`, `minutes`, `end`) covering the full planned duration. Placeholder scaffolds do not invent per-slide teaching timing. Automated builds check structure; only lecturer content/translation review and visual QA can make material ready.

## Continuity: one evolving backend

Use one application through all 12 weeks. **Provisional editorial choice:** a small ordering application with products, limited stock, users, orders and order items, a simulated payment dependency, email confirmation and generated invoice files. This is an example domain, not an assessment specification or instruction to integrate real payments. Its main state-changing request is `POST /orders`; listing and reading endpoints expose different semantics and performance issues.

Evolution: HTTP server → structured backend → REST contract → PostgreSQL persistence → transactions/concurrency control → authentication/authorization → security hardening → background jobs → failure handling/idempotency → measured performance/caching → testing/observability → production.

Carry the endpoint designed in Week 3 into Week 4 persistence, expose its race in Week 5, restrict it in Week 6, attack it in Week 7, and move expensive work to a worker in Week 8. For Weeks 9–12, continue with the explicitly supplied weekly scenarios: lost payment response/retry, slow endpoint diagnosis, retrospective failure investigation and production deployment. The supplied final continuity bullet was truncated after “Week 9 examines”; no missing wording is treated as a lecturer decision.

For each week record the incoming application state, the new requirement/failure, and the state handed to the next week. Keep intentionally vulnerable/naive examples visibly labelled and separate from corrected code. Do not silently replace an earlier implementation: explain the new assumption that invalidates it.

Final architecture: browser/Vue → HTTPS/reverse proxy/load balancer → multiple backend instances → PostgreSQL, optionally adding Redis/cache and queue → worker. Analyze how authentication, authorization, transactions, concurrency, retries, caching, observability and deployment affect the same requests.

## AI-assisted development and assessment design

Assume students can use generative AI tools. Understanding and verification matter more than boilerplate production. Generated routes, schemas, CRUD, SQL, tests, Docker configuration and API clients alone do not establish mastery. Prefer predicting behavior before execution, explaining generated code, reviewing unfamiliar code, identifying assumptions, finding security/authorization/race defects, reasoning about transaction boundaries and failures, diagnosing performance, and justifying corrections.

Include occasional plausible AI-generated defects: frontend-only authorization; check-then-update race; unsafe retry; JWT decoded without cryptographic verification; injectable SQL; a transaction opened too late; password logging; stale authorization in cache; N+1 queries; a job unsafe under duplicate delivery. Have students identify the violated assumption and construct evidence for the correction. Keep assessment format and weights pending lecturer decisions.

## Sources and correctness

Prioritize HTTP specifications and MDN for web behavior, OWASP for security, official PostgreSQL and MongoDB documentation for database semantics, official Node.js/Fastify documentation for implementation details, original technology documentation, and established architecture/design literature. Verify current/version-specific claims while drafting, using the actual authoritative source. Cite important claims in the script and slides and provide references at each lecture's end. Never infer framework/database/infrastructure guarantees from a convenient example.

Each scaffold names source categories to research, not verified citations. Record exact source, version where relevant, access date, supported claim and section in `sources.md`; mark unresolved claims explicitly. Do not treat a successful code run as proof of concurrency or security correctness.

## Lecture 00: orientation copied for adaptation

A separate 24-minute slides-only orientation was copied from Distributed Systems at the lecturer's request. It is outside the 12-week teaching sequence and excluded from the book. The Croatian draft now follows this course plan and four Web Applications administrative rules explicitly approved by the lecturer on 2026-10-06; see `lectures/00-course-introduction/sources.md` for their scope. Inherited RS links, QR and assessment diagrams are excluded from that draft. Historical assets and review records remain preserved; the English source is still the unadapted copy, pending Croatian review. See `lectures/00-course-introduction/README.md` for pending decisions and verification. All other weeks retain the 90–120-minute requirement.

## Syllabus status

The **12-week sequence and teaching requirements were supplied by the lecturer on 2026-10-06**. They are the authoring plan, not a claim about institutional accreditation, credits or assessment rules. Lecture 01 now has a Croatian chapter and a 46-slide draft (42 substantive slides), with a 120-minute teaching plan and an agent narrative review. Lecturer approval and complete visual verification remain pending; English remains a scaffold. Lectures 02–12 remain planned.

## 12-week sequence

| Week | Lecture | Application evolution | Status |
| --- | --- | --- | --- |
| 01 | [How Web Applications Actually Work](lectures/01-introduction/README.md) | Trace one request | drafting |
| 02 | [Backend Application Architecture](lectures/02-backend-architecture/README.md) | Separate endpoint responsibilities | planned |
| 03 | [REST and API Design](lectures/03-api-design/README.md) | Define the API contract | planned |
| 04 | [Databases and Persistence](lectures/04-persistence/README.md) | Persist orders in PostgreSQL | planned |
| 05 | [Transactions and Concurrency](lectures/05-transactions-concurrency/README.md) | Preserve stock under concurrent requests | planned |
| 06 | [Authentication and Authorization](lectures/06-authentication-authorization/README.md) | Enforce identity and object permissions | planned |
| 07 | [Web Application Security](lectures/07-security/README.md) | Challenge trust boundaries | planned |
| 08 | [Asynchronous Backend Processing](lectures/08-asynchronous-processing/README.md) | Move email/file work to workers | planned |
| 09 | [Reliability and Error Handling](lectures/09-reliability/README.md) | Handle lost responses and retries | planned |
| 10 | [Performance and Scalability](lectures/10-performance-scalability/README.md) | Measure and remove bottlenecks | planned |
| 11 | [Testing and Observability](lectures/11-testing-observability/README.md) | Collect test and production evidence | planned |
| 12 | [Deployment and Production Web Architecture](lectures/12-production/README.md) | Analyze the complete production lifecycle | planned |

### Week 1: How Web Applications Actually Work

**Scope:** Web application architecture; browser, frontend, backend and database; complete HTTP request/response lifecycle; methods, status codes, headers, content types and cookies in context; statelessness and persistent connections; conceptual HTTPS/TLS; DNS and TCP only as needed; reverse proxies; failure and latency locations.

**Required scenario / emphasis:** GET /products: pratiti jedan zahtjev i označiti svaku granicu, zapis stanja i mogući prekid. Jedan zahtjev kroz sustav; HTTP statelessness nasuprot trajnoj vezi i aplikacijskom stanju.

### Week 2: Backend Application Architecture

**Scope:** Backend responsibilities; routing; controllers/handlers; business logic; services; data-access layer and repositories; dependency direction; separation of concerns; configuration, environment variables and secrets; dependency injection as a concept; startup and shutdown; stateless application servers; monoliths and modular monoliths; architecture as applications grow.

**Required scenario / emphasis:** POST /orders: razložiti početni handler koji validira, primjenjuje pravila, pristupa podacima i šalje poruku. Endpoint raste; objasniti zašto granice odgovornosti pomažu bez obveznog sloja za svaku funkciju.

### Week 3: REST and API Design

**Scope:** APIs as contracts; resources and representations; resource-oriented design; URLs and resource naming; HTTP method semantics, safe and idempotent methods; status codes; request/response bodies; validation and error responses; pagination, filtering and sorting; partial updates; versioning and backward compatibility; REST constraints at an appropriate level; REST versus RPC; OpenAPI as contract/documentation.

**Required scenario / emphasis:** Definirati POST /orders, GET /orders/{id} i GET /products; usporediti dobar i problematičan ugovor. Klijent ponavlja ili pogrešno tumači operaciju; konvencija naziva URL-a nije jamstvo ponašanja.

### Week 4: Databases and Persistence

**Scope:** Persistent state; relational model; tables, primary/foreign keys and relationships; constraints; practical normalization; SQL from backend perspective, queries and joins; indexes; database connections and pools; repository/data-access patterns; parameterized queries; ORMs/query builders, benefits and hidden abstractions; schema migrations; SQL versus document databases; PostgreSQL and MongoDB basics (tables versus collections/documents, identifiers, CRUD, relationships, validation and indexes); choosing storage by access patterns and consistency needs.

**Required scenario / emphasis:** Dodati PostgreSQL za proizvode, narudžbe i stavke narudžbe; povezati zahtjev, SQL i promjenu stanja. Na istim podacima prikazati osnove MongoDB-a: dokumente, kolekcije, CRUD te izbor između ugniježđenih podataka i referenci. Usporediti modele i odabir baze za projekt. Pokazati što ORM skriva; usporediti vezu po zahtjevu sa skupom veza i jasno označiti granice resursa.

### Week 5: Transactions and Concurrency

**Scope:** Multiple requests and shared state; races; read-modify-write and lost updates; transactions and ACID, especially atomicity/isolation; practical isolation levels; dirty/non-repeatable reads and phantoms where appropriate; optimistic concurrency control; pessimistic locking; constraints as correctness mechanisms; atomic database operations; conceptual deadlocks.

**Required scenario / emphasis:** Dva kupca pokušavaju kupiti posljednji artikl: A čita 1, B čita 1, A piše, B piše; ispitati broj prihvaćenih narudžbi i preostalu zalihu. Obvezno korak po korak pokazati naivan kod, narušenu invarijantu i više mogućih ispravaka s pretpostavkama.

### Week 6: Authentication and Authorization

**Scope:** Authentication versus authorization; identity; password storage, hashing and salting; sessions, identifiers, cookies and storage; token approaches; JWT structure, purpose and misconceptions; access tokens and conceptual refresh tokens; session/JWT trade-offs; roles, permissions and RBAC; ownership and object-level authorization; middleware; state across requests; logout and session/token invalidation.

**Required scenario / emphasis:** Korisnik je prijavljen, ali traži tuđu narudžbu preko GET /orders/{id}; pratiti provjeru identiteta i dopuštenja zasebno. Obvezan potpuni slijed autentificiranog zahtjeva; ispravna autentikacija uz izostanak provjere vlasništva.

### Week 7: Web Application Security

**Scope:** Trust boundaries and untrusted client input; validation and output encoding; SQL injection; XSS; CSRF; CORS and same-origin policy; authentication/password attacks; broken access control; rate limiting; security headers; HTTPS; secrets; sensitive data exposure and logging; dependency vulnerabilities; OWASP Top 10 as a reasoning framework.

**Required scenario / emphasis:** Napasti prethodnu implementaciju narudžbi kontroliranim primjerima: SQL injection, pristup tuđem objektu i zahtjev preko druge web stranice. Ranjiva implementacija → napad → ispravak; sigurnost povezati s arhitekturom i granicama povjerenja.

### Week 8: Asynchronous Backend Processing

**Scope:** Synchronous HTTP processing versus asynchronous work; long-running operations; background jobs; queues; producers, consumers and workers; job queues and events; acknowledgements; retries; duplicates; at-least-once delivery; idempotent consumers; dead-letter queues; scheduled jobs; email and file-processing examples; API → queue → worker.

**Required scenario / emphasis:** Narudžba pokreće slanje e-pošte, a zatim izradu datoteke računa; pratiti granicu između HTTP odgovora i dovršetka posla. Obvezan slijed s prekidom prije/poslije potvrde, ponovljenom dostavom i analizom onoga što je izgubljeno ili dobiveno izdvajanjem posla.

### Week 9: Reliability and Error Handling

**Scope:** Normality of failures; client/server/dependency/database/network failures; timeouts; retry strategies and exponential backoff; retry storms; idempotency and keys; duplicate requests; partial completion; error propagation; graceful degradation; circuit breakers; rate limiting; conceptual backpressure; defensive external API use.

**Required scenario / emphasis:** Simulirana naplata uspije, ali se HTTP odgovor izgubi; klijent ponavlja isti zahtjev. Treba li naplata ponovno izvršiti? Obvezan slijed djelomičnog dovršetka, pada i ponavljanja; idempotency key analizirati zajedno s pohranom ishoda i konkurentnim zahtjevima.

### Week 10: Performance and Scalability

**Scope:** Latency, throughput and response time; bottlenecks; measure before optimizing; query performance/plans and indexes; N+1 queries; connection pooling; caching and cache-aside; invalidation and consistency; in-memory cache and Redis as example; application/HTTP caching; compression; pagination and avoiding work; vertical/horizontal scaling; stateless instances; load balancing; database bottlenecks.

**Required scenario / emphasis:** GET /orders postaje spor: izmjeriti SQL upite i vrijeme, dijagnosticirati N+1 ili čekanje veze, tek zatim usporediti optimizacije. Ispravno → sporo → izmjereno → dijagnosticirano → optimizirano; ne pretpostavljati da je cache rješenje.

### Week 11: Testing and Observability

**Scope:** Backend versus isolated function testing; unit/integration/API/database tests; test databases, fixtures and data; mocking choices; authentication/authorization tests; failure/concurrency tests; API contracts; structured logging and levels; request/correlation IDs; metrics including latency, error rate and throughput; tracing and conceptual distributed tracing; health checks; production debugging.

**Required scenario / emphasis:** Korisnik kaže: zahtjev je zakazao jučer u 14:32. Odrediti koji bi podaci objasnili put kroz API, bazu i worker bez izlaganja tajni. Bez prikupljenih dokaza dijagnoza postaje nagađanje; razlikovati test koji potvrđuje kod od testa koji može otkriti pogrešnu pretpostavku.

### Week 12: Deployment and Production Web Architecture

**Scope:** Development versus production; configuration, environment variables and secrets; build artifacts; processes and deployment units; containers/Docker as mechanism; proxies and TLS termination; app servers; database deployment and migrations; health/readiness/liveness; graceful shutdown; multiple instances, load balancing and stateless services; persistent state; CI/CD concepts; deployment strategies and rolling deployments; zero-downtime considerations; backward-compatible database changes; complete production request lifecycle.

**Required scenario / emphasis:** Pratiti zahtjev kroz Vue → HTTPS/proxy/load balancer → više backend instanci → PostgreSQL, uz opcionalni cache i red → worker, tijekom rolling deploymenta. Završna analiza cjelovite aplikacije; razmotriti stanje, naplatu, konkurentnost, migraciju sheme, kvarove i dokaze o radu.

## Illustration workflow

- Plan illustrations alongside the learning outcomes, before writing a long text-only draft. Record each figure's teaching purpose and its placement in the chapter and slides in the lecture's `illustrations.md`.
- Use diagrams to explain processes, message exchange, ordering, shared state, and failures. Each core mechanism should have a worked visual example when this makes it easier to understand; avoid decorative images and arbitrary image quotas.
- Start with relevant legacy figures. Inspect the complete source page, verify labels and assumptions, and record the original PDF, page, author, and attribution/license information in `sources.md`. Preserve the original source.
- Reuse a clear extracted figure; rebuild a low-resolution, crowded, outdated, or inconsistent diagram as editable vector artwork. Keep the editable diagram source in the lecture's `assets/` directory. Use SVG for HTML and a corresponding vector PDF or suitable PNG for PDF output.
- Create original technical diagrams with precise shapes, labels, and connectors. Prefer code-based vector drawing or a diagram description language over generated raster artwork for protocol logic, equations, or readable text. Use generated illustrations only when a conceptual scene or visual analogy helps, and review their technical meaning.
- Use consistent node names, colours, arrow meanings, and time direction. Label failures and state changes explicitly; colour alone must not convey meaning. Prefer the same running example across figures.
- Use explanatory pictures from the legacy teaching material as starting points for abstract comparisons; inspect their source pages and attribution, and redraw or extend them when needed. Explain why a warning or distinction matters with a concrete consequence, rather than leaving it as a slogan.
- Explain arrow direction and meaning in each diagram with a legend or nearby text. Distinguish calls/dependencies from chronological message exchanges and state explicitly when replies are omitted.
- Center the complete label group vertically inside diagram boxes, accounting for font size and text baselines. Check that the visible top and bottom padding are balanced, including boxes with a heading and subtitle.
- Share the same underlying artwork between chapter and slides. Leave generous inner margins in diagram boxes; fit long labels without letting text touch borders. Give book figures descriptive captions and surrounding explanation; use shorter labels and staged steps on slides where useful. A PDF must still explain every essential step without animation.
- Add alternative text for figures. Check every figure in the rendered lecture PDF and browser slides for label size, clipping, contrast, and correct sequence. Dense legacy slides should be split or redrawn instead of shrunk to fit.

## Folder structure

```text
COURSE.md                 Course identity, syllabus, and teaching requirements
AGENTS.md                 Working rules for agents
justfile                  Build and verification commands
lectures/
  README.md               Lecture registry, ownership, and progress
  _template/              Copy this directory to start a lecture
    README.md             Lecture brief and review checklist
    chapter.qmd            Student book chapter
    slides.qmd             Slide outline and speaker notes
    sources.md            References and verification notes
    illustrations.md      Figure purposes, sources, and placement
    assets/               Lecture-specific diagrams and images
references/               Shared bibliography and source notes
assets/shared/            Reusable visual assets
publishing/
  book/                   Book assembly order and front matter
  slides/                 Shared slide conventions
scripts/                  Local build commands
output/lectures/          Individual lecture PDFs
output/book/              Generated book exports
output/slides/            Generated teaching slide exports
```

## Lecture-by-lecture workflow

1. Define the lecture topic, prerequisites, learning outcomes, and scope. Register it in `lectures/README.md`.
2. Copy `lectures/_template/` to `lectures/NN-short-topic/`, using a two-digit sequence number and a descriptive slug.
3. Assign an agent to the lecture directory. Record ownership and status in the lecture registry so agents do not overwrite each other's work.
4. Collect and verify sources, then write the chapter with explanations, examples, exercises, and a recap.
5. Derive the slide deck from the reviewed chapter. Include teaching notes and checks for understanding.
6. Review technical accuracy, prerequisites, terminology, references, and consistency between chapter and slides.
7. Add the completed chapter to the book assembly order and build the deliverables locally with Quarto (see `README.md`).

Use these statuses: `planned`, `drafting`, `review`, `ready`. Only mark a lecture `ready` after both its chapter and slides have passed review.

## Content guidelines

- Write speaker notes as usable teaching cues: purpose, what to say or ask, expected answers, likely misconceptions, and a transition where useful. Use short labelled blocks or bullets instead of dense procedural paragraphs. End each lecture by widening the running problem into a small, open design challenge. Students should propose how to solve something using the ideas learned, with several defensible answers; avoid merely recalling an example already answered. Include a follow-up failure or constraint and a bridge to later lectures. The preceding recap consolidates the lesson. Explain the purpose, discussion prompts, and possible reasoning to the lecturer without scripting a single required answer.
- Keep slide speaker notes concise; place the complete lecturer script in the chapter. Preserve timing, questions, caveats and source links in notes.
- Default regular presentation text uses dark gray (`#333333`). Preserve the established title and bold-text colors, red definition labels, and diagram colors.
- Title slides place a larger FIPU logo above the title, aligned with its left edge. Preserve the logo proportions.
- Presentations use a visible 6 px bottom progress bar and a small footer identifying the course and lecturer, localized to the presentation language.

- Put key definitions in a distinctive red-bordered box with a thicker left edge and a pale red background. Number them by lecture and definition: **Definition 1.1**, **Definition 1.2**, **Definition 2.1**. Use a fenced Div such as `::: {.definition number="1.1"}`; keep the same explicit number in the chapter, slides, and translation. The shared filter labels Croatian boxes **Definicija**. Keep each definition short enough to fit together on one page or slide; introduce its concrete meaning before the box.
- State learning outcomes and prerequisite knowledge at the start of each lecture.
- Write learning outcomes in language students understand before attending the lecture. Introduce unfamiliar technical terms with a plain-language explanation and a concrete example; use a short chapter footnote when it helps without interrupting the flow.
- Ground examples in the evolving backend application and explain the concrete records, messages and requests involved.
- Build on frontend programming and Firebase usage; introduce HTTP/TCP and backend concepts explicitly; connect every week to earlier backend decisions.
- Use familiar section labels such as **Example**, rather than **Worked scenario**.
- Introduce concepts before formal definitions; explain assumptions, failure models, and tradeoffs explicitly.
- Use concrete web application examples, diagrams, and worked scenarios.
- Include exercises or discussion questions tied to the learning outcomes.
- Cite external claims and adapted material, and record asset provenance and licensing.
- Verify every reference exists, confirm author/title/year and the cited section, and open the actual public full text where available. Record access date and any email, login, or payment requirement in `sources.md`; never claim full-text access from a landing page alone. Required reading must be accessible without institutional subscriptions; clearly label optional resources with access conditions.
- Use publicly accessible books, papers, and university notes in exported references, with author, title, year, and a direct public link. Keep internal legacy filenames and adaptation notes in `sources.md`; preserve required public attribution.
- Format table headers in bold and alternate white and light-gray body rows, starting with white. Use a slightly smaller table font and generous horizontal and vertical cell padding. Apply this consistently in PDF chapters, the combined book, and HTML slides.
- Keep terminology and notation consistent across lectures. Identify dependencies on earlier chapters.
- Keep editable source files in lecture directories and generated exports in `output/`.
- Follow the lecturer-supplied sequence below. Assessment weights, credits, student links and attendance policy remain unspecified; do not invent them.


- Use `scripts/diagram_style.py` for original box-and-arrow diagrams: consistent cards, text padding and arrowheads. Keep lecture-specific geometry in the lecture asset generator.

### Terminal commands on slides — lecturer decision, 2026-10-28

Shell commands on slides use a terminal look, not ordinary inline code.

- **Inline command:** `` `npm start`{.cmd} `` renders as a dark pill with a green `$ ` prompt added automatically; do not type `$` yourself. Example: ``Run `cd code/01-introduction`{.cmd} then `npm start`{.cmd}.``
- **Terminal session or output (several lines):** use a fenced block ```` ```{.terminal code-line-numbers="false"} ````. Type `$ ` before each command; output lines have no prompt. It renders as a dark terminal window with three dots.
- Use `.cmd` / `.terminal` only for commands a person types in a shell (`npm`, `node`, `curl`, `nc`, `git`, `docker`, `PORT=3001 npm start` …). File names, URLs, identifiers, HTTP messages and program code keep ordinary code formatting (` ```http `, ` ```javascript `).
- Syntax highlighting is switched off inside terminal styling; colour must not split a command.
- Speaker notes and PDF chapters keep ordinary code formatting; the shared CSS lives in `publishing/slides/revealjs.yml`.

### Attendance QR slide — lecturer decision, 2026-10-28

Every slide deck (01–12 and the template; 00 already had it) has slide 2 right after the title slide: `## Evidencija prisutnosti {#attendance .attendance-slide}` / `## Mark your presence`, with `assets/attendance-wa.png` linked to https://bit.ly/wa-tu-sam and the link shown as text below. It takes 0.5 min from the title slide's first minute, so the lecture total does not change. It is not a substantive slide. Shared CSS is in `publishing/slides/revealjs.yml`.

## Orientation calendar — lecturer decision, 2026-10-07

The academic year ends on 30 September. Lecturer annual leave: 20 July–25 August. Display these dates in orientation 00 alongside the rule for projects not defended within the academic year; they do not establish specific exam appointments.

## Reusing a previous course application — lecturer decision, 2026-10-07

Students may request to extend an application from a previous course if it received at least very good (4), i.e. grade 4 or 5. This is a request to the lecturer, not automatic reuse approval or transfer of the previous grade. Orientation includes 12 optional project ideas with end-user AI features; these are suggestions, not mandatory assignments.
