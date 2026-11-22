<script lang="ts">
    import SelectorIcon from "@iconify-svelte/tabler/selector";
    import PictureIcon from "@iconify-svelte/tabler/photo";
    import { PUBLIC_API_ENDPOINT } from "$app/env/public";
    import type { PageProps } from "./$types";

    const { data }: PageProps = $props();

    $inspect(data);
</script>

<div class="h-screen overflow-hidden flex items-center justify-center">
    <div
        class="w-full max-w-4xl rounded-4xl bg-primary-slight-black h-[calc(100vh-2rem)] px-5 py-5"
    >
        <div class="h-full overflow-auto scrollbar-thin">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-5">
                    <div class="rounded-full h-32 w-32 border"></div>
                    <div class="space-y-3">
                        <div>
                            <h1 class="capitalize text-lg font-semibold">
                                Martin
                            </h1>
                            <p>martinsilungwe12@gmail.com</p>
                        </div>
                        <form action="">
                            <button
                                aria-label="uploading profile pictures"
                                title="Upload Profile"
                                class="flex items-center gap-2 justify-center cursor-pointer hover:opacity-80 transition duration-200 bg-green-100 text-green-900 rounded-full px-4 py-2"
                            >
                                <PictureIcon height="1.5em" class="shrink-0" />
                                <span>upload profile</span>
                            </button>
                        </form>
                    </div>
                </div>

                <div class="">
                    <button
                        aria-label="open options"
                        class="flex items-center justify-center cursor-pointer p-3 rounded-full bg-black hover:ring-1 transition duration-200"
                    >
                        <SelectorIcon height="1.5em" class="shrink-0" />
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
