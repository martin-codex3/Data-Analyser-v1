<script lang="ts">
  import type { Component } from "svelte";

  let toggleModalButton: boolean = $state(false);

  interface Props {
    title: string;
    iconData: any;
    value: string | string[];
    headerIcon: any;
    length: number;
    index: number;
    openModal: () => void;
  }

  const {
    title,
    iconData: IconData,
    headerIcon: HeaderIcon,
    length,
    value,
    openModal,
    index,
  }: Props = $props();

  $effect(() => console.log(truncatedDescription()));

  const truncatedDescription = $derived(() => {
    if (title === "Description") {
      return value.slice(0, 40);
    } else {
      return value;
    }
  });

  // for showing the open modal icon
  const showOpenModalButton = $derived(() => {
    if (title === "Slug" || title === "Updated at" || title === "Created at") {
      return false;
    } else {
      return true;
    }
  });
</script>

{#snippet cardHeader(title: string | string[], Icon: Component)}
  <div class="flex items-center gap-2">
    <Icon height="1.5em" class="shrink-0" />
    <h1 class="first-letter:uppercase">{title}</h1>
  </div>
{/snippet}

{#snippet cardBody(value: string | string[], Icon: Component)}
  <div class="flex items-center gap-5">
    <h2>
      {truncatedDescription() ?? "Not set"}
    </h2>
    {#if showOpenModalButton()}
      <button
        aria-label="Update details button"
        title="Update Name"
        onclick={() => openModal()}
        class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
      >
        <Icon height="1.5em" class="shrink-0" />
      </button>
    {/if}
  </div>
{/snippet}

<div>
  <div
    class={[
      "flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg",
      length - 1 === index ? "rounded-3xl" : "",
    ]}
  >
    {@render cardHeader(title, HeaderIcon)}
    {@render cardBody(value, IconData)}
  </div>
</div>
