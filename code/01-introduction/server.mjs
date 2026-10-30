// Nastavni backend, stanje nakon 1. tjedna: podaci u memoriji; bez baze, proxyja, TLS-a i autentikacije.
import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { resolve } from "node:path";

const products = [{ id: 7, name: "Bilježnica", price: 3.5 }];
export async function handleRequest(req, res) {
  const url = new URL(req.url, "http://127.0.0.1");
  const start = Date.now();
  res.on("finish", () =>
    console.log(
      JSON.stringify({
        method: req.method,
        path: url.pathname,
        scenario: url.searchParams.get("case") || "ok",
        status: res.statusCode,
        durationMs: Date.now() - start,
      }),
    ),
  );
  const json = (status, body) => {
    res.writeHead(status, {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    });
    res.end(JSON.stringify(body));
  };
  if (req.method !== "GET")
    return json(405, { error: "Samo GET u demonstraciji" });
  if (url.pathname === "/") {
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    return res.end(
      await readFile(new URL("./public/index.html", import.meta.url)),
    );
  }
  if (url.pathname !== "/products")
    return json(404, { error: "Ruta ne postoji" });
  const scenario = url.searchParams.get("case") || "ok";
  if (!["ok", "empty", "error", "slow", "html"].includes(scenario)) {
    return json(400, { error: "Nepoznat demonstracijski slučaj" });
  }
  if (scenario === "slow") await new Promise((r) => setTimeout(r, 2000));
  if (scenario === "error")
    return json(503, { error: "Simulirana nedostupnost ovisnosti" });
  if (scenario === "html") {
    res.writeHead(200, {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "no-store",
    });
    return res.end("<p>Namjerno neočekivan format umjesto JSON-a.</p>");
  }
  return json(200, scenario === "empty" ? [] : products);
}
if (
  process.argv[1] &&
  resolve(process.argv[1]) === fileURLToPath(import.meta.url)
) {
  const server = createServer((req, res) =>
    handleRequest(req, res).catch((error) => {
      console.error(error.message);
      if (!res.headersSent)
        res.writeHead(500, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("Greška demonstracijskog poslužitelja");
    }),
  );
  server.listen(Number(process.env.PORT || 3000), "127.0.0.1", () => {
    console.log(
      `Otvorite http://127.0.0.1:${server.address().port} — baza je simulirana.`,
    );
  });
}
