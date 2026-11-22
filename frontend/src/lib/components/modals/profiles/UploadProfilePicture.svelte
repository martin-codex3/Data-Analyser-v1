<script lang="ts">
    import type { FormResponse } from "#lib/types/forms/form_response.ts";
    import type { User } from "#lib/types/users/user.ts";
    import { PUBLIC_API_ENDPOINT } from "$app/env/public";
    import { enhance } from "$app/forms";
    import FileUploadIcon from "@iconify-svelte/tabler/pencil";
    import CloseIcon from "@iconify-svelte/tabler/x";
    import { toast } from "svelte-sonner";
    import LoadingIcon from "@iconify-svelte/svg-spinners/180-ring";

    interface Props {
        user: User;
        closeModal: () => void;
        form: FormResponse | null;
    }

    const { user, closeModal, form }: Props = $props();
    let errorTitle: string = $state("");
    let isUpdatingProfile: boolean = $state(false);

    $effect(() => {
        if (form?.problem?.title) {
            errorTitle = form?.problem?.title;
        }

        if (form?.message) {
            errorTitle = form?.message;
        }
    });

    const handleCloseModal = () => {
        closeModal();
    };

    const fieldErrors = $derived((field: string) => {
        return form?.problem?.errors?.find((e) => field === e.pointer);
    });
</script>

<div
    class="fixed bg-black/10 backdrop-blur-sm inset-0 z-100 flex items-center justify-center"
>
    <div
        class="bg-primary-slight-black w-full max-w-md rounded-4xl border border-primary-main-orange/10 motion-preset-slide-down-sm
        motion-duration-200"
    >
        <div class="relative">
            <img
                src={`${PUBLIC_API_ENDPOINT}${user.profile_image_url}`}
                alt="profile"
                class="h-70 w-full object-cover rounded-tr-4xl rounded-tl-4xl"
            />

            <div class="absolute top-3 right-3">
                <button
                    aria-label="close button"
                    title="Close"
                    onclick={handleCloseModal}
                    class="flex items-center justify-center p-2 border cursor-pointer rounded-full bg-black/10 backdrop-blur-sm"
                >
                    <CloseIcon height="1.5em" class="shrink-0" />
                </button>
            </div>
        </div>

        <div class="px-5 py-5 space-y-5">
            <div class="">
                <h1 class="first-letter:capitalize font-semibold text-xl">
                    Upload your profile
                </h1>
                <p>upload files in (JPEG, JPG, PNG, GIF) format</p>
            </div>

            <div>
                <form
                    action="?/handleUploadedFile"
                    method="POST"
                    enctype="multipart/form-data"
                    use:enhance={() => {
                        isUpdatingProfile = true;
                        return async ({ update, result }) => {
                            await update();
                            isUpdatingProfile = false;

                            if (result.type === "error") {
                                toast.error(errorTitle);
                            }

                            if (result.type === "failure") {
                                toast.error(errorTitle);
                            }

                            if (result.type === "success") {
                                toast.success("Profile uploaded successfully");
                            }
                        };
                    }}
                >
                    <div class="flex items-center w-full gap-3">
                        <div class="w-full">
                            <input
                                type="file"
                                accept="images/*"
                                name="file"
                                class={[
                                    "w-full rounded-full border border-gray-100 px-4 py-3",
                                    form?.message
                                        ? "border-red-600 text-red-600"
                                        : "",
                                ]}
                            />
                            {#if fieldErrors("#/profile_image")?.detail}
                                <span
                                    >{fieldErrors("#/profile_image")
                                        ?.detail}</span
                                >
                            {/if}
                        </div>

                        <div>
                            <button
                                aria-label="upload profile picture"
                                title="Save Profile Picture"
                                class="flex items-center justify-center p-3 rounded-full bg-primary-main-orange text-orange-950 cursor-pointer"
                            >
                                {#if isUpdatingProfile}
                                    <LoadingIcon
                                        height="1.5em"
                                        class="shrink-0"
                                    />
                                {:else}
                                    <FileUploadIcon
                                        height="1.5em"
                                        class="shrink-0"
                                    />
                                {/if}
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
