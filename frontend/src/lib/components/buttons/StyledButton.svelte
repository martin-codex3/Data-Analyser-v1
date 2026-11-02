<script lang="ts">
  import LoadingIcon from "@iconify-svelte/svg-spinners/180-ring";
  interface Props {
    title: string;
    isLoading: boolean;
    label: string;
  }
  let { title = "Button Title", label, isLoading = false }: Props = $props();
</script>

<button
  aria-label="styled-button-component"
  {title}
  class="flex items-center justify-center bg-primary-main-blue first-letter:capitalize rounded-full h-12 w-54 text-blue-50 cursor-pointer hover:shadow-xl transition duration-200"
>
  {#if isLoading}
    <LoadingIcon />
  {:else}
    <span>{label}</span>
  {/if}
</button>
