// Obavijest kupcu. Stvarnu e-poštu ne šaljemo: ispis u terminal glumi vanjsku uslugu.
// Načini rada služe demonstraciji: slow (3 s) i fail (usluga ne radi).
export function createNotifier({ mode = "console", log = console } = {}) {
  return {
    async orderPlaced(order) {
      if (mode === "slow") await new Promise((r) => setTimeout(r, 3000));
      if (mode === "fail") throw new Error("Usluga e-pošte nije dostupna");
      log.log(`[e-pošta] ${order.email}: narudžba ${order.id} zaprimljena, ukupno ${order.total} €`);
    },
  };
}
