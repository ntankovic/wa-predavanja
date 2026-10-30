# Course introduction and assessment

- Number: 00
- Owner: coordinating agent
- Status: review (historical assessment rules need lecturer confirmation)
- Format: slides only; no chapter and no inclusion in the student book
- Languages: Croatian draft (`slides.hr.qmd`) and existing English reference (`slides.qmd`)
- Duration: 20 minutes including questions, separate from Lecture 01's 60 minutes
- Deliverable: 14-slide orientation deck with speaker notes

## Purpose

Introduce learning goals, the course sequence, practical work, assessment, participation, and help. Historical 2022/23 rules are visibly labelled. Study suggestions are not an official marking rubric. Current deadlines, grading, retakes, channels, and collaboration/attribution rules remain unresolved. AI-use policy was supplied by the lecturer on 2026-09-17.

## Timing

- 00–00:30: Course introduction and assessment
- 00:30–01:30: Attendance and participation
- 01:30–02: Mark your presence (shared slide)
- 02–03: Teaching staff and course obligations
- 03–04: What this course is about
- 04–06: The route through the course
- 06–07: From lectures to practical work
- 07–08: Project preparation
- 08–09: Course information and help
- 09–12: How to pass the course (BPMN)
- 12–13: Submission, exemption, and defence
- 13–16: Prepare to explain your project
- 16–18: AI use and your responsibility
- 18–20: Before the first technical lecture

## Build

`just slides 00-course-introduction`

`just browser-check 00-course-introduction`

`just all` includes the deck. `just lecture 00-course-introduction` intentionally has no PDF chapter to build. `lecture.json` declares the slides-only format and 20-minute timing exception.

## Review

- [x] Extracted administrative statements mapped to original pages.
- [x] Historical rules distinguished from current confirmed requirements.
- [x] No invented weights, deadlines, retake rules, or current contact links.
- [x] Rendered-output verification complete: all 14 slides visually reviewed; headless Chrome passed with no overflow, missing images, or JavaScript errors. Structural checks confirm 20-minute timing and exclusion from the book. Build-all dispatch checked for 12 chapter PDFs, 13 decks, and one book.
- [ ] Lecturer has confirmed the current policy and student-facing links.

Attendance update (2026-09-17): the shared build adds presence check-in as slide 2. Welcome and check-in together occupy 00–01 min; subsequent teaching segments retain their timing.

2026-09-17 source review: added the lecturer-supplied BPMN original and the confirmed staff responsibility split. English process summary remains pending translation review. Luka’s full name/title confirmed: Luka Blašković, mag. inf. Current calendar dates and grading weights remain unresolved.

AI policy review: lecturer-approved substance recorded in `sources.md`; Croatian wording in `ai-policy.hr.md`, English slide wording pending lecturer review. The orientation remains 20 minutes.

Editorial separation (2026-09-17): internal review comments moved to `design-review.md`, which is excluded from exports. Speaker notes now contain teaching cues, timing, and diagram attribution. Unconfirmed attendance requirements are recorded only in the internal review file.

Visual update (2026-09-17): added five original diagrams for practical examples, attendance, course completion, deadlines, and AI responsibility. Editable bilingual SVG sources and vector PDF derivatives are in `assets/`. HTML layout and PDF figure renders reviewed; the 14-slide / 20-minute structure is preserved. English diagram labels remain pending lecturer review.

2026-09-17: lecture 00 only places the attendance explanation on slide 2 and QR check-in on slide 3. Attendance is optional, as confirmed by the lecturer. Other decks retain QR check-in on slide 2.

2026-09-17: removed the simplified course-completion overview at the lecturer’s request. The original BPMN is the sole course-passing diagram and receives the removed slide’s minute; total remains 20 minutes across 14 slides.

## Croatian translation review, 2026-09-17

- Direction: English → Croatian, explicitly requested by the lecturer to establish the Croatian source for review.
- Source revision: `slides.qmd` as present on 2026-09-17, including optional attendance, current help channels, and corrected defence timing. This workspace has no Git metadata.
- Croatian content/language review: pending lecturer review.
- English translation review: pending; existing English remains a reference, not an approved translation of the new Croatian draft.
- Timing: the same 14 slides and 20-minute outline above, including the shared QR slide at 01:30–02 min. All teaching notes and alternative text translated; existing Croatian diagram variants reused.
- [x] Slide-by-slide coverage, links, source attribution, and confirmed policy checked against the supplied English deck and local confirmation record.
- [x] `just slides 00-course-introduction hr` completed.
- [x] `just browser-check 00-course-introduction hr` passed for all 14 slides, with no overflow, missing images, or runtime errors. All slide screenshots visually reviewed.
- [x] Croatian title, footer, diagram selection, and QR timing checked in generated HTML.
- [ ] Lecturer review of Croatian wording, especially provisional terminology in `references/terminology.md`.
- [ ] Resolve the preserved original BPMN image's superseded 7-day rule and calendar-day wording before classroom release. The following deadline slide and notes use the current rule: at least 3 working days before defence, defence by exam day. No policy was invented during translation.

Build the Croatian deck with `just slides 00-course-introduction hr`; verify with `just browser-check 00-course-introduction hr`. Lecture 00 has no chapter/PDF chapter by design. Existing diagram PDF derivatives were unchanged in this translation pass.

2026-09-17 terminology review: lecturer chose **Proces 1/2** instead of **Radnik 1/2** in the practical-work diagram. Updated editable source, Croatian/English SVG and PDF derivatives, and slide alternative text. English **Process 1/2** remains pending translation review.

2026-09-17 terminology review: lecturer approved **ispad** instead of **otkaz**. Applied throughout Croatian Lecture 00; English continues to use **failure**.

2026-09-18 wording review: lecturer approved the course-overview row “Sigurnost i procjena arhitekture” with “Koja jamstva sustav može pružiti i pod kojim pretpostavkama?”. English row aligned; translation review pending. Slide count and 20-minute timing unchanged.

2026-09-18 project-work wording: lecturer approved “Rad na projektu: Postavi problem → predloži rješenje → implementiraj → testiraj i doradi”. Added spacing between steps and before the diagram; notes clarify applicability to practical-class tasks and iteration. English aligned, pending language review.

2026-09-18: renamed the preparation slide to “Priprema za projekt” / “Project preparation” to clarify the purpose of the prerequisite checklist.
