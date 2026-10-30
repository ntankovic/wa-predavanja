// Usmjeravanje (routing): metoda + putanja → handler. Ne sadrži poslovna pravila.
import { readFile } from "node:fs/promises";
import { HttpError, sendJson } from "./http.mjs";

export function createApp({ productHandlers, orderHandlers, log = console }) {
  const routes = {
    "GET /": serveIndex,
    "GET /products": productHandlers.list,
    "POST /orders": orderHandlers.create,
  };

  return async function handleRequest(req, res) {
    const url = new URL(req.url, "http://127.0.0.1");
    const start = Date.now();
    res.on("finish", () =>
      log.log(JSON.stringify({ method: req.method, path: url.pathname, status: res.statusCode, durationMs: Date.now() - start })),
    );
    const handler = routes[`${req.method} ${url.pathname}`];
    try {
      if (handler) return await handler(req, res, url);
      const pathExists = Object.keys(routes).some((key) => key.endsWith(` ${url.pathname}`));
      return sendJson(res, pathExists ? 405 : 404, { error: pathExists ? "Metoda nije podržana" : "Ruta ne postoji" });
    } catch (error) {
      if (error instanceof HttpError) return sendJson(res, error.status, { error: error.message });
      log.error(error);
      if (!res.headersSent) sendJson(res, 500, { error: "Neočekivana greška poslužitelja" });
    }
  };
}

async function serveIndex(req, res) {
  res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  res.end(await readFile(new URL("../public/index.html", import.meta.url)));
}
