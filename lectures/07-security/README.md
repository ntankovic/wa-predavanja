# Predavanje 07: Sigurnost web aplikacija

- English title: Web Application Security
- Owner: unassigned
- Status: planned
- Authoring language: Croatian
- Croatian content review: not started
- English translation review: not started
- Croatian revision translated: none; English files are structural placeholders only
- Intended duration: 105 minutes; adaptable within 90–120 minutes
- Target: approximately 30–40 substantive slides; current outline is not a full deck
- Prerequisites: Ishodi tjedana 1–6; prethodno stanje iste aplikacije.
- Incoming state: Enforce identity and object permissions.
- Outgoing state: Challenge trust boundaries

## Predloženi ishodi (terminologija i formulacije čekaju pregled)

- Prepoznati prekršenu pretpostavku povjerenja.
- Objasniti napad i ispravak na istom toku zahtjeva.
- Razlikovati validaciju, kodiranje izlaza i kontrolu pristupa.
- Procijeniti što CORS, HTTPS i druge zaštite jamče, a što ne.

## Scope supplied by the lecturer

Trust boundaries and untrusted client input; validation and output encoding; SQL injection; XSS; CSRF; CORS and same-origin policy; authentication/password attacks; broken access control; rate limiting; security headers; HTTPS; secrets; sensitive data exposure and logging; dependency vulnerabilities; OWASP Top 10 as a reasoning framework.

## Zahtjev, problem i obvezni primjer

Napasti prethodnu implementaciju narudžbi kontroliranim primjerima: SQL injection, pristup tuđem objektu i zahtjev preko druge web stranice.

Ranjiva implementacija → napad → ispravak; sigurnost povezati s arhitekturom i granicama povjerenja.

## Privremeni vremenski proračun

Ovo je plan za buduću razradu, a ne dokaz da postoji dovršen nastavni scenarij.

| Vrijeme | Aktivnost | Minute |
| --- | --- | --- |
| 00–10 | Ishodi, prethodna odluka i konkretan zahtjev | 10 |
| 10–25 | Problem, početno rješenje i predviđanje ponašanja | 15 |
| 25–45 | Izvršavanje korak po korak, ispad i uzrok | 20 |
| 45–70 | Poboljšani dizajn, jamstva i kompromisi | 25 |
| 70–95 | Analiza koda, zadatak u paru i rasprava | 25 |
| 95–105 | Sažetak, provjera ishoda i prijelaz | 10 |

Za 90 minuta skratiti aktivnost u paru s 25 na 10 minuta; za 120 dodati 15 minuta analize druge varijante scenarija. Pri pisanju pune skripte prilagoditi stvarnoj gustoći teme i unijeti vremenske oznake u bilješke. Tada izraditi `timing.json` po slajdovima; ukupno mora odgovarati `lecture.json`.

## Plan ilustracija

Granice povjerenja; slijed napada; usporedba ranjivog i ispravljenog koda. Razraditi svrhu i korake u `illustrations.md` prije punog nacrta.

## Izvori koje treba provjeriti

OWASP, HTTP/web-platform specifications, MDN, PostgreSQL and official security documentation. Ovo su kategorije za istraživanje, ne potvrđeni citati.

## Otvorena pitanja

- Hrvatski naslovi i ishodi trebaju jezični i sadržajni pregled.
- Primjer aplikacije za naručivanje je prijedlog; potvrditi pri razradi prvog predavanja.
- Odabrati verzije alata i provjeriti implementacijske tvrdnje pri pisanju.
- Izraditi punu skriptu, 30–40 sadržajnih slajdova, kod, dijagrame i provjerene izvore.

## Language workflow

Write `chapter.hr.qmd` and `slides.hr.qmd` first. After Croatian review, translate into `chapter.qmd` and `slides.qmd`. Record the source revision/date translated and any later changes requiring retranslation. Keep language-specific diagram labels and alternative text consistent.

## Review checklist

- [ ] Script supports 90–120 minutes and includes 3–6 explicit outcomes.
- [ ] Slides communicate one main idea each and map directly to the script.
- [ ] Important mechanisms follow problem → naive code → failure → reason → correction.
- [ ] A concrete execution is traced step by step where required.
- [ ] Misconceptions, student questions and AI-code review tasks are included.
- [ ] Concepts, patterns and product-specific behavior are distinguished.
- [ ] Continuity with the evolving application is explicit.
- [ ] Guarantees are attributed to the component actually providing them.
- [ ] `lecture.json` and `timing.json` agree with the brief and notes.

- [ ] Learning outcomes are covered by the chapter and slides.
- [ ] Chapter is understandable without the slides.
- [ ] Technical claims, examples, and sources have been checked.
- [ ] Assumptions, failure models, and tradeoffs are explicit where relevant.
- [ ] Exercises and discussion prompts align with the outcomes.
- [ ] Terminology and notation match the shared dictionary.
- [ ] Croatian chapter and slides have passed lecturer review.
- [ ] English translation reflects the recorded Croatian revision.
- [ ] Lecturer translation choices are recorded in the dictionary and applied consistently.
- [ ] Both language exports have passed visual review.
- [ ] Slide sequence and speaker notes support classroom teaching.
- [ ] Diagrams are readable and asset provenance is recorded.
- [ ] Essential visual steps are understandable in the static PDF as well as the slides.
- [ ] Timing totals 90–120 minutes, including student participation.
- [ ] Lecturer and faculty names are correct.
- [ ] Review findings and remaining issues are recorded below.

## Review notes

Pending.
