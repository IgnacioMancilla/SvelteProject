<script>
  import "../app.css";
  let { children, data } = $props();
  const LOGO = "/images/LogoCocinas.png";
  let mobileOpen = false;
  const toggle = () => (mobileOpen = !mobileOpen);
  const close  = () => (mobileOpen = false);
  
</script>

<div class="min-h-screen flex flex-col bg-slate-50 text-slate-900">
  <nav class="sticky top-0 z-40 bg-white/80 backdrop-blur border-b border-slate-200">
    <div class="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
      <!-- Logo en lugar del texto APPEL -->
      <a href="/" class="inline-flex items-center" aria-label="Ir al inicio">
        <img
          src={LOGO}
          alt="Cocinas Appel"
          class="h-10 sm:h-12 w-auto select-none"
          draggable="false"
        />
      </a>

      <div class="hidden md:flex gap-3">
        <a href="/" class="px-3 py-1.5 rounded hover:bg-slate-100">Inicio</a>
        <a href="/hacemos" class="px-3 py-1.5 rounded hover:bg-slate-100">Qué hacemos</a>
        <a href="/productos" class="px-3 py-1.5 rounded hover:bg-slate-100">Productos</a>
        <a href="/contacto" class="px-3 py-1.5 rounded hover:bg-slate-100">Contacto</a>
        <a href="/galeria" class="px-3 py-1.5 rounded hover:bg-slate-100">Galería</a>
        {#if data?.authed}
          <a href="/admin" class="ml-2 px-3 py-1.5 rounded bg-amber-600 text-white hover:bg-amber-700">
            Panel
          </a>
          <form method="POST" action="/logout" class="ml-1">
            <button class="px-3 py-1.5 rounded ring-1 ring-slate-300 hover:bg-slate-100">
              Cerrar sesión
            </button>
          </form>
        {:else}
          <a href="/login" class="ml-2 px-3 py-1.5 rounded ring-1 ring-slate-300 hover:bg-slate-100 inline-flex items-center gap-2">
  <svg viewBox="0 0 24 24" class="h-4 w-4" fill="currentColor" aria-hidden="true">
    <path d="M12 2c5.2 0 9.5 2.5 9.5 5.7v3c0 5.2-4.2 10.3-9.5 10.3S2.5 15.9 2.5 10.7v-3C2.5 4.5 6.8 2 12 2Z"/>
    <path fill="#fff" d="M7.6 9.2c.9-.7 2.1-.7 3 0 .2.2.6.2.8 0 .9-.7 2.1-.7 3 0 .4.3.1.9-.4.8-1-.2-2-.1-2.9.2-.2.1-.5.1-.7 0-.9-.3-1.9-.4-2.9-.2-.5.1-.8-.5-.4-.8Z"/>
    <path fill="#fff" d="M7.7 13.1c2.1.9 4.5.9 6.6 0 .4-.2.9.2.8.6-.5 1.7-2.5 3.1-4.1 3.1s-3.6-1.4-4.1-3.1c-.1-.4.4-.8.8-.6Z" />
  </svg>
  Iniciar sesión
</a>

        {/if}
      </div>
    </div>
  </nav>

  <!-- Botón hamburguesa para móviles -->




  <main class="flex-1 max-w-6xl mx-auto px-4 py-8">
    {@render children?.()}
  </main>

  <!-- Barra de redes -->
<div class="flex justify-center gap-6 py-8">
  <!-- Facebook -->
  <a
    href="https://www.facebook.com/cocinasappel/?locale=es_LA" 
    target="_blank" rel="noopener"
    aria-label="Facebook"
    class="grid h-12 w-12 place-items-center rounded-full bg-[#1877F2] text-white
           shadow hover:shadow-lg hover:scale-105 transition"
  >
    <!-- icono facebook -->
    <svg viewBox="0 0 24 24" class="h-6 w-6" fill="currentColor" aria-hidden="true">
      <path d="M22 12a10 10 0 1 0-11.6 9.9v-7h-2.6V12h2.6V9.7c0-2.6 1.5-4 3.9-4 1.1 0 2.3.2 2.3.2v2.5h-1.3c-1.3 0-1.8.8-1.8 1.7V12h3l-.5 2.9h-2.5v7A10 10 0 0 0 22 12z"/>
    </svg>
  </a>

  <!-- WhatsApp (abre chat) -->
  <a
    href="https://wa.me/56942312053?text=Hola%20quiero%20información"
    target="_blank" rel="noopener"
    aria-label="WhatsApp"
    class="grid h-12 w-12 place-items-center rounded-full bg-[#25D366] text-white
           shadow hover:shadow-lg hover:scale-105 transition"
  >
    <svg viewBox="0 0 24 24" class="h-6 w-6" fill="currentColor" aria-hidden="true">
      <path d="M20.5 3.5A11.9 11.9 0 0 0 12 0C5.4 0 0 5.4 0 12c0 2 .5 3.8 1.4 5.5L0 24l6.7-1.8A12 12 0 0 0 12 24c6.6 0 12-5.4 12-12 0-3.2-1.3-6.2-3.5-8.5zM12 22a10 10 0 0 1-5.1-1.4l-.4-.3-4 .9.9-3.9-.3-.4A9.9 9.9 0 1 1 22 12c0 5.5-4.5 10-10 10zm5-7.6c-.3-.2-1.8-.9-2-.9-.3-.1-.5-.2-.7.2-.2.3-.8 1-.9 1.2-.2.2-.4.2-.7 0a7.6 7.6 0 0 1-2.2-1.4 8.2 8.2 0 0 1-1.5-1.9c-.2-.3 0-.5.2-.7l.5-.6c.1-.2.2-.3.3-.6 0-.2 0-.4 0-.6 0-.2-.7-1.7-1-2.3-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.9 4.2 4 .6.3 1.1.5 1.5.6.6.2 1.1.2 1.6.1.5-.1 1.8-.7 2-1.4.2-.7.2-1.3.1-1.4z"/>
    </svg>
  </a>

  <!-- Email -->
  <a
    href="mailto:appelpatagonia@gmail.com?subject=Consulta&body=Hola%2C%20quisiera%20informaci%C3%B3n..."
    aria-label="Email"
    class="grid h-12 w-12 place-items-center rounded-full bg-slate-500 text-white
           shadow hover:shadow-lg hover:scale-105 transition"
  >
    <svg viewBox="0 0 24 24" class="h-6 w-6" fill="currentColor" aria-hidden="true">
      <path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4-8 5L4 8V6l8 5 8-5v2Z"/>
    </svg>
  </a>
</div>

  

  <footer class="bg-slate-100">
    <div class="max-w-6xl mx-auto px-4 py-6 text-sm text-slate-600 text-center">
      © {new Date().getFullYear()} Cocinas Appel. Todos los derechos reservados.
    </div>
  </footer>
</div>

