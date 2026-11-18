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

    const { data }: PageProps = $props();

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
    const fieldName: string = $state("");
    const fieldValue: String = $state("");
    const fieldLabel: string = $state("");

    const handleOpenModal = (
        name: string,
        value: string | undefined | boolean | object,
        label: string,
    ) => {
        openModal = true;
        if (openModal) {
            fieldName: name;
            fieldValue: value;
            fieldLabel: label;
        }
    };

    const handleCloseModal = () => {
        openModal = false;
    };
</script>

<div class="h-screen flex items-center justify-center overflow-hidden">
    <div
        class="bg-primary-slight-black w-full max-w-4xl px-5 py-5 rounded-4xl h-[calc(100vh-2rem)]"
    >
        <div class="h-full overflow-auto scrollbar-thin space-y-10 px-5">
            <!-- for the main header -->
            <div class="flex items-center gap-5">
                <div class="rounded-full border h-20 w-20"></div>
                <div>
                    <h1 class="capitalize text-lg font-semibold">
                        {data.user.first_name}
                    </h1>
                    <p>{data.user.email}</p>
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
    <UpdateProfile name={fieldName} value={fieldValue} label={fieldLabel} />
{/if}
