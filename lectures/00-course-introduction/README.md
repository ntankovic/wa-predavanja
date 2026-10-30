# Lecture 00 — Web aplikacije: uvod i pravila polaganja

- Owner: lecturer; adaptation by the current authoring session
- Status: drafting; Croatian lecturer review pending
- Format: slides only, excluded from the 12 technical weeks and student book
- Timing: 26 slides, 24 minutes (Croatian, 2026-10-13); per-slide plan in `timing.json` and Croatian notes
- Croatian: adapted to COURSE.md and four lecturer-approved assessment rules
- English: inherited Distributed Systems deck; translation deferred until Croatian review. Do not use the English export for Web Applications.

## Scope and sources

Course identity is Web aplikacije / Web Applications. Staff remains Nikola Tanković and Luka Blašković. Source and exact approval scope are recorded in `sources.md`. The legacy PDF is from 2021/22; it was inspected in place and not copied. No unapproved PDF images, workflow, grading criteria or links are incorporated.

The 20-minute orientation is an explicit exception to full lecture timing and chapter requirements. It introduces the backend-focused 12-week course, prerequisites, teaching stack, confirmed project/exam rules, AI-assisted verification and discussion.

## Pending lecturer decisions

- Numerical team-size limit.
- Remaining student links (course materials and submission).

Confirmed communication: Google Chat **FIPU WA**. Attendance check-in: https://bit.ly/wa-tu-sam.
- Project specification, grading criteria and calendar milestones.
- Whether to reuse the legacy requirements/prototype/modelling workflow.
- Which Web aplikacije lectures are recorded (lecturer, 2026-10-13: "some / not decided"). Slides 4–5 use neutral wording until confirmed.
- Confirm wording on slides 4–5: "Ako samo slušate, oni vam mogu biti jednako dobri" and the "usmjereni na ocjenu" row.
- Review Croatian content; then translate to English and review translation separately.

## Review checklist

- [x] Replace course identity, sequence and prerequisites.
- [x] Retain confirmed teaching staff.
- [x] Incorporate only the four explicitly approved legacy administrative rules.
- [x] Remove inherited RS attendance link/QR and unconfirmed administrative claims from Croatian slides.
- [x] Align AI-use guidance with COURSE.md.
- [x] Plan 20 minutes with per-slide notes and timing.json.
- [x] Verify Croatian HTML visually (headless browser screenshots, 2026-10-13).
- [ ] Verify Croatian slide PDF visually.
- [ ] Lecturer Croatian content review.
- [ ] Translate reviewed Croatian source; verify both languages and obtain translation review.

## Build

```sh
just slides 00-course-introduction hr
just browser-check 00-course-introduction hr
```

## Verification — 2026-10-06

Source checks passed: 16 slides, 16 timing entries, contiguous 20-minute schedule, notes for every slide, no inherited RS links or exemption threshold. `just slides 00-course-introduction hr` could not run because Quarto is absent. The workspace also has no `.tools/qa-venv`. HTML/PDF rendering and visual QA remain pending; existing output files predate this adaptation and must not be treated as updated exports.

## Oral examination update — 2026-10-06

Adapted to the lecturer-supplied oral examination document: explicit knowledge scope, project demonstration, live code changes, and concrete verification of AI-assisted code. The three preparation slides share the previous 3.5-minute block; total remains 20 minutes. Source-page mapping is in sources.md. Database choice resolved: both PostgreSQL and MongoDB basics are covered; students choose either for their project. Resolve Express.js exam coverage versus possible Fastify teaching examples, and provide a student-facing URL for the question document. Croatian content review and English translation remain pending.

2026-10-06 — Inserted lecturer-supplied original attendance QR PNG, linked to https://bit.ly/wa-tu-sam. QR image and link require rendered HTML/PDF QA when build tools are available. No new slide or timing change.

## Build recovery — 2026-10-06

Supersedes the missing-Quarto limitation above: Quarto 1.10.18 is installed locally under `.tools/quarto`; `just slides 00-course-introduction hr` succeeded and updated `output/hr/slides/00-course-introduction.html`. Browser-check dependencies are installed under `.tools/qa-venv`, but `just browser-check 00-course-introduction hr` fails at Chrome startup (SIGABRT). Visual HTML/PDF QA is still pending; the HTML now contains the latest Croatian changes.

2026-10-06 — Lecturer approved matching RS 00 layout. Restored separate large QR slide and attendance illustration, reused existing attributed AI artwork; added original editable request/evidence/live-change SVGs with vector PDF derivatives in assets/build_wa_diagrams.py. 17 slides, 20 minutes. Previously recorded 16-slide counts are superseded.

2026-10-07 — Plan nastave proširen na četiri slajda, po tri predavanja s kratkim opisima prema COURSE.md. Aktualna hrvatska verzija ima 19 slajdova i zadržava 20 minuta; timing.json i bilješke usklađeni. Engleska prilagodba i potpuna provjera u pregledniku ostaju na čekanju.

2026-10-07 — Four syllabus slides restyled as three pale cards each, with separate week badges, consistent spacing and scoped typography. Content and timing unchanged. Just HTML build and 12-card structure check pass; full visual browser review still requires the missing headless shell.

2026-10-07 — Added prerequisite icons, fictional Git history/counts, working-day calendar and AI tools slide after AI responsibility. Current HR deck: 20 slides / 20 minutes, timing and notes aligned. SVG illustrations visually inspected; just build checked; full headless HTML QA remains blocked by missing browser.

2026-10-07 — Lecturer requested previous-app extension option (minimum grade 4, by request) and imaginative AI project ideas. Added eligibility slide plus three slides with 12 original end-user AI concepts and concrete backend scope. HR orientation now 24 slides / 24 minutes, timings and metadata updated. Suggestions are optional; technology-approval rule retained.

2026-10-13 — Adapted the RS "why attend" slides and related RS decisions, approved by the lecturer for this course:

- New slides 4–5 after the QR slide and before Nastavnici: "Što predavanje daje, a AI i materijali ne daju?" (1 min) and "Različiti studenti, različiti razlozi" (0.5 min). Adapted, not copied: recordings are undecided for WA, so the wording is "materijali i, gdje postoje, snimke" rather than "sva su predavanja snimljena" or "snimke kao punu zamjenu"; question channel is Google Chat FIPU WA; WA has a project defence and an oral exam, so the cards and the "usmjereni na ocjenu" row name both.
- Order: AI rules and Preporučeni AI alati now open the project part, followed by commits, previous-app extension, AI project ideas, submission rules, oral exam and defence.
- Commits: "nekoliko commitova tjedno kroz najmanje 2–3 tjedna, uz provjeru autentičnosti" replaces the earlier note that no commit frequency is required.
- AI in project: slide 14 states that AI chat logs are not submitted; commits and the defence suffice. Notes mention an optional "Uporaba AI-ja" README section.
- "Izmjena koda uživo" replaced by "Dorada projekta: objasnite izmjenu" (Gdje? → Kako? → Posljedice?) with three WA example questions. New diagram `assets/wa-design-change.hr.svg`/`.pdf` from `build_wa_diagrams.py` (shared `diagram_style.py` cards). `wa-change.hr.*` is kept but unused.
- `assets/lecture.css`: RS design tokens (28/23/20 px, single accent #105d80, one card style #f3f8fb/#d4e3ec/14 px, links without Reveal blue, slide-number fix), plus figure captions at the small size. Rules used only by the inherited English deck were kept.
- Timing stays 24 minutes: Predaja i polaganje 2 → 1.5, Pokažite razumijevanje projekta 1.5 → 1, Pitanja i sljedeće predavanje 1 → 0.5. `timing.json` and all "Vrijeme:" notes were regenerated for the new order.
- Checks: `just slides 00-course-introduction hr` and `just browser-check 00-course-introduction hr` pass (26 slides; headless shell installed with `just browser-install`). Screenshots of slides 2, 4–6, 8, 12, 14–18, 21, 24 and 25 were reviewed. The slide PDF was not checked. English remains the inherited RS deck and is now further behind the Croatian version.

2026-10-14: koraljni detalji kao u BA uvodu, uz zadržanu paletu: --coral #e4572e, samo ukrasno. Crta ispod naslova (centrirana na slajdu evidencije prisutnosti, izostavljena na BPMN slajdu) i traka slijeva na karticama. Prijašnji CSS spremljen je u scratchpad BA sesije. Headless provjera (hr): PASS.
