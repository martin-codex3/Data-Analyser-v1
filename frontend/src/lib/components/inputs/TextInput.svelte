<script lang="ts">
  import { error } from "@sveltejs/kit";

  interface Props {
    id: string;
    label: string;
    type: string;
    name: string;
    errorValue: string | undefined;
    placeholder: string;
  }

  let { id, label, type, name, errorValue, placeholder }: Props = $props();
</script>

{#snippet formError(name: string | undefined)}
  {#if name}
    <span class="text-sm text-red-600">{name}</span>
  {/if}
{/snippet}

<div class="space-y-1">
  <label for={id}>{label}</label>
  <input
    {type}
    {name}
    {id}
    {placeholder}
    class={[
      "w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue",
    ]}
  />
  {@render formError(errorValue)}
</div>
