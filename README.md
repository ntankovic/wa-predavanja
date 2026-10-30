# Web Applications course starter

Reusable course base for **Web aplikacije / Web Applications**, retaining FIPU branding and lecturer identity. Includes Croatian/English templates, lecture briefs and review checklists, figure/source tracking, Quarto lecture and book PDFs, Reveal.js slides, and verification utilities.

This is a defined teaching plan and scaffolding, not reviewed teaching material. The lecturer-supplied 12-week backend engineering sequence is in `COURSE.md`; all 12 lecture directories are planned scaffolds. Assessment and student links remain to be defined. Start with `COURSE.md`, `AGENTS.md`, and `references/terminology.md`.

## Setup (macOS)

```sh
brew install just
brew install --cask quarto
quarto install tinytex  # only if no LaTeX distribution is installed
python3 -m venv .tools/qa-venv
source .tools/qa-venv/bin/activate
python -m pip install -r requirements-qa.txt
just check
```

Python 3, Quarto, Just and XeLaTeX are required for builds. QA uses PyMuPDF and Playwright with installed Google Chrome (`CHROME_BIN` can override its location). Dependencies and virtual environments are not bundled. `QUARTO_BIN` can point to a portable Quarto executable; `COURSE_QA_PYTHON` can override the browser QA interpreter.

## Build

```sh
just render 01-introduction hr
just book hr
just render 01-introduction en
just book en
just test
just language-check 01-introduction
just browser-check 01-introduction hr
just preview 01-introduction hr
```

Commands default to English; Croatian uses an explicit `hr`. Outputs go to `output/`, or `output/hr/`. `just test` verifies English exports structurally; review PDFs and HTML visually in both languages. Passing a build does not approve content or validate a complete 90–120-minute teaching script.

## Develop the course

1. Follow the 12-week syllabus in `COURSE.md`; record ownership and status in `lectures/README.md`.
2. Develop the 12 numbered scaffolds in sequence. Use `lectures/_template/` for any agreed additions.
3. Write Croatian chapters and slides first; review before translating to English. Record language review separately. Set `scaffold: false` and `status: drafting` in `lecture.json` when replacing the outline with teaching content; add per-slide timing and match the declared duration.
4. Plan 90–120 minutes in each brief and slide notes, including discussion and recap. Keep assets, editable diagram sources, provenance and references beside the lecture.
5. Add each chapter to `publishing/book/_quarto.yml` in teaching order. Build and review both language outputs before marking a lecture ready.

All 12 lectures contain structural placeholders, not complete teaching material. The book assembly order includes all 12 to exercise the publishing pipeline. Each lecture brief has a provisional 105-minute planning budget; full scripts and 30–40 substantive slides remain to be written. Technical lectures from the original course, its bibliography, generated exports and local tools were excluded. Lecture 00 was subsequently copied at the lecturer’s request with its assets, administrative content, old links and source review history for adaptation. Shared logo provenance is in `assets/shared/README.md`. Every deck has an attendance QR slide (https://bit.ly/wa-tu-sam) right after the title slide; see `publishing/slides/README.md`.

## Current plan

The recurring question is “What actually happens when this request reaches the backend?” The stack is Vue 3/Pinia → REST API → Node.js (Fastify may be used) → PostgreSQL. Teach transferable backend principles through one evolving application. See `COURSE.md` for the full weekly scope, AI-assisted learning approach and correctness requirements.

The 2026-10-06 update supersedes the original starter’s 60-minute duration and single placeholder lecture. It does not modify the source Distributed Systems course.

## Orientation to adapt

[Lecture 00](lectures/00-course-introduction/README.md) is copied from the source course and remains separate from the 12 technical weeks and book. Its inherited course title, policies, old attendance link and review records need adaptation. Build with `just slides 00-course-introduction hr`.
