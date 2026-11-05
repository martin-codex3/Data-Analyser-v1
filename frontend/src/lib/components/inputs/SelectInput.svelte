<script lang="ts">
  import { error } from "@sveltejs/kit";

  interface Props {
    id: string | undefined;
    label: string | undefined;
    name: string;
    value: string | object;
    errorValue: string | undefined;
    placeholder: string;
    allRecords: any;
  }

  let {
    id,
    label,
    name,
    errorValue,
    placeholder,
    value = "",
    allRecords,
  }: Props = $props();
</script>

{#snippet formError(name: string | undefined)}
  {#if name}
    <span class="text-sm text-red-600">{name}</span>
  {/if}
{/snippet}

<div class="space-y-1">
  <label for={id} class="">{label}</label>
  <select
    {name}
    {id}
    {placeholder}
    {value}
    class={[
      "w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue invalid:border-red-600",
      errorValue ? "bg-red-50/50 border-red-600 placeholder:text-red-600" : "",
    ]}
  >
    {#each allRecords as record, index (record)}
      <option value={record.iso2}>{record.name}</option>
    {/each}
  </select>
  {@render formError(errorValue)}
</div>
