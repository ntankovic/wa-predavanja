# Plan ilustracija — Arhitektura backend aplikacije

Svi dijagrami su originalni, generira ih `assets/build_diagrams.py` (SVG za slajdove, vektorski PDF za skriptu) uz `scripts/diagram_style.py`. Provjereni u HTML slajdovima (headless Chrome) i u PDF-u skripte.

| Datoteka | Nastavna svrha | Smještaj | Status |
| --- | --- | --- | --- |
| `one-handler` | Sedam redaka naivnog handlera → posao → razlog za promjenu | s08 | nacrt |
| `layers` | Tko koga poziva nakon podjele | s09 / s09b | nacrt |
| `order-sequence` | `POST /orders` kroz handler, servis, katalog, pohranu i obavijest | s15 | nacrt |
| `dependency-direction` | Servis dobiva ovisnosti; samo `server.mjs` bira implementacije | s18 | nacrt |
| `swap-implementation` | Memorija / PostgreSQL / lažni katalog iza istih funkcija | s21 | nacrt |
| `lifecycle` | Pokretanje, rad, uredno gašenje i izlazi s greškom | s26 | nacrt |
| `shutdown-timeline` | Izmjereno uredno gašenje (NOTIFIER=slow, Ctrl+C u 1 s) | s27 | nacrt; vrijednosti izmjerene lokalno |
| `two-processes` | Dva procesa prodaju isti posljednji ruksak | s28 | nacrt; ishod izmjeren lokalno |
| `modular-monolith` | Jedan proces, moduli s malim javnim sučeljem | s31 | nacrt |

Strelice: puna = poziv, isprekidana = povratna vrijednost ili „ostvaruje”, crvena = greška/izlaz s greškom. Vrijeme na dijagramima slijeda teče prema dolje.
