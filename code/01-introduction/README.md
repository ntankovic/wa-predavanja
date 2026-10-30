# Nastavni backend — Predavanje 01

Stanje nastavnog backenda za 1. predavanje. Svako predavanje ima vlastitu kopiju
u `code/NN-naziv`; kasnije kopije polaze od ove i dodaju strukturu, API ugovor, bazu…

**Stanje: 1. tjedan.** Jedan Node.js program bez vanjskih paketa.
Proizvodi su zapisani u memoriji; prave baze, proxyja, HTTPS-a ni prijave još nema.

## Pokretanje

Potreban je [Node.js](https://nodejs.org/) 20 ili noviji (`node --version`).

```sh
cd code/01-introduction
npm start
```

Poslužitelj sluša na `http://127.0.0.1:3000` (samo na vlastitom računalu).
Drugi port: `PORT=3001 npm start` (Windows PowerShell: `$env:PORT=3001; npm start`).
Zaustavljanje: Ctrl+C.

## Što poslužitelj odgovara

| Zahtjev | Odgovor |
| --- | --- |
| `GET /` | HTML stranica s gumbima za dohvat (`public/index.html`) |
| `GET /products` | `200`, JSON niz proizvoda |
| `GET /products?case=empty` | `200`, prazan niz |
| `GET /products?case=slow` | `200` nakon 2 sekunde |
| `GET /products?case=error` | `503`, simulirana nedostupnost ovisnosti |
| `GET /products?case=html` | `200`, namjerno HTML umjesto JSON-a |
| druga putanja | `404` |
| druga metoda | `405` |

Svaki zahtjev ispisuje se u terminal kao jedan JSON redak (metoda, putanja, status, trajanje).

## Ručni HTTP zahtjev

U drugom terminalu:

| Sustav | Naredba |
| --- | --- |
| macOS | `nc -c 127.0.0.1 3000` |
| Linux | `nc -C 127.0.0.1 3000` (netcat-openbsd ili ncat), inače `telnet 127.0.0.1 3000` |
| Windows | `telnet 127.0.0.1 3000` (uključiti značajku Telnet Client) |

Zatim utipkati i završiti praznim retkom:

```
GET /products HTTP/1.1
Host: 127.0.0.1

```
