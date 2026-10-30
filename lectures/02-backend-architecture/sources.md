# Sources and asset provenance — Predavanje 02

Pristup: 2026-10-27. **Mreža je u ovoj sesiji bila blokirana: nijedan vanjski izvor nije otvoren.** Svi URL-ovi i navodi u nastavku napisani su po znanju i moraju se provjeriti prije nastave.

## References (za provjeru)

| Izvor | URL | Podupire tvrdnju | Status |
| --- | --- | --- | --- |
| RFC 9110, 9.3.3 POST; 15.3.2 201 Created | https://www.rfc-editor.org/rfc/rfc9110.html | značenje POST i 201 | brojevi odjeljaka i sidra neprovjereni |
| Dijkstra, *On the role of scientific thought*, EWD447 (1974) | https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html | podrijetlo izraza *separation of concerns* | neprovjereno |
| Fowler, *PresentationDomainDataLayering* (2015) | https://martinfowler.com/bliki/PresentationDomainDataLayering.html | podjela na prikaz/domenu/podatke | neprovjereno |
| Fowler, *Repository* (PoEAA) | https://martinfowler.com/eaaCatalog/repository.html | pojam repozitorija | neprovjereno |
| Fowler, *Inversion of Control Containers and the Dependency Injection pattern* (2004) | https://martinfowler.com/articles/injection.html | ubrizgavanje ovisnosti | neprovjereno |
| Fowler, *MonolithFirst* (2015) | https://martinfowler.com/bliki/MonolithFirst.html | monolit kao polazište | neprovjereno |
| The Twelve-Factor App: III Config, VI Processes, IX Disposability | https://12factor.net/config · /processes · /disposability | konfiguracija iz okruženja, procesi bez stanja, brzo pokretanje i uredno gašenje | neprovjereno |
| OWASP Secrets Management Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html | rukovanje tajnama, rotacija | neprovjereno |
| Node.js: `--env-file` (od 20.6.0) | https://nodejs.org/api/cli.html#--env-fileconfig | učitavanje `.env` | ponašanje provjereno lokalno (20.11); URL neprovjeren |
| Node.js: `server.close()`, signal events, `node:test` | https://nodejs.org/api/http.html#serverclosecallback · https://nodejs.org/api/process.html#signal-events · https://nodejs.org/api/test.html | uredno gašenje, SIGINT/SIGTERM, test runner | ponašanje provjereno lokalno; tvrdnja „od Node 19 close() zatvara neaktivne veze” po znanju, ponašanje na 20.11 potvrđeno |
| Fastify: Routes, Server, Reply | https://fastify.dev/docs/latest/Reference/ | API u skici s32; parsiranje JSON-a, `app.close()`, 500 za neuhvaćenu grešku | **neprovjereno, skica nije pokrenuta** |

## Lokalno provjerene tvrdnje (Node.js v20.11.0, macOS)

- Naivni poslužitelj: `quantity: 2` → 201 (zaliha 5→3); `"2"` → 201 (3→1); `-3` → 201, ukupno −10.5, zaliha 1→4; prekinut JSON → `SyntaxError`, proces završava; odbijena narudžba „olovke 2 + ruksak 5” umanjuje olovke za 2.
- Strukturirani backend: 201 / 400 (e-pošta, količina, nepoznat proizvod, neispravan JSON) / 409 / 415 / 405 / 404; `NOTIFIER=fail` → 201 i zapis greške; `NOTIFIER=slow` → odgovor nakon ~3 s.
- `PORT=abc` i `NOTIFIER=email` → poruka i izlazni kod 1; drugi proces na zauzetom portu → `EADDRINUSE`, kod 1.
- Uredno gašenje: narudžba započeta u t=0, SIGINT u t=1 s, nova veza odbijena (curl exit 7), narudžba dovršena s 201 u t≈3 s, zatim „Svi zahtjevi dovršeni”, exit 0. S neaktivnom keep-alive vezom proces izlazi za ~0,2 s.
- Dva procesa (3023/3024 u testu; na slajdu 3000/3001): oba prodaju posljednji ruksak, oba vraćaju id 1.
- `npm test`: 5 testova, 0 neuspjelih, ~60 ms.
- `--env-file`: zapis pri pokretanju prikazuje `emailApiKey: '(postavljen)'`, ne vrijednost.

## Assets

Svi dijagrami su originalni (vidi `illustrations.md`); nema vanjskih slika ni preuzetih materijala.

## Claims requiring verification

- Fastify skica (s32) i tablica s33 (ugrađeno parsiranje, 415/400 za tijelo, `logger: true`, `app.close()`).
- Svi vanjski URL-ovi gore.
- PowerShell naredba `$env:PORT=3001; npm start`.
