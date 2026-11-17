<script lang="ts">
    import LoadingSVG from "@iconify-svelte/svg-spinners/180-ring";
    interface Props {
        isLoading: boolean;
        title: string;
    }

    const { isLoading, title }: Props = $props();
</script>

<div>
    <button
        aria-label="Button component"
        title="Click to send"
        class="flex items-center justify-center rounded-full h-12 cursor-pointer bg-primary-main-orange text-primary-main-black w-44"
    >
        {#if isLoading}
            <div class="flex items-center gap-2">
                <LoadingSVG height="1.3em" class="shrink-0" />
                <span class="test-sm">Processing..</span>
            </div>
        {/if}
    </button>
</div>
