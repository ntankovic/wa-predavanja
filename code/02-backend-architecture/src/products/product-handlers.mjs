// HTTP sloj za proizvode. Nema poslovnih pravila, pa nema ni servisa:
// handler izravno pita katalog. Scenariji ?case= ostaju iz 1. predavanja.
import { sendJson } from "../http.mjs";

export function createProductHandlers({ catalog }) {
  return {
    async list(req, res, url) {
      const scenario = url.searchParams.get("case") || "ok";
      if (!["ok", "empty", "error", "slow", "html"].includes(scenario)) {
        return sendJson(res, 400, { error: "Nepoznat demonstracijski slučaj" });
      }
      if (scenario === "slow") await new Promise((r) => setTimeout(r, 2000));
      if (scenario === "error") return sendJson(res, 503, { error: "Simulirana nedostupnost ovisnosti" });
      if (scenario === "html") {
        res.writeHead(200, { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store" });
        return res.end("<p>Namjerno neočekivan format umjesto JSON-a.</p>");
      }
      return sendJson(res, 200, scenario === "empty" ? [] : await catalog.list());
    },
  };
}
