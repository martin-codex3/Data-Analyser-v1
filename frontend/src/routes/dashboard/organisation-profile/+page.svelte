<script lang="ts">
    import SelectorIcon from "@iconify-svelte/tabler/selector";
    import PictureIcon from "@iconify-svelte/tabler/photo";
    import { PUBLIC_API_ENDPOINT } from "$app/env/public";
    import type { PageProps } from "./$types";

    const { data }: PageProps = $props();

    interface Props {
        title: string;
        description: string;
        value: string | undefined | object | boolean;
        name: string;
    }

    const tenantData: Props[] = $derived([
        {
            title: "Business name",
            description: "Name of the business",
            value: data.tenant.business_name ?? "Unset",
            name: "business_name",
        },
        {
            title: "Business type",
            description: "Type or legal structure of the business",
            value: data.tenant.business_type ?? "Unset",
            name: "business_type",
        },
        {
            title: "Business email",
            description: "Primary contact email for the business",
            value: data.tenant.business_email ?? "Unset",
            name: "business_email",
        },
        {
            title: "Business phone",
            description: "Primary contact phone number",
            value: data.tenant.business_phone ?? "Unset",
            name: "business_phone",
        },
        {
            title: "Registration number",
            description: "Official business registration number",
            value: data.tenant.registration_number ?? "Unset",
            name: "registration_number",
        },
        {
            title: "Industry",
            description: "Industry sector the business operates in",
            value: data.tenant.industry ?? "Unset",
            name: "industry",
        },
        {
            title: "Address line 1",
            description: "Street address line 1",
            value: data.tenant.address_line_1 ?? "Unset",
            name: "address_line_1",
        },
        {
            title: "Address line 2",
            description: "Apartment, suite, or street address line 2",
            value: data.tenant.address_line_2 ?? "Unset",
            name: "address_line_2",
        },
        {
            title: "City",
            description: "City where the business is located",
            value: data.tenant.city ?? "Unset",
            name: "city",
        },
        {
            title: "Region",
            description: "State, province, or region",
            value: data.tenant.region ?? "Unset",
            name: "region",
        },
        {
            title: "Postal code",
            description: "ZIP or postal code",
            value: data.tenant.postal_code ?? "Unset",
            name: "postal_code",
        },
        {
            title: "Country code",
            description: "ISO country code",
            value: data.tenant.country_code ?? "Unset",
            name: "country_code",
        },
        {
            title: "Status",
            description: "Current account or tenant status",
            value: data.tenant.status ?? "Unset",
            name: "status",
        },
        {
            title: "Website URL",
            description: "Official business website",
            value: data.tenant.website_url ?? "Unset",
            name: "website_url",
        },
        {
            title: "Slug",
            description: "URL-friendly identifier for the tenant",
            value: data.tenant.slug ?? "Unset",
            name: "slug",
        },
        {
            title: "Settings",
            description: "Tenant configuration settings",
            value: data.tenant.settings ?? "Unset",
            name: "settings",
        },
        {
            title: "Description",
            description: "Summary or description of the business",
            value: data.tenant.description ?? "Unset",
            name: "description",
        },
        {
            title: "Business logo",
            description: "Logo URL or asset reference",
            value: data.tenant.business_logo ?? "Unset",
            name: "business_logo",
        },
        {
            title: "Created by",
            description: "ID of the user who created the tenant",
            value: data.tenant.created_by_id ?? "Unset",
            name: "created_by_id",
        },
        {
            title: "Created at",
            description: "Timestamp when the tenant was created",
            value: data.tenant.created_at ?? "Unset",
            name: "created_at",
        },
        {
            title: "Updated at",
            description: "Timestamp of the last update",
            value: data.tenant.updated_at ?? "Unset",
            name: "updated_at",
        },
        {
            title: "Deleted",
            description: "Whether the tenant is marked as deleted",
            value: data.tenant.is_deleted,
            name: "is_deleted",
        },
    ]);
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

            <!-- for the main content here  -->
            <div></div>
        </div>
    </div>
</div>
