# Shared slides

Reveal.js configuration is in `revealjs.yml`. Build with `just slides 01-introduction hr`. Slides embed assets and use the FIPU logo, course footer, progress bar, definition boxes and table styling. Browser tab titles use WA-NN.

Use level-two headings for slides and fenced `.notes` blocks for concise teaching cues and timing. Keep editorial review notes in the lecture brief. Every deck has an attendance slide right after the title slide (lecturer decision, 2026-10-28): `## Evidencija prisutnosti {#attendance .attendance-slide}` with `assets/attendance-wa.png` linked to https://bit.ly/wa-tu-sam, 0.5 min, taken from the title slide's first minute. It is not inserted automatically: keep it in each `slides*.qmd`; `lectures/_template/` already contains it. The shared CSS is in `revealjs.yml`.

Shell commands on slides use the terminal look: inline `` `npm start`{.cmd} `` and multi-line ```` ```{.terminal code-line-numbers="false"} ```` blocks (CSS in `revealjs.yml`; rule in `COURSE.md`).
