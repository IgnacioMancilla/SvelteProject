<script>
  // Teléfono de WhatsApp en formato internacional (sin +, espacios ni guiones)
  const WHATSAPP = "56942312053";

  // Catálogo (ejemplos). Cambia nombres, precios e imágenes:
  const productos = [
    {
      id: "cocina-tradicional",
      nombre: "Cocina a leña tradicional",
      precio: 389000,
      img: "/images/prod-cocina.jpg",
      categoria: "cocinas",
      desc: "Modelo clásico, ideal para hogares patagónicos.",
      badges: ["Más vendido"]
    },
    {
      id: "calefactor-lento",
      nombre: "Calefactor de combustión lenta",
      precio: 459000,
      img: "/images/prod-calefactor.jpg",
      categoria: "calefactores",
      desc: "Alto rendimiento, bajo consumo de leña.",
      badges: ["Nuevo"]
    },
    {
      id: "parrilla-enlozada",
      nombre: "Parrilla enlozada",
      precio: 89000,
      img: "/images/prod-parrilla.jpg",
      categoria: "accesorios",
      desc: "Superficie enlozada, fácil de limpiar."
    },
    {
      id: "termo-lena",
      nombre: "Termo a leña",
      precio: 279000,
      img: "/images/prod-termo.jpg",
      categoria: "accesorios",
      desc: "Agua caliente asegurada todo el año."
    },
    {
      id: "bullon-cano",
      nombre: "Bullón al caño",
      precio: 24900,
      img: "/images/prod-bullon.jpg",
      categoria: "accesorios",
      desc: "Acabado de primera para tu instalación."
    }
  ];

  const categorias = [
    { id: "todo", label: "Todos" },
    { id: "cocinas", label: "Cocinas" },
    { id: "calefactores", label: "Calefactores" },
    { id: "accesorios", label: "Accesorios" }
  ];

  let categoria = "todo";
  let q = "";
  let orden = "popular"; // 'popular' | 'precio-asc' | 'precio-desc'

  const clp = new Intl.NumberFormat("es-CL", {
    style: "currency",
    currency: "CLP",
    maximumFractionDigits: 0
  }).format;

  const linkWA = (p) =>
    `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(
      `Hola, me interesa el producto "${p.nombre}" (ID: ${p.id}). ¿Podrían darme más información?`
    )}`;

  $: lista = productos
    .filter((p) =>
      categoria === "todo" ? true : p.categoria === categoria
    )
    .filter((p) =>
      q.trim()
        ? (p.nombre + " " + (p.desc ?? ""))
            .toLowerCase()
            .includes(q.toLowerCase())
        : true
    )
    .slice()
    .sort((a, b) => {
      if (orden === "precio-asc") return a.precio - b.precio;
      if (orden === "precio-desc") return b.precio - a.precio;
      return 0; // popular (orden original)
    });
</script>

<section id="productos" class="mx-auto max-w-7xl px-4 py-10">
  <div class="flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
    <div>
      <h2 class="text-2xl md:text-3xl font-semibold text-amber-800">Productos</h2>
      <p class="text-slate-600">Fabricación propia y accesorios seleccionados.</p>
    </div>

    <!-- Controles -->
    <div class="flex flex-col gap-3 sm:flex-row sm:items-center">
      <div class="flex gap-2 flex-wrap">
        {#each categorias as c}
          <button
            class="rounded-full px-4 py-1.5 text-sm ring-1 ring-slate-300 hover:bg-slate-100"
            class:bg-amber-100={categoria === c.id}
            class:ring-amber-400={categoria === c.id}
            on:click={() => (categoria = c.id)}
            aria-pressed={categoria === c.id}
          >
            {c.label}
          </button>
        {/each}
      </div>

      <input
        type="search"
        placeholder="Buscar producto…"
        bind:value={q}
        class="w-full sm:w-56 rounded-lg border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-amber-400"
      />

      <select
        bind:value={orden}
        class="rounded-lg border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-amber-400"
        aria-label="Ordenar por"
      >
        <option value="popular">Orden: Popular</option>
        <option value="precio-asc">Precio: menor a mayor</option>
        <option value="precio-desc">Precio: mayor a menor</option>
      </select>
    </div>
  </div>

  <!-- Grid de tarjetas -->
  <div class="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
    {#each lista as p}
      <article class="group bg-white rounded-2xl shadow overflow-hidden ring-1 ring-slate-200 hover:shadow-lg transition">
        <div class="relative">
          <img
            src={p.img}
            alt={p.nombre}
            class="w-full aspect-[4/3] object-cover"
            loading="lazy"
          />
          {#if p.badges?.length}
            <div class="absolute top-3 left-3 flex gap-2">
              {#each p.badges as b}
                <span class="rounded-md bg-amber-500/95 px-2 py-0.5 text-xs font-semibold text-black/90 shadow">
                  {b}
                </span>
              {/each}
            </div>
          {/if}
        </div>

        <div class="p-4 flex flex-col gap-3">
          <header class="flex items-start justify-between gap-3">
            <h3 class="text-lg font-semibold leading-snug">{p.nombre}</h3>
            <span class="shrink-0 rounded-md bg-amber-50 px-2 py-1 text-sm font-semibold text-amber-700 ring-1 ring-amber-200">
              {clp(p.precio)}
            </span>
          </header>

          {#if p.desc}
            <p class="text-sm text-slate-600 line-clamp-2">{p.desc}</p>
          {/if}

          <div class="mt-1 flex flex-wrap items-center gap-2">
            <span class="rounded-full bg-slate-100 px-2 py-0.5 text-xs text-slate-700">
              {p.categoria}
            </span>
          </div>

          <div class="mt-2 flex items-center gap-2">
            <a
              href={linkWA(p)}
              target="_blank" rel="noopener"
              class="inline-flex items-center justify-center gap-2 rounded-lg bg-amber-600 px-3 py-2 text-white hover:bg-amber-700 active:scale-[.98]"
            >
              <!-- ícono whatsapp minimal -->
              <svg viewBox="0 0 24 24" class="h-4 w-4" fill="currentColor" aria-hidden="true"><path d="M20.5 3.5A11.9 11.9 0 0 0 12 0C5.4 0 0 5.4 0 12c0 2 .5 3.8 1.4 5.5L0 24l6.7-1.8A12 12 0 0 0 12 24c6.6 0 12-5.4 12-12 0-3.2-1.3-6.2-3.5-8.5zM12 22a10 10 0 0 1-5.1-1.4l-.4-.3-4 .9.9-3.9-.3-.4A9.9 9.9 0 1 1 22 12c0 5.5-4.5 10-10 10zm5-7.6c-.3-.2-1.8-.9-2-.9-.3-.1-.5-.2-.7.2-.2.3-.8 1-.9 1.2-.2.2-.4.2-.7 0a7.6 7.6 0 0 1-2.2-1.4 8.2 8.2 0 0 1-1.5-1.9c-.2-.3 0-.5.2-.7l.5-.6c.1-.2.2-.3.3-.6 0-.2 0-.4 0-.6 0-.2-.7-1.7-1-2.3-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.9 4.2 4 .6.3 1.1.5 1.5.6.6.2 1.1.2 1.6.1.5-.1 1.8-.7 2-1.4.2-.7.2-1.3.1-1.4z"/></svg>
              Consultar
            </a>

            <!-- Botón "Más info" por si luego haces /productos/[id] -->
            <a
              href={`/productos/${p.id}`}
              class="inline-flex items-center justify-center rounded-lg px-3 py-2 text-slate-700 ring-1 ring-slate-300 hover:bg-slate-50"
            >
              Más info
            </a>
          </div>
        </div>
      </article>
    {/each}
  </div>

  {#if !lista.length}
    <p class="mt-8 text-center text-slate-600">No encontramos productos con esos filtros.</p>
  {/if}
</section>
