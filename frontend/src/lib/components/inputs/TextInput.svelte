<script lang="ts">
    interface Props {
        label: string;
        id: string;
        placeholder: string;
        value: string | undefined | boolean | object;
        inputError: string | undefined;
        name: string;
        type: string;
    }

    const { label, id, placeholder, value, inputError, name, type }: Props =
        $props();
</script>

{#snippet formError(name: string | undefined)}
    <span class="text-sm text-red-600">{name}</span>
{/snippet}

<div class="">
    {#if label}
        <label for={id}>{label}</label>
    {/if}
    <input
        {type}
        {id}
        {placeholder}
        {name}
        {value}
        class={[
            "w-full outline-none mt-1 px-2 py-3 rounded-lg border bg-transparent focus:ring-primary-main-orange focus:border-primary-main-orange",
            inputError ? "border-red-500" : "border-white",
        ]}
    />
    {@render formError(inputError)}
</div>
