// Pokretanje i gašenje procesa. Ovo je jedino mjesto koje zna sve dijelove
// i spaja ih (composition root): konfiguracija → ovisnosti → HTTP poslužitelj.
import { createServer } from "node:http";
import { loadConfig, describeConfig } from "./src/config.mjs";
import { createApp } from "./src/app.mjs";
import { createMemoryCatalog } from "./src/products/memory-catalog.mjs";
import { createProductHandlers } from "./src/products/product-handlers.mjs";
import { createMemoryOrders } from "./src/orders/memory-orders.mjs";
import { createOrderService } from "./src/orders/order-service.mjs";
import { createOrderHandlers } from "./src/orders/order-handlers.mjs";
import { createNotifier } from "./src/notifications/notifier.mjs";

// 1. Konfiguracija: neispravna vrijednost zaustavlja pokretanje odmah.
let config;
try {
  config = loadConfig();
} catch (error) {
  console.error(`Neispravna konfiguracija: ${error.message}`);
  process.exit(1);
}

// 2. Sastavljanje ovisnosti: tko što dobiva.
const catalog = createMemoryCatalog();
const orderService = createOrderService({
  catalog,
  orders: createMemoryOrders(),
  notifier: createNotifier({ mode: config.notifier }),
});
const app = createApp({
  productHandlers: createProductHandlers({ catalog }),
  orderHandlers: createOrderHandlers({ orderService }),
});

// 3. Tek sada proces počinje primati zahtjeve.
const server = createServer(app);
server.on("error", (error) => {
  // Npr. EADDRINUSE: port već koristi drugi proces.
  console.error(`Pokretanje nije uspjelo: ${error.code} (${config.host}:${config.port})`);
  process.exit(1);
});
server.listen(config.port, config.host, () => {
  console.log(`Sluša na http://${config.host}:${config.port} (PID ${process.pid})`);
  console.log("Konfiguracija:", describeConfig(config));
});

// 4. Uredno gašenje: ne primaj nove veze, dovrši započete zahtjeve, zatim izađi.
function shutdown(signal) {
  console.log(`${signal}: ne primam nove zahtjeve, dovršavam započete…`);
  server.close(() => {
    console.log("Svi zahtjevi dovršeni. Izlazim.");
    process.exit(0);
  });
  setTimeout(() => {
    console.error("Gašenje traje predugo; prekidam.");
    process.exit(1);
  }, config.shutdownTimeoutMs).unref();
}
process.once("SIGINT", shutdown);
process.once("SIGTERM", shutdown);
