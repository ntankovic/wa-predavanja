// Test poslovnih pravila bez HTTP poslužitelja, mreže i e-pošte:
// servis dobiva lažne (fake) ovisnosti koje sami složimo.
import { test } from "node:test";
import assert from "node:assert/strict";
import { createOrderService, OutOfStockError, ValidationError } from "../src/orders/order-service.mjs";
import { createMemoryCatalog } from "../src/products/memory-catalog.mjs";
import { createMemoryOrders } from "../src/orders/memory-orders.mjs";

function setup({ notifier } = {}) {
  const sent = [];
  const catalog = createMemoryCatalog();
  const service = createOrderService({
    catalog,
    orders: createMemoryOrders(),
    notifier: notifier ?? { orderPlaced: async (order) => sent.push(order.id) },
    log: { error() {} },
  });
  return { service, catalog, sent };
}

test("cijena dolazi iz kataloga, ne iz zahtjeva", async () => {
  const { service } = setup();
  const order = await service.placeOrder({ email: "a@b.hr", items: [{ productId: 7, quantity: 2, price: 0.01 }] });
  assert.equal(order.total, 7);
});

test("nedovoljna zaliha baca OutOfStockError i ne mijenja zalihu", async () => {
  const { service, catalog } = setup();
  await assert.rejects(service.placeOrder({ email: "a@b.hr", items: [{ productId: 9, quantity: 2 }] }), OutOfStockError);
  assert.equal((await catalog.findById(9)).stock, 1);
});

test("neispravna količina je ValidationError", async () => {
  const { service } = setup();
  await assert.rejects(service.placeOrder({ email: "a@b.hr", items: [{ productId: 7, quantity: -2 }] }), ValidationError);
});

test("neuspjela obavijest ne poništava spremljenu narudžbu", async () => {
  const { service } = setup({ notifier: { orderPlaced: async () => { throw new Error("pala"); } } });
  const order = await service.placeOrder({ email: "a@b.hr", items: [{ productId: 8, quantity: 1 }] });
  assert.equal(order.id, 1);
});

test("uspješna narudžba šalje jednu obavijest", async () => {
  const { service, sent } = setup();
  await service.placeOrder({ email: "a@b.hr", items: [{ productId: 8, quantity: 3 }] });
  assert.deepEqual(sent, [1]);
});
