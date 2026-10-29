<script lang="ts">
  let { children } = $props();
</script>

<div class="main__content__wrapper bg-gray-100 px-5 py-5">
  <nav
    class="main__navigation fixed h-screen w-32 rounded-2xl bg-white border border-gray-200"
  >
    <div class="nav__wrapper">
      <div></div>
      <div class="">
        <ul>
          <li>
            <a href="/dashboard">Dashboard</a>
          </li>

          <li>
            <a href="/dashboard">Uploads</a>
          </li>

          <li>
            <a href="/dashboard">chat</a>
          </li>

          <li>
            <a href="/dashboard">Dashboard</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <main class="min-h-screen">
    <section class="ms-32">
      {@render children()}
    </section>
  </main>
</div>
