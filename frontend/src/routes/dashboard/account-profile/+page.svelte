<script lang="ts">
    import type { PageProps } from "./$types";
    import UserIcon from "@iconify-svelte/tabler/user";
    import MailIcon from "@iconify-svelte/tabler/mail";
    import PhoneIcon from "@iconify-svelte/tabler/phone";
    import AtIcon from "@iconify-svelte/tabler/at";
    import CircleCheckIcon from "@iconify-svelte/tabler/circle-check";
    import CalendarIcon from "@iconify-svelte/tabler/calendar";
    import FileDescriptionIcon from "@iconify-svelte/tabler/file-description";
    import ProfileCard from "#lib/components/cards/ProfileCard.svelte";
    import { format } from "date-fns";
    import UpdateProfile from "#lib/components/modals/profiles/UpdateProfile.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import SelectorIcon from "@iconify-svelte/tabler/selector";
    import CloseIcon from "@iconify-svelte/tabler/x";
    import BuildingIcon from "@iconify-svelte/tabler/building";
    import ThemeIcon from "@iconify-svelte/tabler/palette";
    import LogoutIcon from "@iconify-svelte/tabler/logout";
    import DeleteIcon from "@iconify-svelte/tabler/trash";
    import KeysIcon from "@iconify-svelte/tabler/lock";
    import { enhance } from "$app/forms";
    import PictureIcon from "@iconify-svelte/tabler/photo";

    const { data, form }: PageProps = $props();

    interface Props {
        title: string;
        description: string;
        icon: any;
        value: string | undefined | boolean | object;
        name: string;
    }

    const formattedDate = $derived(() => {
        return format(data.user.account_created_at, "MM-dd-yyyy");
    });

    const profileData: Props[] = $derived([
        {
            title: "First Name",
            description: "The name for the account",
            icon: UserIcon,
            value: data.user.first_name,
            name: "first_name",
        },
        {
            title: "Last Name",
            description: "The name for the account",
            icon: UserIcon,
            value: data.user.last_name,
            name: "last_name",
        },
        {
            title: "Email",
            description: "The email for the account",
            icon: MailIcon,
            value: data.user.email,
            name: "email",
        },
        {
            title: "phone number",
            description: "Current phone",
            icon: PhoneIcon,
            value: data.user.phone_number,
            name: "phone_number",
        },
        {
            title: "Username",
            description: "Name to display on profile",
            icon: AtIcon,
            value: data.user.username ?? "Not set",
            name: "username",
        },
        {
            title: "Email verified",
            description: "Email verification",
            icon: CircleCheckIcon,
            value: data.user.is_email_verified ?? "Not set",
            name: "is_email_verified",
        },
        {
            title: "Account created at",
            description: "Account creation date",
            icon: CalendarIcon,
            value: formattedDate() ?? "Not set",
            name: "account_created_at",
        },
        {
            title: "Bio",
            description: "User biography",
            icon: FileDescriptionIcon,
            value: data.user.bio ?? "Not set",
            name: "bio",
        },
    ]);

    const truncatedDescription = $derived(() => {
        return data.user?.bio?.slice(0, 30);
    });

    let openModal: boolean = $state(false);
    // for the field values
    let fieldName: string = $state("");
    let fieldValue: String | undefined | boolean | object = $state("");
    let fieldLabel: string = $state("");
    // for opening the more options

    let isOpeningOptions: boolean = $state(false);
    let isClosingOptions: boolean = $state(false);

    // for uploading the profile photo
    let openProfileModal: boolean = $state(false);

    const handleOpenModal = (
        name: string,
        value: string | undefined | boolean | object,
        label: string,
    ) => {
        openModal = true;
        fieldValue = value;
        fieldName = name;
        fieldLabel = label;
    };

    const handleCloseModal = () => {
        openModal = false;
    };

    // for the more options modal
    const handleOpenMoreOptions = () => {
        isOpeningOptions = true;
        isClosingOptions = false;
    };

    const handleCloseMoreOptions = () => {
        isClosingOptions = true;
    };

    const handleAnimationEnd = () => {
        if (isClosingOptions) {
            isOpeningOptions = false;
            isClosingOptions = false;
        }
    };

    const handleOpenUploadProfileModal = () => {
        openProfileModal = true;
    };

    const closeOpenUploadProfileModal = () => {
        openProfileModal = true;
    };
</script>

<div class="relative h-screen flex items-center justify-center overflow-hidden">
    <div
        class="bg-primary-slight-black w-full max-w-4xl px-5 py-5 rounded-4xl h-[calc(100vh-2rem)]"
    >
        <div class="h-full overflow-auto scrollbar-thin space-y-10 px-5">
            <!-- for the main header -->
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-5">
                    <div class="rounded-full border h-32 w-32"></div>
                    <div class="space-y-3">
                        <div>
                            <h1 class="capitalize text-lg font-semibold">
                                {data.user.first_name}
                            </h1>
                            <p>{data.user.email}</p>
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
                        onclick={handleOpenMoreOptions}
                        class="flex items-center justify-center cursor-pointer p-3 rounded-full bg-black hover:ring-1 transition duration-200"
                    >
                        <SelectorIcon height="1.5em" class="shrink-0" />
                    </button>
                </div>
            </div>

            <!-- for the main content here  -->
            <div class="space-y-1">
                {#each profileData as profile, index}
                    <ProfileCard
                        Icon={profile.icon}
                        title={profile.title}
                        description={profile.description}
                        value={profile.title === "Bio"
                            ? truncatedDescription()
                            : profile.value}
                        {index}
                        length={profileData.length}
                        name={profile.name}
                        openModal={() =>
                            handleOpenModal(
                                profile.name,
                                profile.value,
                                profile.title,
                            )}
                    />
                {/each}
            </div>
        </div>
    </div>
</div>

{#if openModal}
    <UpdateProfile
        name={fieldName}
        value={fieldValue}
        label={fieldLabel}
        closeModal={handleCloseModal}
        {form}
    />
{/if}

<!-- for the other options -->
{#if isOpeningOptions}
    <div
        class="fixed inset-0 z-100 bg-black/40 flex items-center justify-center"
    >
        <div
            class={[
                "absolute right-32 w-sm rounded-4xl space-y-5 px-5 py-5 top-28 bg-primary-slight-black border border-gray-300/10 z-100",
                isClosingOptions
                    ? "motion-opacity-out-5"
                    : "motion-preset-slide-down-sm motion-duration-500 motion-opacity-in-10",
            ]}
            onanimationend={handleAnimationEnd}
        >
            <div class="flex items-center justify-between">
                <h1 class="text-xl font-semibold capitalize">more</h1>
                <button
                    aria-label="closing options"
                    title="Close Options"
                    onclick={handleCloseMoreOptions}
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
                            href="/account-profile/manage-business"
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
                                <LogoutIcon height="1.3em" class="shrink-0" />
                                <span class="first-letter:uppercase"
                                    >Log out</span
                                >
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
                                <span class="capitalize"
                                    >Delete your account</span
                                >
                            </button>
                        </form>
                    </li>
                </ul>
            </div>
        </div>
    </div>
{/if}
