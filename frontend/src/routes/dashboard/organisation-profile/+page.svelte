<script lang="ts">
    import SelectorIcon from "@iconify-svelte/tabler/selector";
    import PictureIcon from "@iconify-svelte/tabler/photo";
    import type { PageProps } from "./$types";
    import TenantCard from "#lib/components/cards/TenantCard.svelte";
    import BuildingStoreIcon from "@iconify-svelte/tabler/building-store";
    import BriefcaseIcon from "@iconify-svelte/tabler/briefcase";
    import MailIcon from "@iconify-svelte/tabler/mail";
    import PhoneIcon from "@iconify-svelte/tabler/phone";
    import FileCertificateIcon from "@iconify-svelte/tabler/file-certificate";
    import CategoryIcon from "@iconify-svelte/tabler/category";
    import MapPinIcon from "@iconify-svelte/tabler/map-pin";
    import HomeIcon from "@iconify-svelte/tabler/home";
    import BuildingCityIcon from "@iconify-svelte/tabler/building-community";
    import MapIcon from "@iconify-svelte/tabler/map";
    import MailboxIcon from "@iconify-svelte/tabler/mailbox";
    import FlagIcon from "@iconify-svelte/tabler/flag";
    import ActivityIcon from "@iconify-svelte/tabler/activity";
    import WorldIcon from "@iconify-svelte/tabler/world";
    import LinkIcon from "@iconify-svelte/tabler/link";
    import SettingsIcon from "@iconify-svelte/tabler/settings";
    import FileDescriptionIcon from "@iconify-svelte/tabler/file-description";
    import PhotoIcon from "@iconify-svelte/tabler/photo";
    import UserCheckIcon from "@iconify-svelte/tabler/user-check";
    import CalendarPlusIcon from "@iconify-svelte/tabler/calendar-plus";
    import CalendarEventIcon from "@iconify-svelte/tabler/calendar-event";
    import TrashIcon from "@iconify-svelte/tabler/trash";
    import UpdateTenantProfile from "#lib/components/modals/tenants/UpdateTenantProfile.svelte";

    const { data, form }: PageProps = $props();

    interface Props {
        title: string;
        description: string;
        value: string | undefined | object | boolean;
        name: string;
        Icon: any;
    }

    const tenantData: Props[] = $derived([
        {
            title: "Business name",
            description: "Name of the business",
            value: data.tenant.business_name ?? "Unset",
            name: "business_name",
            Icon: BuildingStoreIcon,
        },
        {
            title: "Business type",
            description: "Type or legal structure of the business",
            value: data.tenant.business_type ?? "Unset",
            name: "business_type",
            Icon: BriefcaseIcon,
        },
        {
            title: "Business email",
            description: "Primary contact email for the business",
            value: data.tenant.business_email ?? "Unset",
            name: "business_email",
            Icon: MailIcon,
        },
        {
            title: "Business phone",
            description: "Primary contact phone number",
            value: data.tenant.business_phone ?? "Unset",
            name: "business_phone",
            Icon: PhoneIcon,
        },
        {
            title: "Registration number",
            description: "Official business registration number",
            value: data.tenant.registration_number ?? "Unset",
            name: "registration_number",
            Icon: FileCertificateIcon,
        },
        {
            title: "Industry",
            description: "Industry sector the business operates in",
            value: data.tenant.industry ?? "Unset",
            name: "industry",
            Icon: CategoryIcon,
        },
        {
            title: "Address line 1",
            description: "Street address line 1",
            value: data.tenant.address_line_1 ?? "Unset",
            name: "address_line_1",
            Icon: MapPinIcon,
        },
        {
            title: "Address line 2",
            description: "Apartment, suite, or street address line 2",
            value: data.tenant.address_line_2 ?? "Unset",
            name: "address_line_2",
            Icon: HomeIcon,
        },
        {
            title: "City",
            description: "City where the business is located",
            value: data.tenant.city ?? "Unset",
            name: "city",
            Icon: BuildingCityIcon,
        },
        {
            title: "Region",
            description: "State, province, or region",
            value: data.tenant.region ?? "Unset",
            name: "region",
            Icon: MapIcon,
        },
        {
            title: "Postal code",
            description: "ZIP or postal code",
            value: data.tenant.postal_code ?? "Unset",
            name: "postal_code",
            Icon: MailboxIcon,
        },
        {
            title: "Country code",
            description: "ISO country code",
            value: data.tenant.country_code ?? "Unset",
            name: "country_code",
            Icon: FlagIcon,
        },
        {
            title: "Status",
            description: "Current account or tenant status",
            value: data.tenant.status ?? "Unset",
            name: "status",
            Icon: ActivityIcon,
        },
        {
            title: "Website URL",
            description: "Official business website",
            value: data.tenant.website_url ?? "Unset",
            name: "website_url",
            Icon: WorldIcon,
        },
        {
            title: "Slug",
            description: "URL-friendly identifier for the tenant",
            value: data.tenant.slug ?? "Unset",
            name: "slug",
            Icon: LinkIcon,
        },
        {
            title: "Settings",
            description: "Tenant configuration settings",
            value: data.tenant.settings ?? "Unset",
            name: "settings",
            Icon: SettingsIcon,
        },
        {
            title: "Description",
            description: "Summary or description of the business",
            value: data.tenant.description ?? "Unset",
            name: "description",
            Icon: FileDescriptionIcon,
        },
        {
            title: "Business logo",
            description: "Logo URL or asset reference",
            value: data.tenant.business_logo ?? "Unset",
            name: "business_logo",
            Icon: PhotoIcon,
        },

        {
            title: "Created at",
            description: "Timestamp when the tenant was created",
            value: data.tenant.created_at ?? "Unset",
            name: "created_at",
            Icon: CalendarPlusIcon,
        },
        {
            title: "Updated at",
            description: "Timestamp of the last update",
            value: data.tenant.updated_at ?? "Unset",
            name: "updated_at",
            Icon: CalendarEventIcon,
        },
        {
            title: "Deleted",
            description: "Whether the tenant is marked as deleted",
            value: data.tenant.is_deleted,
            name: "is_deleted",
            Icon: TrashIcon,
        },
    ]);

    let openModal: boolean = $state(false);
    let fieldName: string = $state("");
    let fieldValue: String | undefined | boolean | object = $state("");
    let fieldLabel: string = $state("");

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
</script>

<div class="h-screen overflow-hidden flex items-center justify-center">
    <div
        class="w-full max-w-4xl rounded-4xl bg-primary-slight-black h-[calc(100vh-2rem)] px-5 py-5"
    >
        <div class="h-full overflow-auto scrollbar-thin space-y-10 px-5">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-5">
                    <div class="rounded-full h-32 w-32 border"></div>
                    <div class="space-y-3">
                        <div>
                            <h1 class="capitalize text-lg font-semibold">
                                {data.tenant.business_name}
                            </h1>
                            <p>{data.tenant.business_email}</p>
                        </div>
                        <form action="">
                            <button
                                aria-label="uploading profile pictures"
                                title="Upload Profile"
                                class="flex items-center gap-2 justify-center cursor-pointer hover:opacity-80 transition duration-200 bg-green-100 text-green-900 rounded-full px-4 py-2"
                            >
                                <PictureIcon height="1.5em" class="shrink-0" />
                                <span>upload organisation logo</span>
                            </button>
                        </form>
                    </div>
                </div>
            </div>

            <!-- for the main content here  -->
            <div class="space-y-1">
                {#each tenantData as tenant, index}
                    <TenantCard
                        Icon={tenant.Icon}
                        title={tenant.title}
                        description={tenant.description}
                        value={tenant.value}
                        {index}
                        length={tenantData.length}
                        name={tenant.name}
                        openModal={() =>
                            handleOpenModal(
                                tenant.name,
                                tenant.value,
                                tenant.title,
                            )}
                    />
                {/each}
            </div>
        </div>
    </div>
</div>

{#if openModal}
    <UpdateTenantProfile
        name={fieldName}
        value={fieldValue}
        label={fieldLabel}
        closeModal={handleCloseModal}
        {form}
    />
{/if}
