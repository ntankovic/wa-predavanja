// NAMJERNO NAIVNO — prva verzija POST /orders, sve u jednom handleru.
// Radi za ispravan zahtjev, ali miješa HTTP, pravila, podatke i obavijest,
// a neispravan unos prolazi ili ruši proces. Služi za usporedbu sa src/.
import { createServer } from "node:http";

const products = [
  { id: 7, name: "Bilježnica", price: 3.5, stock: 5 },
  { id: 8, name: "Olovka", price: 0.8, stock: 20 },
  { id: 9, name: "Ruksak", price: 24.9, stock: 1 },
];
const orders = [];

function send(res, status, body) {
  res.writeHead(status, { "Content-Type": "application/json" });
  res.end(JSON.stringify(body));
}

createServer(async (req, res) => {
  if (req.method === "POST" && req.url === "/orders") {
    let text = "";
    for await (const chunk of req) text += chunk;
    const body = JSON.parse(text);
    if (!body.email || !Array.isArray(body.items) || body.items.length === 0)
      return send(res, 400, { error: "Neispravna narudžba" });
    let total = 0;
    for (const item of body.items) {
      const product = products.find((p) => p.id === item.productId);
      if (!product || product.stock < item.quantity)
        return send(res, 409, { error: "Nema na zalihi" });
      product.stock -= item.quantity;
      total += product.price * item.quantity;
    }
    const order = { id: orders.length + 1, email: body.email, items: body.items, total };
    orders.push(order);
    console.log(`Šaljem e-poštu na ${body.email}: narudžba ${order.id}`);
    return send(res, 201, order);
  }
  send(res, 404, { error: "Ruta ne postoji" });
}).listen(Number(process.env.PORT ?? 3000), "127.0.0.1");
