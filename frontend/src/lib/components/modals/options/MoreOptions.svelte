<script lang="ts">
    import CloseIcon from "@iconify-svelte/tabler/x";
    import BuildingIcon from "@iconify-svelte/tabler/building";
    import ThemeIcon from "@iconify-svelte/tabler/palette";
    import LogoutIcon from "@iconify-svelte/tabler/logout";
    import DeleteIcon from "@iconify-svelte/tabler/trash";
    import KeysIcon from "@iconify-svelte/tabler/lock";
    import { enhance } from "$app/forms";
    import { toast } from "svelte-sonner";

    const { closeModal } = $props();

    const handleCloseModal = () => {
        closeModal();
    };
</script>

<div class="fixed inset-0 z-100 bg-black/40 flex items-center justify-center">
    <div
        class="absolute right-32 w-sm rounded-4xl space-y-5 px-5 py-5 top-32 bg-primary-slight-black border border-gray-300/10 z-100 motion-preset-slide-down-sm motion-duration-150"
    >
        <div class="flex items-center justify-between">
            <h1 class="text-xl font-semibold capitalize">more</h1>
            <button
                aria-label="closing options"
                title="Close Options"
                onclick={handleCloseModal}
                class="flex items-center justify-center cursor-pointer transition duration-300"
            >
                <CloseIcon
                    height="2.5em"
                    class="flex items-center justify-center hover:bg-black rounded-full p-2"
                />
            </button>
        </div>

        <!-- for the main content here -->
        <div>
            <ul class="space-y-3">
                <li>
                    <a
                        href="/dashboard/organisation-profile"
                        class="flex items-center gap-3 rounded-full px-3 py-2 text-lg hover:bg-white hover:text-primary-main-black transition duration-200"
                    >
                        <BuildingIcon height="1.3em" class="shrink-0" />
                        <span class="first-letter:uppercase"
                            >manage your business</span
                        >
                    </a>
                </li>

                <li>
                    <a
                        href="/account-profile/manage-business"
                        class="flex items-center gap-3 rounded-full px-3 py-2 text-lg hover:bg-white hover:text-primary-main-black transition duration-200"
                    >
                        <ThemeIcon height="1.3em" class="shrink-0" />
                        <span class="first-letter:uppercase"
                            >themes and colors</span
                        >
                    </a>
                </li>

                <!-- for updating the user password here -->
                <li>
                    <form
                        action=""
                        method="POST"
                        use:enhance={() => {
                            return async ({ update, result }) => {
                                await update();
                            };
                        }}
                    >
                        <button
                            aria-label="logout button"
                            title="Log out"
                            class="flex items-center gap-3 rounded-full px-3 py-2 text-lg cursor-pointer w-full hover:bg-white hover:text-primary-main-black transition duration-200"
                        >
                            <KeysIcon height="1.3em" class="shrink-0" />
                            <span class="first-letter:uppercase"
                                >update your password</span
                            >
                        </button>
                    </form>
                </li>

                <li>
                    <form
                        action="?/logoutUsers"
                        method="POST"
                        use:enhance={() => {
                            return async ({ update, result }) => {
                                await update();

                                if (result.type === "error") {
                                    toast.error("Something went wrong");
                                }

                                if (result.type === "failure") {
                                    toast.error("Something went wrong");
                                }

                                if (result.type === "success") {
                                    toast.success("Logged out successfully");
                                }
                            };
                        }}
                    >
                        <button
                            aria-label="logout button"
                            title="Log out"
                            class="flex items-center gap-3 rounded-full px-3 py-2 text-lg cursor-pointer w-full hover:bg-white hover:text-primary-main-black transition duration-200"
                        >
                            <LogoutIcon height="1.3em" class="shrink-0" />
                            <span class="first-letter:uppercase">Log out</span>
                        </button>
                    </form>
                </li>

                <li>
                    <form
                        action=""
                        method="POST"
                        use:enhance={() => {
                            return async ({ result, update }) => {};
                        }}
                    >
                        <button
                            aria-label="logout button"
                            title="Log out"
                            class="flex items-center gap-3 rounded-full px-3 py-2 text-lg cursor-pointer hover:bg-white hover:text-primary-main-black w-full hover:opacity-80 transition duration-200"
                        >
                            <DeleteIcon height="1.3em" class="shrink-0" />
                            <span class="capitalize">Delete your account</span>
                        </button>
                    </form>
                </li>
            </ul>
        </div>
    </div>
</div>
