// Poslovna pravila naručivanja. Ne zna ništa o HTTP-u (nema req, res ni statusa)
// ni o tome gdje su podaci: ovisnosti dobiva kao parametre.
export class ValidationError extends Error {}
export class OutOfStockError extends Error {}

export function createOrderService({ catalog, orders, notifier, log = console }) {
  return {
    async placeOrder(input) {
      const { email, items } = validate(input);
      const lines = [];
      for (const { productId, quantity } of items) {
        const product = await catalog.findById(productId);
        if (!product) throw new ValidationError(`Proizvod ${productId} ne postoji`);
        if (product.stock < quantity) {
          throw new OutOfStockError(`Nema dovoljno: ${product.name} (na zalihi ${product.stock})`);
        }
        // Cijena dolazi iz kataloga, nikad iz zahtjeva klijenta.
        lines.push({ productId, name: product.name, quantity, unitPrice: product.price });
      }
      // NAPOMENA: provjera i umanjenje zalihe nisu atomični — dva istodobna
      // zahtjeva mogu oba proći provjeru (5. predavanje).
      for (const line of lines) await catalog.decreaseStock(line.productId, line.quantity);
      const total = Math.round(lines.reduce((s, l) => s + l.unitPrice * l.quantity, 0) * 100) / 100;
      const order = await orders.save({ email, items: lines, total });
      try {
        await notifier.orderPlaced(order);
      } catch (error) {
        // Narudžba je spremljena; neuspjela obavijest ne smije je prikazati kao neuspjelu.
        log.error(`Obavijest za narudžbu ${order.id} nije poslana: ${error.message}`);
      }
      return order;
    },
  };
}

function validate(input) {
  const { email, items } = input ?? {};
  if (typeof email !== "string" || !/^[^@\s]+@[^@\s]+$/.test(email)) {
    throw new ValidationError("Neispravna e-pošta");
  }
  if (!Array.isArray(items) || items.length === 0) {
    throw new ValidationError("Narudžba mora imati barem jednu stavku");
  }
  const seen = new Set();
  for (const item of items) {
    if (!Number.isInteger(item?.productId) || !Number.isInteger(item?.quantity) || item.quantity < 1) {
      throw new ValidationError("Stavka treba cjelobrojne productId i quantity ≥ 1");
    }
    if (seen.has(item.productId)) throw new ValidationError("Svaki proizvod navedite jednom");
    seen.add(item.productId);
  }
  return { email, items };
}
