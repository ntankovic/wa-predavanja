# Plan ilustracija — Implementacija i rad web aplikacije u produkciji

Planirano, nije nacrtano niti provjereno u izvozu.

| Ilustracija | Nastavna svrha | Smještaj | Podrijetlo | Status |
| --- | --- | --- | --- | --- |
| Završna arhitektura; rolling deployment i miješane verzije; graceful shutdown | Objasniti: Pratiti zahtjev kroz Vue → HTTPS/proxy/load balancer → više backend instanci → PostgreSQL, uz opcionalni cache i red → worker, tijekom rolling deploymenta. | Uskladiti s koracima skripte i nizom slajdova | Plan originalnog dijagrama; izvore tvrdnji tek provjeriti | planned |

Prije izrade razdvojiti ovu početnu ideju u zasebne ilustracije s jednom svrhom, označiti smjer i značenje strelica, sačuvati uređivi izvor u `assets/`, dodati alternativni tekst i provjeriti PDF i HTML.
