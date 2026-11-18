<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import CancelIcon from "@iconify-svelte/tabler/x";
    import { toast } from "svelte-sonner";

    interface Props {
        name: string;
        value: string | undefined | boolean | object;
        label: string;
    }

    const { name, value, label }: Props = $props();
    let isUpdatingProfile: boolean = $state(false);
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
                        toast.error("error");
                    }

                    if (result.type === "failure") {
                        toast.error("error");
                    }

                    if (result.type === "success") {
                        toast.success("Okay");
                    }
                };
            }}
        >
            <div class="space-y-7">
                <TextInput
                    type="text"
                    {name}
                    id={label}
                    placeholder=""
                    inputError=""
                    {value}
                    {label}
                />
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
        class="w-full max-w-md rounded-4xl px-5 py-5 space-y-7 bg-primary-slight-black border border-orange-50/10"
    >
        <div class="space-y-4">
            <div class="flex items-center justify-between">
                <h1 class="text-xl font-semibold first-letter:capitalize">
                    update profile
                </h1>

                <button
                    aria-label="button to close modal"
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
