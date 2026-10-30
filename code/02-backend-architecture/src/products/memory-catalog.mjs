// Pristup podacima o proizvodima. Zasad niz u memoriji procesa;
// u 4. predavanju isto sučelje dobiva implementaciju nad PostgreSQL-om.
export function createMemoryCatalog() {
  const products = [
    { id: 7, name: "Bilježnica", price: 3.5, stock: 5 },
    { id: 8, name: "Olovka", price: 0.8, stock: 20 },
    { id: 9, name: "Ruksak", price: 24.9, stock: 1 },
  ];
  return {
    async list() {
      return products.map(({ id, name, price }) => ({ id, name, price }));
    },
    async findById(id) {
      const p = products.find((x) => x.id === id);
      return p ? { ...p } : null;
    },
    async decreaseStock(id, quantity) {
      products.find((x) => x.id === id).stock -= quantity;
    },
  };
}
