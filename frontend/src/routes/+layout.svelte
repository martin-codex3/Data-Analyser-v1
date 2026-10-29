<script lang="ts">
  import "./layout.css";
  import favicon from "#lib/assets/favicon.svg";
  import type { LayoutProps } from "./$types";
  import { Toaster, toast } from "svelte-sonner";

  let { children }: LayoutProps = $props();
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<main>
  <Toaster richColors position="top-right" />
  {@render children()}
</main>
