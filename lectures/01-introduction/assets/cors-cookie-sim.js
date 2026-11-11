// Simulator kolačića i CORS-a za Predavanje 01 (slajd s27b).
// Model namjerno pokriva samo osnovni slučaj: jednostavni zahtjevi (bez preflighta),
// fetch s credentials: 'same-origin' (zadano) ili 'include'. Ponašanje prema Fetch standardu i MDN-u.
(function () {
  const root = document.getElementById('cc-sim');
  if (!root) return;

  const API = 'http://localhost:3000';
  const CLIENTS = {
    same: { label: 'stranica s http://localhost:3000', origin: 'http://localhost:3000', browser: true },
    cross: { label: 'stranica s http://localhost:5173', origin: 'http://localhost:5173', browser: true },
    curl: { label: 'curl (izvan preglednika)', origin: null, browser: false },
  };
  const ACAO = {
    none: { label: 'ne šalje', value: null },
    vite: { label: 'http://localhost:5173', value: 'http://localhost:5173' },
    ip: { label: 'http://127.0.0.1:5173', value: 'http://127.0.0.1:5173' },
    any: { label: '*', value: '*' },
  };
  const CRED = {
    'same-origin': { label: "'same-origin' (zadano)" },
    include: { label: "'include'" },
  };
  const SID = 'abc123';
  const state = { client: 'same', acao: 'none', cred: 'same-origin', acac: false, jar: null };

  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const line = (text, cls) => `<div class="cc-line${cls ? ' ' + cls : ''}">${esc(text)}</div>`;
  const note = (text, cls) => `<div class="cc-note${cls ? ' ' + cls : ''}">${esc(text)}</div>`;

  function radios(name, options) {
    return Object.entries(options).map(([key, o]) =>
      `<label class="cc-opt"><input type="radio" name="${name}" value="${key}"${state[name] === key ? ' checked' : ''}><span>${esc(o.label)}</span></label>`
    ).join('');
  }

  root.innerHTML = `
    <div class="cc-controls">
      <fieldset><legend>Tko šalje zahtjev na :3000?</legend>${radios('client', CLIENTS)}</fieldset>
      <fieldset><legend>fetch(url, { credentials })</legend>${radios('cred', CRED)}</fieldset>
      <fieldset><legend>Backend šalje Access-Control-Allow-Origin</legend>${radios('acao', ACAO)}
        <label class="cc-opt cc-check"><input type="checkbox" name="acac"><span>Access-Control-Allow-Credentials: true</span></label></fieldset>
      <div class="cc-actions">
        <button type="button" data-path="/products">GET /products</button>
        <button type="button" data-path="/login">POST /login</button>
        <button type="button" data-path="/cart" class="cc-locked" title="Treba kolačić sesije (prijava)">GET /cart<svg class="cc-lock" viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4" fill="none"/></svg></button>
      </div>
      <div class="cc-jar"><div class="cc-jar-head"><span>Kolačići preglednika</span><button type="button" class="cc-clear">obriši</button></div><div class="cc-jar-body"></div></div>
    </div>
    <div class="cc-trace">
      <div class="cc-step"><h3>1 · Zahtjev</h3><div class="cc-out" data-step="req"></div></div>
      <div class="cc-step"><h3>2 · Backend</h3><div class="cc-out" data-step="srv"></div></div>
      <div class="cc-step"><h3>3 · Odgovor</h3><div class="cc-out" data-step="res"></div></div>
      <div class="cc-step"><h3>4 · Što dobiva naš kod</h3><div class="cc-out" data-step="js"></div></div>
    </div>`;

  const out = (step) => root.querySelector(`[data-step="${step}"]`);

  function renderJar() {
    root.querySelector('.cc-jar-body').innerHTML = state.jar
      ? line(`localhost  sid=${state.jar}`, 'cc-good') + note('Kolačić veže ime domaćina, ne port.')
      : note('prazno');
  }

  function clearTrace() {
    for (const s of ['req', 'srv', 'res', 'js']) out(s).innerHTML = note('Kliknite zahtjev.', 'cc-muted');
  }

  function send(path) {
    const client = CLIENTS[state.client];
    const method = path === '/login' ? 'POST' : 'GET';
    const crossOrigin = client.browser && client.origin !== API;
    // credentials: 'same-origin' šalje i prima kolačiće samo za isto podrijetlo; 'include' i za drugo.
    const include = state.cred === 'include';
    const credentials = client.browser && (!crossOrigin || include);
    const sentCookie = credentials && state.jar ? state.jar : null;

    // 1. Zahtjev
    let req = line(`${method} ${path} HTTP/1.1`, 'cc-strong') + line('Host: localhost:3000');
    if (client.browser && (crossOrigin || method === 'POST')) req += line(`Origin: ${client.origin}`, 'cc-hl');
    if (method === 'POST') req += line('Content-Type: application/x-www-form-urlencoded') + line('') + line('user=ana');
    if (sentCookie) req += line(`Cookie: sid=${sentCookie}`, 'cc-hl');
    if (!client.browser) req += note('curl ne dodaje Origin i sam ne pamti kolačiće; credentials ne postoji.');
    else if (crossOrigin && state.jar && !include) req += note('Kolačić postoji, ali fetch ga ne šalje na drugo podrijetlo bez credentials: \'include\'.', 'cc-warn');
    else if (!sentCookie && path === '/cart') req += note('Nema kolačića za poslati.');
    out('req').innerHTML = req;

    // 2. Backend: uvijek obradi zahtjev; ne zna ni za kakav CORS „blok”.
    let status, body, setCookie = null, srv;
    if (path === '/products') {
      status = 200; body = '[{"id":1,"name":"ruksak"}]';
      srv = note('Javni podaci, nije potrebna prijava.');
    } else if (path === '/login') {
      status = 200; body = '{"user":"ana"}'; setCookie = `sid=${SID}`;
      srv = note('Stvara sesiju sid=abc123 za korisnicu ana.');
    } else if (sentCookie === SID) {
      status = 200; body = '{"items":["ruksak"]}';
      srv = note('Preko sid=abc123 pronalazi sesiju i košaricu.', 'cc-good');
    } else {
      status = 401; body = '{"error":"Niste prijavljeni"}';
      srv = note('Bez kolačića ne zna čija je košarica.', 'cc-warn');
    }
    const reason = status === 200 ? 'OK' : 'Unauthorized';
    out('srv').innerHTML = line(`${method} ${path} → ${status}`, 'cc-strong') + srv + note('Zahtjev je obrađen bez obzira na CORS.');

    // 3. Odgovor
    const acao = ACAO[state.acao].value;
    let res = line(`HTTP/1.1 ${status} ${reason}`, status === 200 ? 'cc-strong' : 'cc-strong cc-bad')
      + line('Content-Type: application/json');
    if (acao) res += line(`Access-Control-Allow-Origin: ${acao}`, 'cc-hl');
    if (state.acac) res += line('Access-Control-Allow-Credentials: true', 'cc-hl');
    if (setCookie) res += line(`Set-Cookie: ${setCookie}`, 'cc-hl');
    res += line('') + line(body);
    out('res').innerHTML = res;

    // 4. Preglednik i naš JavaScript
    let js = '';
    if (!client.browser) {
      js = line(body, status === 200 ? 'cc-good' : 'cc-bad') + note('curl ne provodi CORS: tijelo je uvijek čitljivo.');
    } else {
      if (setCookie) {
        if (credentials) { state.jar = SID; js += note('Preglednik sprema sid=abc123.', 'cc-good'); }
        else js += note('Set-Cookie zanemaren: odgovor drugog podrijetla bez credentials.', 'cc-warn');
      }
      // Uz credentials: 'include' * ne vrijedi; treba točno podrijetlo i Allow-Credentials: true.
      const originOk = include ? acao === client.origin : (acao === '*' || acao === client.origin);
      const allowed = !crossOrigin || (originOk && (!include || state.acac));
      if (!crossOrigin) {
        js += line(`res.status → ${status}`, status === 200 ? 'cc-good' : 'cc-bad') + line(body) + note('Isto podrijetlo: CORS se ne provjerava.');
      } else if (allowed) {
        js += line(`res.status → ${status}`, status === 200 ? 'cc-good' : 'cc-bad') + line(body)
          + note(status === 200 ? `Dopušteno: ${acao === '*' ? '* za svako podrijetlo' : 'podrijetlo se točno podudara'}${include ? ', uz Allow-Credentials' : ''}.` : 'CORS dopušta čitanje, ali korisnik nije prijavljen.', status === 200 ? '' : 'cc-warn');
      } else {
        js += line('TypeError: Failed to fetch', 'cc-bad')
          + note(!acao ? 'Nema Access-Control-Allow-Origin: preglednik ne predaje odgovor.'
            : include && acao === '*' ? "Uz credentials: 'include' * nije dovoljan: treba točno podrijetlo."
            : acao !== client.origin && acao !== '*' ? `${acao} ≠ ${client.origin}: podrijetlo se mora točno podudarati.`
            : "Uz credentials: 'include' treba i Access-Control-Allow-Credentials: true.", 'cc-warn')
          + (sentCookie ? note('Pazite: kolačić je poslan i backend je zahtjev već obradio.', 'cc-warn') : '');
      }
    }
    out('js').innerHTML = js;
    renderJar();
  }

  root.addEventListener('change', (e) => {
    if (e.target.name in state) { state[e.target.name] = e.target.type === 'checkbox' ? e.target.checked : e.target.value; clearTrace(); }
  });
  root.addEventListener('click', (e) => {
    const b = e.target.closest('button');
    if (!b) return;
    if (b.classList.contains('cc-clear')) { state.jar = null; renderJar(); clearTrace(); return; }
    if (b.dataset.path) send(b.dataset.path);
  });
  // Tipke na kontrolama ne smiju mijenjati slajd.
  root.addEventListener('keydown', (e) => e.stopPropagation());

  renderJar();
  clearTrace();
})();
