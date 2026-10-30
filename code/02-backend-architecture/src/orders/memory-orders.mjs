// Pristup podacima o narudžbama: niz u memoriji procesa.
// Restart procesa briše narudžbe; trajnu pohranu uvodimo u 4. predavanju.
export function createMemoryOrders() {
  const orders = [];
  return {
    async save(order) {
      const saved = { id: orders.length + 1, createdAt: new Date().toISOString(), ...order };
      orders.push(saved);
      return saved;
    },
  };
}
