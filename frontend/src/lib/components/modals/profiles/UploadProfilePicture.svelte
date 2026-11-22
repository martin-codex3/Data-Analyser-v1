<script lang="ts">
    import { PUBLIC_API_ENDPOINT } from "$app/env/public";
    import FileUploadIcon from "@iconify-svelte/tabler/pencil";
    import CloseIcon from "@iconify-svelte/tabler/x";

    const { user, closeModal } = $props();

    const handleCloseModal = () => {
        closeModal();
    };

    let files: FileList | null | undefined = $state();
    let uploadedFile: string = $state("");

    const handleUploadFile = async () => {
        if (!files || files.length === 0) {
            return;
        }
        for (let file of files!) {
            uploadedFile = file?.name;
        }

        if (uploadedFile) {
        }
    };
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

            <div class="flex items-center w-full gap-3">
                <input
                    type="file"
                    accept="images/*"
                    bind:files
                    class="w-full rounded-full border border-gray-100 px-4 py-3"
                />

                <button
                    aria-label="upload profile picture"
                    title="Save Profile Picture"
                    onclick={handleUploadFile}
                    class="flex items-center justify-center p-3 rounded-full bg-primary-main-orange text-orange-950 cursor-pointer"
                >
                    <FileUploadIcon height="1.5em" class="shrink-0" />
                </button>
            </div>
        </div>
    </div>
</div>
