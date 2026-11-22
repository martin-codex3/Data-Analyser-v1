<script lang="ts">
    import { PUBLIC_API_ENDPOINT } from "$app/env/public";
    const { user } = $props();
</script>

<div
    class="fixed bg-black/10 backdrop-blur-sm inset-0 z-100 flex items-center justify-center"
>
    <div
        class="bg-primary-slight-black space-y-5 w-full max-w-sm rounded-4xl border border-primary-main-orange/10"
    >
        <img
            src={`${PUBLIC_API_ENDPOINT}${user.profile_image_url}`}
            alt=""
            class="h-70 w-full object-cover bg-cover rounded-tr-4xl rounded-tl-4xl"
        />

        <div class="px-5">
            <h1 class="first-letter:capitalize font-semibold text-xl">
                upload your profile
            </h1>
            <p>upload files in (JPEG, JPG, PNG, GIF) format</p>
        </div>

        <div class="flex items-center w-full">
            <input
                type="file"
                class="w-full rounded-lg border border-gray-100"
            />

            <button aria-label="upload profile picture"></button>
        </div>
    </div>
</div>
