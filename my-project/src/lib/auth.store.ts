import { writable } from 'svelte/store';
import { me, login as apiLogin, logout as apiLogout } from '$lib/api';

export type Session = { authenticated: boolean; username?: string };
export const user = writable<Session | null>(null);

export async function initSession() {
  try { user.set(await me()); } catch { user.set(null); }
}
export async function doLogin(u: string, p: string) {
  await apiLogin(u, p);
  await initSession();
}
export async function doLogout() {
  await apiLogout();
  user.set(null);
}
