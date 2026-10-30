# Nastavni backend — Predavanje 02

Stanje nakon 2. predavanja (*Arhitektura backend aplikacije*). Polazi od `code/01-introduction`
i dodaje `POST /orders`, razdvojene odgovornosti, konfiguraciju iz okruženja i uredno gašenje.
Usporedba: `diff -r code/01-introduction code/02-backend-architecture`.

**Stanje: 2. tjedan.** I dalje bez vanjskih paketa i bez baze: proizvodi i narudžbe su u memoriji
procesa i nestaju pri restartu. Provjera i umanjenje zalihe nisu atomični (5. predavanje).

## Pokretanje

Node.js 20.6 ili noviji.

```sh
cd code/02-backend-architecture
npm start                 # http://127.0.0.1:3000
npm test                  # testovi servisa, bez HTTP-a
npm run naive             # NAMJERNO NAIVNA verzija za usporedbu (isti port 3000)
```

Konfiguracija (varijable okruženja; primjer u `.env.example`):

| Varijabla | Zadano | Značenje |
| --- | --- | --- |
| `PORT` | `3000` | port poslužitelja |
| `HOST` | `127.0.0.1` | adresa na kojoj sluša |
| `NOTIFIER` | `console` | simulirana e-pošta: `console`, `slow` (3 s), `fail` |
| `EMAIL_API_KEY` | — | primjer tajne; ne ispisuje se i ne koristi za stvarno slanje |

`cp .env.example .env` pa `npm run start:env` čita `.env` (Node `--env-file`). Datoteka `.env` je u `.gitignore`.

## Struktura

```text
server.mjs                     pokretanje: konfiguracija → sastavljanje ovisnosti → listen; gašenje
src/config.mjs                 čitanje i provjera konfiguracije
src/app.mjs                    usmjeravanje (metoda + putanja → handler), 404/405/500
src/http.mjs                   čitanje JSON tijela, slanje JSON odgovora
src/products/                  katalog (pristup podacima) i GET /products
src/orders/order-handlers.mjs  HTTP sloj za POST /orders
src/orders/order-service.mjs   poslovna pravila naručivanja
src/orders/memory-orders.mjs   pohrana narudžbi u memoriji
src/notifications/notifier.mjs simulirana e-pošta
naive/server-naive.mjs         sve u jednom handleru (za usporedbu)
test/order-service.test.mjs    testovi pravila s lažnim ovisnostima
```

## POST /orders

```sh
curl -i -X POST http://127.0.0.1:3000/orders \
  -H 'Content-Type: application/json' \
  -d '{"email":"ana@primjer.hr","items":[{"productId":7,"quantity":2}]}'
```

| Slučaj | Odgovor |
| --- | --- |
| ispravna narudžba | `201` i narudžba; cijena iz kataloga, ne iz zahtjeva |
| neispravna e-pošta, količina ili nepoznat proizvod | `400` |
| nedovoljna zaliha (npr. dva ruksaka) | `409` |
| tijelo nije JSON / nema `Content-Type: application/json` | `400` / `415` |
| neuspjela obavijest (`NOTIFIER=fail`) | `201`; greška se zapisuje u terminal |

Pravila statusa i oblik grešaka razrađujemo u 3. predavanju.

## Uredno gašenje

`Ctrl+C` (SIGINT) ili SIGTERM: poslužitelj prestaje primati nove veze, dovršava započete zahtjeve
i izlazi; nakon 10 s prekida. Isprobajte s `NOTIFIER=slow npm start`, pošaljite narudžbu i odmah pritisnite Ctrl+C.
