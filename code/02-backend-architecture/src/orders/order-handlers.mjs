// HTTP sloj za narudžbe: pretvara HTTP zahtjev u poziv servisa,
// a rezultat ili grešku servisa u HTTP status i JSON odgovor.
import { readJson, sendJson } from "../http.mjs";
import { ValidationError, OutOfStockError } from "./order-service.mjs";

export function createOrderHandlers({ orderService }) {
  return {
    async create(req, res) {
      const body = await readJson(req);
      try {
        const order = await orderService.placeOrder(body);
        return sendJson(res, 201, order);
      } catch (error) {
        if (error instanceof ValidationError) return sendJson(res, 400, { error: error.message });
        if (error instanceof OutOfStockError) return sendJson(res, 409, { error: error.message });
        throw error; // neočekivano: app.mjs vraća 500
      }
    },
  };
}
