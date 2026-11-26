<script lang="ts">
    import type { Component } from "svelte";
    import PencilIcon from "@iconify-svelte/tabler/pencil";

    interface Props {
        Icon: Component;
        title: string;
        description: string;
        value: string | undefined | boolean | object;
        index: number;
        length: number;
        name: string;
        openModal: () => void;
    }

    const {
        Icon,
        title,
        description,
        value,
        index,
        length,
        openModal,
        name,
    }: Props = $props();

    // for the border radius
    const cardRadius = $derived(() => {
        return index + 1 === 1 ? "rounded-tr-3xl rounded-tl-3xl" : "rounded-lg";
    });
    const lastCardRadius = $derived(() => {
        return length - 1 === index
            ? "rounded-bl-3xl rounded-br-3xl"
            : "rounded-lg";
    });

    const handleOpenModal = () => {
        openModal();
    };
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
            <h1 class="text-lg">{title}</h1>
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
            {#if name !== "is_deleted" && name !== "created_at" && name !== "updated_at" && name !== "created_by_id"}
                <button
                    aria-label="The open details button"
                    title="Open Update Modal"
                    onclick={handleOpenModal}
                    class="flex items-center justify-center cursor-pointer hover:bg-primary-slight-black/40 p-2 rounded-full"
                >
                    <PencilIcon height="1.3em" class="shrink-0" />
                </button>
            {/if}
        </div>
    </div>
{/snippet}

<div
    class={[
        "flex items-center justify-between bg-black px-5 py-2",
        cardRadius(),
        lastCardRadius(),
    ]}
>
    {@render cardHeader(Icon, title, description)}
    {@render cardBody(value)}
</div>
