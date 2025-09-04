const API = import.meta.env.VITE_API_URL;

function getCookie(name: string) {
  return document.cookie.split('; ')
    .find(r => r.startsWith(name + '='))?.split('=')[1] ?? '';
}

async function apiGet(path: string) {
  const r = await fetch(`${API}${path}`, { credentials: 'include' });
  if (!r.ok) throw new Error(await r.text());
  return r.json();
}

async function apiPost(path: string, data: any, extraHeaders: Record<string,string> = {}) {
  const r = await fetch(`${API}${path}`, {
    method: 'POST',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json', ...extraHeaders },
    body: JSON.stringify(data),
  });
  if (!r.ok) throw new Error(await r.text());
  return r.json();
}

export async function ensureCsrf() { return apiGet('/api/csrf/'); }
export async function ping()       { return apiGet('/api/ping/'); }
export async function me()         { return apiGet('/api/auth/me/'); }

export async function login(username: string, password: string) {
  await ensureCsrf();
  const token = getCookie('csrftoken');
  return apiPost('/api/auth/login/', { username, password }, { 'X-CSRFToken': token });
}
export async function logout() {
  const token = getCookie('csrftoken');
  return apiPost('/api/auth/logout/', {}, { 'X-CSRFToken': token });
}

export async function register(payload: {
  username: string; email: string; password: string; password2: string;
}) {
  await ensureCsrf();
  const token = document.cookie.split('; ').find(r => r.startsWith('csrftoken='))?.split('=')[1] ?? '';
  return apiPost('/api/auth/register/', payload, { 'X-CSRFToken': token });
}
