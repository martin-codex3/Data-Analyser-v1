<script lang="ts">
  import type { Component } from "svelte";

  interface Props {
    title: string;
    iconData: any;
    value: string;
    headerIcon: any;
    openModal: () => void;
  }

  const {
    title,
    iconData: IconData,
    headerIcon: HeaderIcon,
    value,
    openModal,
  }: Props = $props();
</script>

{#snippet cardHeader(title: string, Icon: Component)}
  <div class="flex items-center gap-2">
    <Icon height="1.5em" class="shrink-0" />
    <h1 class="first-letter:uppercase">{title}</h1>
  </div>
{/snippet}

{#snippet cardBody(value: string, Icon: Component)}
  <div class="flex items-center gap-5">
    <h2>{value ?? "Not set"}</h2>
    <button
      aria-label="Update details button"
      title="Update Name"
      onclick={() => openModal()}
      class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
    >
      <Icon height="1.5em" class="shrink-0" />
    </button>
  </div>
{/snippet}

<div>
  <div
    class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
  >
    {@render cardHeader(title, HeaderIcon)}
    {@render cardBody(value, IconData)}
  </div>
</div>
