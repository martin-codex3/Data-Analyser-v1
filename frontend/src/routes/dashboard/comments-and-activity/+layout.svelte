<script lang="ts">
  let { children } = $props();
</script>

<div class="main__content__wrapper">
  <nav
    class="fixed bg-white h-[calc(100vh)] overflow-auto scrollbar-thin w-80 border border-gray-200"
  ></nav>
  <main>
    {@render children()}
  </main>
</div>
