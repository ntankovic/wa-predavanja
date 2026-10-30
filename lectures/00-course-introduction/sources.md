# Internal sources and confirmation record

Reviewed 2026-09-14. Internal provenance is not displayed as student reading.

| Source | PDF page | Used for | Status |
| --- | --- | --- | --- |
| Nikola Tanković, RS-01-Intro.pdf, 2022/23 | 1 | Author and historical year | Historical identity confirmed on cover |
| Same | 3 | Theory plus small-project learning goals | Rephrased as course goals |
| Same | 4 | Microservices and distributed data analysis practical themes | Historical; current briefs not confirmed |
| Same | 5 | Optional attendance; individual projects; GitHub progress; project defence and oral exam | Exact administrative content checked in text and rendered source page; current applicability unconfirmed |
| Same | 6 | Help through documentation, Slack, colleagues, assistant, consultations | Rewritten as generic study guidance; current channels unconfirmed |
| Same | 2 | Old attendance short link | Excluded; not verified as a current student resource |
| COURSE.md | Current plan | Identity, proposed sequence, language | Project requirements, not official university assessment policy |

No numerical weights, pass thresholds, number of projects, deadlines, retake arrangements, contact address, or current policy URL were established. No public reference is offered as evidence for current local assessment rules. Project-defence preparation prompts are original study guidance, not an official rubric.

Before classroom release, the lecturer must confirm or replace the historical rules, supply the missing administrative details and official student-accessible links, and remove draft/historical labels only for confirmed content. Record the confirmation date and source here.

2026-09-17 — Lecturer explicitly supplied `http://bit.ly/rs-tu-sam` as the presence check-in URL and requested it with a QR code on slide 2 of every deck. This supersedes the earlier decision to exclude the old attendance link; it does not confirm an attendance obligation. Teaching staff and assessment-flow revision remains pending the newer PDF offered by the lecturer.

## Lecturer-supplied BPMN and staff update, 2026-09-17

- Original image: `assets/hodogram_rs.png`, copied unchanged from the lecturer-supplied `/Users/ntankovic/Downloads/hodogram_rs.png`. This is the visual authority for the included process and its annotations.
- Supporting editable source: `assets/hodogram-original.bpmn`, copied unchanged from `../hodogram.bpmn`; retained for provenance, not assumed pixel-identical to the supplied PNG.
- Staff responsibility confirmed in conversation: lectures — Nikola Tanković; practical classes — Luka. Full name/title for Luka awaits the newer deck.
- The diagram supplies previously missing information: practical points and project work in parallel; 7-day submission lead time; oral-exam exemption conditions (at least 50% of practical points, no disputed project parts, lecturer discretion, valid through academic year); defence at least 3 days after submission and by exam day; re-registration after failure; commits every 1–2 days and authenticity checks. These supersede earlier claims that the supplied material established no thresholds or timing. No overall grading weights or current calendar dates are inferred.
- English process overview is a provisional translation of the lecturer-supplied Croatian diagram; original Croatian artwork is preserved.

## AI policy confirmed 2026-09-17

The lecturer explicitly permits AI use, restricted to technologies used in lectures or approved by the professor. Students must understand every part of generated code and prove that they guided architectural decisions, including the reasoning, alternatives, and tradeoffs. “Architecture is a set of informed choices” is the lecturer's framing. No prompt-log submission or specific disclosure format was requested. This supersedes the earlier statement that AI-use permission was unresolved. Croatian wording is recorded in `ai-policy.hr.md`; English slide wording remains pending language review.

2026-09-17 — Lecturer confirmed the practical-class instructor’s full name and title: **Luka Blašković, mag. inf.** This resolves the earlier pending staff-name item.

2026-09-17 — Lecturer clarified that the BPMN describes how to pass the **course**, not merely the exam. The oral exam is one possible path; exemption provides another. Updated slide titles and teaching notes accordingly.

2026-09-17 — Lecturer rejected the “Assessment details still to be announced” placeholder: the supplied BPMN is authoritative for these process rules. Replaced the slide with submission timing, exemption conditions and validity, registration on both paths, defence timing, and re-registration after an unsuccessful result.

2026-09-17 — Lecturer confirmed course-information locations: E-Učenje, https://e-ucenje.unipu.hr/, and the course web page, https://ntankovic.unipu.hr/rs. Added both as clickable links. This resolves the previously missing course-information links.

2026-09-17 — Lecturer confirmed: consult course materials before asking; all questions go first to Google Chat under **FIPU RS**. Email is discouraged. This resolves the current help-channel question and supersedes legacy Slack guidance.

## Course page review, 2026-09-17

Reviewed public Notion course page https://fiputreca.notion.site/Raspodijeljeni-sustavi-544564d5cc9e48b3a38d4143216e5dd6 through its public page-data response.

- Lecturer confirmed all lectures are recorded on YouTube. Page supplies playlist: https://www.youtube.com/playlist?list=PLIeA2EYS12RVaj1GdVP4fkNrLiK5k6VD-. Added to the course-information slide.
- “Potrebna znanja programskog jezika Python” supplies the programming-preparation checklist. Summarised in English; language review pending.
- Page confirms Nikola Tanković, Luka Blašković, and the attendance short link.
- Do not copy stale/conflicting communication details: page includes Slack, “FIPU 24/25 RS”, a 2025–2026 Moodle link, and a statement that the traditional e-learning portal is unused. Current lecturer instructions take precedence: Google Chat **FIPU RS**, https://e-ucenje.unipu.hr/, and https://ntankovic.unipu.hr/rs.
- Other links (old Zoom and assignment submission) were not promoted as current instructions.

2026-09-17 — Lecturer added: exempt students must note their exemption; appointment booking is at https://ntankovic.unipu.hr/termin, with appointments available 10 days in advance. Added to the assessment slide and teaching notes.

2026-09-17 — Lecturer correction: the minimum interval between submission and defence is **3 working days**, not 3 calendar days. This supersedes the original BPMN image’s “3 dana”. The source image is preserved unchanged; its slide explicitly displays the corrected rule, and all teaching notes use working days.

2026-09-17 — Lecturer added Docker Compose and Docker Swarm to the programming-preparation checklist.

## Original explanatory diagrams, 2026-09-17

Created five editable bilingual diagrams in `assets/build_diagrams.py`, with `.hr.svg`, `.en.svg`, and corresponding vector PDF exports. No third-party stock artwork was incorporated.

- `course-completion`: simplified from the lecturer-supplied `hodogram_rs.png`; preserve original attribution and use the full BPMN on the following slide. Arrows show parallel inputs, exemption alternatives, and repeat registration after an unsuccessful result.
- `deadlines`: lecturer-supplied rules and corrections: ≥7 days before exam, ≥3 working days between submission and defence, defence by exam day, booking availability 10 days ahead. Intervals are schematic, not a calendar.
- `attendance-explained`: lecturer-confirmed check-in link and participation guidance; no claim that attendance is compulsory or points-bearing.
- `ai-responsibility`: lecturer-confirmed policy; student chooses architecture, directs AI, and remains accountable for code and reasoning.
- `practical-work`: original illustrative request-flow and split/process/combine examples of the already stated themes. Request arrows omit replies; data arrows show data flow.

Croatian and English labels were authored together with Croatian first in the source; English wording remains pending lecturer review.

2026-09-17 — Lecturer confirmed attendance is optional. In lecture 00 only, attendance explanation precedes the QR slide and has no repeated URL.

2026-09-17 — Lecturer removed the 7-day submission rule. Current deadline guidance uses at least 3 working days between submission and defence, with defence no later than the exam date. Removed the 7-day interval from both language diagrams, alt text, and teaching notes. The unchanged source BPMN image contains historical wording superseded by this instruction.

## External artwork added 2026-09-17

- **Teaching**, Katerina Limpitsouni / unDraw: https://undraw.co/illustration/teaching_58yg. Original SVG: https://cdn.undraw.co/illustrations/teaching_58yg.svg. Original saved as `assets/undraw-teaching.original.svg`; derivative `undraw-teaching.svg` changes only the purple accent to FIPU blue (#1585b4). Attendance slide.
- **Online learning**, Katerina Limpitsouni / unDraw: https://undraw.co/illustration/online-learning_tgmv. Original SVG: https://cdn.undraw.co/illustrations/online-learning_tgmv.svg. Original saved as `assets/undraw-online-learning.original.svg`; derivative changes only the accent to FIPU blue. Course information slide. Both use https://undraw.co/license (free use/modification; no required attribution); visible source links are included voluntarily.
- **Server racks in data center**, imgix / Unsplash, published 2017-09-26: https://unsplash.com/photos/server-racks-in-data-center-klWUhr-wPJ8. Image CDN: https://images.unsplash.com/photo-1506399558188-acca6f8cbf41?fit=max&fm=jpg&q=85&w=1800. Saved as `assets/server-racks.jpg`; CSS crops the display, source bytes unchanged. License: https://unsplash.com/license. Course-goals slide, with visible credit. This is illustrative infrastructure, not claimed to belong to the university.
- **YouTube icon**, official source https://brand.youtube/youtube-icon/. Image: https://www.gstatic.com/marketing-cms/assets/images/96/ff/14b02dc0467e8875e062e9565cbd/external-icon-core-1.png. Saved unchanged as `assets/youtube-icon.png`. CSS crops surrounding presentation whitespace while preserving the full mark and proportions. Icon is next to and linked to the course playlist; colours unchanged. Brand guidance: https://brand.youtube/ and https://about.google/brand-resource-center/guidance/ (educational use). No endorsement implied.

All assets retrieved via `just download-image`. Accessed 2026-09-17. Originals retained; not redistributed as an asset pack.

2026-09-17 — At the lecturer’s request, removed visible unDraw and Unsplash credits from slides. Their licenses do not require attribution. Full source and license records remain here.

2026-09-18 — Lecturer replaced the E-Učenje URL with https://moodle.srce.hr/. Applied to Croatian and English slides; supersedes the previously confirmed e-ucenje.unipu.hr URL.

## Copy to Web Applications, 2026-10-06

The lecturer requested this orientation as adaptation material. Existing verification and policy approvals above belong to the source Distributed Systems course only. The shared attendance fragment was inlined and its QR copied into local `assets/attendance-qr.svg`; it still encodes the source-course `http://bit.ly/rs-tu-sam` link and must be replaced or removed during adaptation. Source QR provenance: lecturer-supplied URL, locally generated with Python qrcode 8.2, medium error correction and four-module quiet zone, approved for the source course on 2026-09-17. No new Web Applications policy approval is implied.

## Web Applications adaptation — 2026-10-06

This section governs the adapted Croatian deck. Earlier approvals above belong only to Distributed Systems.

- Lecturer supplied `/Users/ntankovic/Dropbox/1_UNIPU/1_NASTAVA/FIPU-WA/Public/DWA-P1.pdf` (Nikola Tanković, Web aplikacije, 2021/22). Read in place; no PDF or assets copied. Pages 4–6 visually inspected.
- Lecturer explicitly approved four numbered rules in conversation: optional lecture/practical attendance with active participation; team project with individual contributions tracked and defence plus oral exam; completed project submitted at least three working days before the exam date; if not defended during that academic year, a new individual project, proposed topic approved by the lecturer (pages 4–5).
- Staff retained by explicit instruction: Nikola Tanković (lectures), Luka Blašković (practical classes).
- Course scope, prerequisites, teaching stack, sequence and AI-assisted verification guidance derive from `COURSE.md`; no external technical guarantees introduced.
- No permission inferred for page 6 project workflow, historical team-size limits, project-size grading, dates, links, or images. These were not incorporated.
- Removed source-course QR, links, BPMN, exemption/50% rules, booking rules and commit-frequency requirement from the Croatian deck. Assets retained as historical sources, unused in this draft.
- English remains the inherited source deck, NOT an adapted translation or approved Web Applications deck. Translation deferred until Croatian content review, per COURSE.md.

2026-10-06 — Lecturer confirmed Google Chat group **FIPU WA** and attendance URL **bit.ly/wa-tu-sam** in conversation. Added the group name and clickable HTTPS attendance link to the Croatian deck. No QR asset copied or regenerated; the inherited RS QR remains unused. Link destination was supplied by the lecturer, not independently verified.

## Oral examination requirements — 2026-10-06

Lecturer supplied `/Users/ntankovic/Dropbox/1_UNIPU/1_NASTAVA/FIPU-WA/pitanja_usmeni.v2.pdf` and explicitly instructed adaptation of Lecture 00 to what students must know. Title: „Pitanja za usmeni ispit – Web aplikacije”; attribution: lecturer-supplied document (no author printed). All five pages read and visually inspected. Source PDF remains unchanged in place; no assets copied.

- Page 1: list is guidance, not exhaustive; scope includes official literature, lectures, practical classes and everything used in the project.
- Sections 1–10, pp. 1–3: knowledge areas, including Express.js, Vue 3, Axios and MongoDB/Atlas. Summarised on the new oral-scope slide.
- Section 11, pp. 3–5: actual code and application behavior, prediction before execution, end-to-end request tracing, diagnosis, permissions, data, async behavior and AI-code verification. Adapted into project-demonstration and AI slides.
- Section 12, p. 5: live code changes, affected components, prediction, results and at least one edge case; local execution on test data, scope suited to defence time. Added a dedicated slide.
- Reconciliation pending: the exam document explicitly includes Express.js and MongoDB/Atlas; COURSE.md specifies PostgreSQL and possible Fastify for teaching examples. No exam topics silently removed and no teaching stack changed. Lecturer to reconcile the technology-specific scope.
- No public download URL supplied; no local filesystem link exposed in student slides.

2026-10-06 — Lecturer supplied the QR image directly and identified its URL as `bit.ly/wa-tu-sam`, authorizing its use. Copied unchanged to `assets/attendance-wa.png` from clipboard image `codex-clipboard-nHUWZ4.png`; no regeneration, cropping or PDF-origin claim. Both image hyperlink and text hyperlink use `https://bit.ly/wa-tu-sam`. Image visually inspected; encoded payload not independently decoded.

2026-10-06 — Lecturer confirmed teaching the basics of both PostgreSQL and MongoDB, with either permitted for the project. Updated COURSE.md and Lecture 00 stack/exam overview. This supersedes the pending database-scope issue above; framework-specific Express.js versus Fastify alignment remains pending.

2026-10-06 — Lecturer approved matching RS 00 layout. Restored separate large QR slide and attendance illustration, reused existing attributed AI artwork; added original editable request/evidence/live-change SVGs with vector PDF derivatives in assets/build_wa_diagrams.py. 17 slides, 20 minutes. Previously recorded 16-slide counts are superseded.

2026-10-06 — Restyled the Croatian AI responsibility loop with the shared card/arrow style. Content and original attribution retained; current editable source is `assets/build_wa_diagrams.py`. Archived generator no longer overwrites this Croatian asset. SVG and PDF inspected visually; all box-and-arrow figures referenced by current HR slides 00/01 now use the shared style. HTML rebuilt with `just slides 00-course-introduction hr`; browser QA remains pending the headless runtime installation.

2026-10-07 — Lecturer explicitly requires prior approval for project technologies differing from lectures and practical classes. Applied to the technology slide, speaker notes and COURSE.md; PostgreSQL/MongoDB choice retained.

## Orientation visuals and AI tools — 2026-10-07

- Original editable illustrations: `assets/build_orientation_visuals.py`; SVG and PDF derivatives. Git history uses fictional names, commit hashes and counts (3/2/1). Calendar assumes a Wednesday exam, prior Friday deadline, no holidays; weekend days excluded.
- Technology icons are original simplified identifiers inspired by familiar JS/Vue/Firebase/Pinia imagery, not downloaded official logos. HTTP is an original message-exchange symbol. Network download was unavailable.
- Claude/Codex app icons extracted without graphical alteration from installed `/Applications/Claude.app/Contents/Resources/electron.icns` and `/Applications/Codex.app/Contents/Resources/electron.icns`, converted to PNG for identification. Trademarks remain their owners'. Claude icon identifies the family, not a unique Design/Code product mark.
- Official documentation read: https://code.claude.com/docs/en/overview (code agent); https://www.anthropic.com/news/claude-design-anthropic-labs (visual work/prototypes); https://learn.chatgpt.com/docs/code-review (Codex review); https://github.com/QwenLM/Qwen3-Coder and https://github.com/deepseek-ai/DeepSeek-Coder-V2 (downloadable coding models). Public pages, no login required. No pricing, hardware minimum or comparative ranking claimed. DeepSeek model licence distinct from repository MIT licence.

2026-10-07 — Lecturer supplied 30 September academic-year end and 20 July–25 August annual leave. Original calendar-card illustration `assets/academic-year.hr.svg` / `.pdf`, editable in `assets/build_orientation_visuals.py`; placed on the existing repeat-project slide. Timing unchanged.

2026-10-07 — Lecturer requested previous-app extension option (minimum grade 4, by request) and imaginative AI project ideas. Added eligibility slide plus three slides with 12 original end-user AI concepts and concrete backend scope. HR orientation now 24 slides / 24 minutes, timings and metadata updated. Suggestions are optional; technology-approval rule retained.

## Web aplikacije — lecturer decisions, 2026-10-13

Source: lecturer-supplied instruction "Uputa: slajdovi Zašto dolaziti na predavanja i povezane odluke u uvodnom predavanju (00)", based on RS `lectures/00-course-introduction/slides.hr.qmd` slides 4–5 and `assets/lecture.css`. The lecturer confirmed in this session that all four related RS decisions apply to Web aplikacije: typography tokens, the "explain the change" defence slide (replaces the live code change in "Pitanja za usmeni ispit – Web aplikacije", section 12, p. 5), the commit rule plus "no AI chat logs", and the project-section order.

- Recordings: the lecturer answered "some / not decided". No claim that all lectures are recorded; slides say "materijali i, gdje postoje, snimke". Open.
- Attendance optional and Google Chat FIPU WA: already confirmed (2026-10-06).
- Defence and oral exam exist (confirmed rules above), so "Prioriteti", "Rasprava s kolegama" and "usmjereni na ocjenu" stay, adapted to name both.
- Wording pending lecturer confirmation: "Ako samo slušate, oni vam mogu biti jednako dobri" and the "usmjereni na ocjenu" row.
- Diagram rule from RS (WA card style, right-angle arrows, no large coloured labels inside diagrams) is already met by `scripts/diagram_style.py`; no existing diagram was redrawn.
