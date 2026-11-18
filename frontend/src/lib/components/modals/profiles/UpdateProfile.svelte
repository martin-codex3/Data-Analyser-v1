<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import CancelIcon from "@iconify-svelte/tabler/x";
    import { toast } from "svelte-sonner";
    import type { ActionData } from "../../../../routes/dashboard/account-profile/$types";
    import TextAreaInput from "#lib/components/inputs/TextAreaInput.svelte";

    interface Props {
        name: string;
        value: string | undefined | boolean | object;
        label: string;
        closeModal: () => void;
        form: ActionData;
    }

    const { name, value, label, closeModal, form }: Props = $props();

    let isUpdatingProfile: boolean = $state(false);
    let errorTitle: string = $state("");

    $effect(() => {
        if (form?.problem?.title) {
            errorTitle = form?.problem?.title;
        }

        if (form?.problem?.detail) {
            errorTitle = form?.problem?.detail;
        }
    });

    const fieldErrors = $derived((field: string) => {
        return form?.problem?.errors.find((e) => field === e.pointer);
    });
</script>

{#snippet modalBody()}
    <div>
        <form
            action="?/updateProfile"
            method="POST"
            use:enhance={() => {
                isUpdatingProfile = true;
                return async ({ update, result }) => {
                    await update({ reset: false, refreshAll: true });
                    isUpdatingProfile = false;

                    if (result.type === "failure") {
                        toast.error(errorTitle);
                    }

                    if (result.type === "error") {
                        toast.error(errorTitle);
                    }

                    if (result.type === "success") {
                        toast.success("Okay");
                    }
                };
            }}
        >
            <div class="space-y-5">
                {#if name === "bio"}
                    <TextAreaInput
                        type="text"
                        {name}
                        id={label}
                        placeholder=""
                        inputError={fieldErrors(`#/${name}`)?.detail}
                        value={`${value}`}
                        {label}
                    />
                {:else}
                    <TextInput
                        type="text"
                        {name}
                        id={label}
                        placeholder=""
                        inputError={fieldErrors(`#/${name}`)?.detail}
                        {value}
                        {label}
                    />
                {/if}
                <StyledButton
                    isLoading={isUpdatingProfile}
                    title="Update detail"
                />
            </div>
        </form>
    </div>
{/snippet}

<div
    class="fixed inset-0 z-100 backdrop-blur-sm bg-black/20 flex items-center justify-center"
>
    <div
        class="w-full max-w-md rounded-4xl px-5 py-5 space-y-7 bg-primary-slight-black border border-orange-50/10 motion-preset-slide-down-sm"
    >
        <div class="space-y-4">
            <div class="flex items-center justify-between">
                <h1 class="text-xl font-semibold first-letter:capitalize">
                    update profile
                </h1>

                <button
                    aria-label="button to close modal"
                    onclick={closeModal}
                    class="flex items-center justfiy-center cursor-pointer hover:bg-black rounded-full transition duration-300 p-2"
                >
                    <CancelIcon height="1.3em" class="shrink-0" />
                </button>
            </div>
            <div>
                <p class="text-gray-400">
                    Make changes to your profile. The changes will reflect
                    automatically when the action is successful
                </p>
            </div>
        </div>

        <div>
            {@render modalBody()}
        </div>
    </div>
</div>
