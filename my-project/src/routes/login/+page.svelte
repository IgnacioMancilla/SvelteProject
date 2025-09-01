<!-- src/routes/login/+page.svelte -->
<script lang="ts">
  import { env } from '$env/dynamic/public';
  
  let sending = false;
  let errorMsg: string | null = null;

  async function handleSubmit(e: SubmitEvent) {
    e.preventDefault();
    const form = e.currentTarget as HTMLFormElement;
    const data = Object.fromEntries(new FormData(form).entries()) as Record<string, string>;

    sending = true;
    errorMsg = null;

    try {
      const res = await fetch(`${env.PUBLIC_API_BASE}/auth/login/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',              // <- importante para cookies
        body: JSON.stringify(data)
      });

      if (res.ok) {
        // recarga para que +layout.server.ts lea la cookie y cambie la navbar
        window.location.href = '/';
      } else {
        const j = await res.json().catch(() => ({}));
        errorMsg = j.error ?? 'Credenciales inválidas';
      }
    } catch {
      errorMsg = 'Error de red. Intenta nuevamente.';
    } finally {
      sending = false;
    }
  }
</script>

<section class="mx-auto max-w-md px-4 py-10">
  <form
    class="grid gap-4 bg-white p-6 rounded-2xl shadow ring-1 ring-slate-200"
    on:submit|preventDefault={handleSubmit}
    autocomplete="on"
  >
    <!-- Header con ícono de “cara anónima” -->
    <div class="flex flex-col items-center text-center gap-3 mb-2">
      <div class="h-14 w-14 rounded-full bg-amber-100 text-amber-700 grid place-items-center shadow-inner" aria-hidden="true">
        <svg viewBox="0 0 24 24" class="h-7 w-7" fill="currentColor">
          <path d="M12 2c5.2 0 9.5 2.5 9.5 5.7v3c0 5.2-4.2 10.3-9.5 10.3S2.5 15.9 2.5 10.7v-3C2.5 4.5 6.8 2 12 2Z"/>
          <path fill="#fff" d="M7.6 9.2c.9-.7 2.1-.7 3 0 .2.2.6.2.8 0 .9-.7 2.1-.7 3 0 .4.3.1.9-.4.8-1-.2-2-.1-2.9.2-.2.1-.5.1-.7 0-.9-.3-1.9-.4-2.9-.2-.5.1-.8-.5-.4-.8Z"/>
          <path fill="#fff" d="M7.7 13.1c2.1.9 4.5.9 6.6 0 .4-.2.9.2.8.6-.5 1.7-2.5 3.1-4.1 3.1s-3.6-1.4-4.1-3.1c-.1-.4.4-.8.8-.6Z" />
        </svg>
      </div>
      <h1 class="text-2xl font-semibold">Iniciar sesión</h1>
      <p class="text-sm text-slate-500 -mt-1">Usa tus credenciales de administrador</p>
    </div>

    {#if errorMsg}
      <div class="rounded bg-red-100 text-red-800 p-3 text-sm" role="alert" aria-live="polite">
        {errorMsg}
      </div>
    {/if}

    <label class="block">
      <span class="text-sm font-medium">Usuario</span>
      <input
        name="username"
        required
        class="mt-1 w-full rounded-lg border px-3 py-2"
        autocomplete="username"
      />
    </label>

    <label class="block">
      <span class="text-sm font-medium">Contraseña</span>
      <input
        name="password"
        type="password"
        required
        class="mt-1 w-full rounded-lg border px-3 py-2"
        autocomplete="current-password"
      />
    </label>

    <button class="rounded-lg bg-amber-600 px-4 py-2 text-white disabled:opacity-60" disabled={sending}>
      {#if sending}Entrando…{:else}Entrar{/if}
    </button>
  </form>
</section>

