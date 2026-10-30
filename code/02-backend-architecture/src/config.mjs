// Konfiguracija: sve što se razlikuje među okruženjima čita se iz varijabli okruženja,
// provjerava se jednom pri pokretanju i dalje se prosljeđuje kao običan objekt.
const NOTIFIERS = ["console", "slow", "fail"];

export function loadConfig(env = process.env) {
  const port = Number(env.PORT ?? 3000);
  if (!Number.isInteger(port) || port < 1 || port > 65535) {
    throw new Error(`PORT mora biti cijeli broj 1–65535, a dobiven je "${env.PORT}"`);
  }
  const notifier = env.NOTIFIER ?? "console";
  if (!NOTIFIERS.includes(notifier)) {
    throw new Error(`NOTIFIER mora biti jedan od: ${NOTIFIERS.join(", ")}`);
  }
  return Object.freeze({
    port,
    host: env.HOST ?? "127.0.0.1",
    notifier,
    emailApiKey: env.EMAIL_API_KEY || null, // tajna: ne ispisuje se
    shutdownTimeoutMs: 10_000,
  });
}

// Sažetak za zapis pri pokretanju — bez tajni.
export function describeConfig(config) {
  return { ...config, emailApiKey: config.emailApiKey ? "(postavljen)" : "(nije postavljen)" };
}
