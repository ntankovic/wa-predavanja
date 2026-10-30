// Pomoćne funkcije HTTP sloja: čitanje JSON tijela i slanje JSON odgovora.
export class HttpError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

export async function readJson(req) {
  const type = req.headers["content-type"] ?? "";
  if (!type.startsWith("application/json")) {
    throw new HttpError(415, "Tijelo mora biti JSON (Content-Type: application/json)");
  }
  let text = "";
  for await (const chunk of req) text += chunk;
  try {
    return JSON.parse(text);
  } catch {
    throw new HttpError(400, "Tijelo nije valjan JSON");
  }
}

export function sendJson(res, status, body) {
  res.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store",
  });
  res.end(JSON.stringify(body));
}
