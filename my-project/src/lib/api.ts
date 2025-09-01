// src/lib/api.ts
import { env } from '$env/dynamic/public';
const BASE = env.PUBLIC_API_BASE;

/** Fetch desde el navegador (páginas/client-side) */
export async function apiFetch(path: string, init: RequestInit = {}) {
  const res = await fetch(`${BASE}${path}`, {
    credentials: 'include', // envía/recibe cookies
    ...init,
    headers: {
      'accept': 'application/json',
      ...(init.headers || {})
    }
  });
  return res;
}

/** Fetch desde load(server): reenvía cookies del request entrante */
export async function apiFetchServer(
  fetchFn: typeof fetch,
  path: string,
  cookie: string | null,
  init: RequestInit = {}
) {
  const res = await fetchFn(`${BASE}${path}`, {
    ...init,
    headers: {
      'accept': 'application/json',
      ...(cookie ? { cookie } : {}),
      ...(init.headers || {})
    }
  });
  return res;
}
