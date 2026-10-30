# Kod uz predavanja — Web aplikacije

Svako predavanje ima vlastitu, samostalnu kopiju nastavnog backenda u istoimenoj mapi.
Kopija sljedećeg predavanja polazi od prethodne i mijenja samo ono što predavanje uvodi,
pa se stanja mogu usporediti (npr. `diff -r 01-introduction 02-backend-architecture`).

| Mapa | Predavanje | Pokretanje |
| --- | --- | --- |
| [01-introduction](01-introduction/) | Klijent, poslužitelj i HTTP | `cd code/01-introduction` → `npm start` |
| [02-backend-architecture](02-backend-architecture/) | Arhitektura backend aplikacije | `cd code/02-backend-architecture` → `npm start` |

Potreban je Node.js 20 ili noviji (od predavanja 02: 20.6+ zbog `--env-file`).
