<script lang="ts">
    interface Props {
        label: string;
        id: string;
        placeholder: string;
        inputError: string | undefined;
        name: string;
        children: any;
    }

    const { label, id, placeholder, inputError, name, children }: Props =
        $props();
</script>

{#snippet formError(name: string | undefined)}
    <span class="text-sm text-red-600">{name}</span>
{/snippet}

<div class="">
    {#if label}
        <label for={id}>{label}</label>
    {/if}
    <select
        {id}
        {placeholder}
        {name}
        class={[
            "w-full outline-none mt-1 px-2 py-3 rounded-lg border bg-transparent focus:ring-primary-main-orange focus:border-primary-main-orange",
            inputError ? "border-red-500" : "border-white",
        ]}
    >
        {@render children()}
    </select>
    {@render formError(inputError)}
</div>
