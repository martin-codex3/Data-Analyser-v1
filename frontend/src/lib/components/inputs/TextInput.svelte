<script lang="ts">
    interface Props {
        label: string;
        id: string;
        placeholder: string;
        value: string;
        inputError: string;
        name: string;
        type: string;
    }

    const { label, id, placeholder, value, inputError, name, type }: Props =
        $props();
</script>

{#snippet formError(name: string)}
    <span>{name}</span>
{/snippet}

<div>
    {#if label}
        <label for={id}>{label}</label>
    {/if}
    <input
        {type}
        {id}
        {placeholder}
        {name}
        {value}
        class="w-full outline-none px-2 py-3 rounded-lg border border-white bg-transparent focus:ring-primary-main-orange focus:border-primary-main-orange"
    />
</div>
