<script lang="ts">
  import type { Component } from "svelte";
  import type { TenantResponse } from "#lib/types/tenant/tenant_response.ts";
  import PencilIcon from "@iconify-svelte/tabler/pencil";
  import BuildingIcon from "@iconify-svelte/tabler/building";
  import BriefcaseIcon from "@iconify-svelte/tabler/briefcase";
  import MailIcon from "@iconify-svelte/tabler/mail";
  import PhoneIcon from "@iconify-svelte/tabler/phone";
  import CertificateIcon from "@iconify-svelte/tabler/certificate";
  import FactoryIcon from "@iconify-svelte/tabler/building-factory-2";
  import MapPinIcon from "@iconify-svelte/tabler/map-pin";
  import SignpostIcon from "@iconify-svelte/tabler/sign-left";
  import SkyscraperIcon from "@iconify-svelte/tabler/building-skyscraper";
  import MapIcon from "@iconify-svelte/tabler/map-2";
  import MailboxIcon from "@iconify-svelte/tabler/mailbox";
  import FlagIcon from "@iconify-svelte/tabler/flag";
  import ActivityIcon from "@iconify-svelte/tabler/activity";
  import WorldWwwIcon from "@iconify-svelte/tabler/world-www";
  import LinkIcon from "@iconify-svelte/tabler/link";
  import CalendarPlusIcon from "@iconify-svelte/tabler/calendar-plus";
  import CalendarTimeIcon from "@iconify-svelte/tabler/calendar-time";
  import FileDescriptionIcon from "@iconify-svelte/tabler/file-description";
  import ItemCard from "../cards/ItemCard.svelte";
  import UpdateAccount from "../modals/UpdateAccount.svelte";
  import type { ActionData } from "../../../routes/$types";

  let openUpdateModal: boolean = $state(false);

  let { tenant, form }: { tenant: TenantResponse; form: ActionData } = $props();

  // for the fields
  let fieldLabel: string = $state("");
  let fieldValue: string | string[] = $state("");
  let fieldName: string = $state("");

  type TenantField = {
    name: keyof TenantResponse & string;
    label: string;
    icon: Component | any;
  };

  const fields: TenantField[] = [
    { name: "business_name", label: "Business name", icon: BuildingIcon },
    { name: "business_type", label: "Business type", icon: BriefcaseIcon },
    { name: "business_email", label: "Business email", icon: MailIcon },
    { name: "business_phone", label: "Business phone", icon: PhoneIcon },
    {
      name: "registration_number",
      label: "Registration number",
      icon: CertificateIcon,
    },
    { name: "industry", label: "Industry", icon: FactoryIcon },
    { name: "address_line_1", label: "Address line 1", icon: MapPinIcon },
    { name: "address_line_2", label: "Address line 2", icon: SignpostIcon },
    { name: "city", label: "City", icon: SkyscraperIcon },
    { name: "region", label: "Region", icon: MapIcon },
    { name: "postal_code", label: "Postal code", icon: MailboxIcon },
    { name: "country_code", label: "Country code", icon: FlagIcon },
    { name: "status", label: "Status", icon: ActivityIcon },
    { name: "website_url", label: "Website url", icon: WorldWwwIcon },
    { name: "slug", label: "Slug", icon: LinkIcon },
    { name: "created_at", label: "Created at", icon: CalendarPlusIcon },
    { name: "updated_at", label: "Updated at", icon: CalendarTimeIcon },
    { name: "description", label: "Description", icon: FileDescriptionIcon },
  ];

  const handleOpenUpdateModal = (
    value: string | string[],
    label: string,
    name: string,
  ) => {
    fieldLabel = label;
    fieldValue = value;
    fieldName = name;
    openUpdateModal = true;
  };

  const handleCloseModal = () => {
    openUpdateModal = false;
  };
</script>

<div class="">
  <div class="motion-preset-slide-down-sm motion-duration-300">
    <div>
      <h1 class="text-xl capitalize">organisation details</h1>
      <p>{tenant.business_name}</p>
    </div>

    <!-- for the main content here -->
    <div>
      <div class="space-y-1">
        {#each fields as field (field.name)}
          <ItemCard
            title={field.label}
            headerIcon={field.icon}
            length={fields.length}
            value={tenant[field.name]}
            iconData={PencilIcon}
            openModal={() =>
              handleOpenUpdateModal(
                tenant[field.name] as string | string[],
                field.label,
                field.name,
              )}
          />
        {/each}
      </div>
    </div>
  </div>

  <!-- for the modal here -->
  {#if openUpdateModal}
    <UpdateAccount
      closeModal={handleCloseModal}
      {fieldLabel}
      {fieldName}
      {fieldValue}
      {form}
    />
  {/if}
</div>
