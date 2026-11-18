<script lang="ts">
    import type { Component } from "svelte";

    interface Props {
        Icon: Component;
        title: string;
        description: string;
        value: string | undefined | boolean | object;
    }

    const { Icon, title, description, value }: Props = $props();
</script>

<!-- the card header -->
{#snippet cardHeader(
    Icon: Component,
    title: string,
    description: string | undefined,
)}
    <div class="flex items-center gap-5">
        <div>
            <Icon height="1.5em" class="shrink-0" />
        </div>

        <div>
            <h1>{title}</h1>
            <p>{description}</p>
        </div>
    </div>
{/snippet}

<!-- for the card body -->
{#snippet cardBody(value: string | undefined | boolean | object)}
    <div class="flex items-center gap-5">
        <div class="">
            <h1>{value}</h1>
        </div>
        <div>
            <button
                aria-label="The open details button"
                title="Open Modal"
                class="flex items-center justify-center"
            ></button>
        </div>
    </div>
{/snippet}

<div class="flex items-center justify-between">
    {@render cardHeader(Icon, title, description)}
    {@render cardBody(value)}
</div>
