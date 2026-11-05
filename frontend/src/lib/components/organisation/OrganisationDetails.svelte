<script lang="ts">
  import type { TenantResponse } from "#lib/types/tenant/tenant_response.ts";
  import PencilIcon from "@iconify-svelte/tabler/pencil";
  import BuildingIcon from "@iconify-svelte/tabler/building";
  import ItemCard from "../cards/ItemCard.svelte";
  import UpdateAccount from "../modals/UpdateAccount.svelte";
  import type { ActionData } from "../../../routes/$types";

  let openUpdateModal: boolean = $state(false);

  let { tenant, form }: { tenant: TenantResponse; form: ActionData } = $props();

  // for the fields
  let fieldLabel: string = $state("");
  let fieldValue: string = $state("");
  let fieldName: string = $state("");

  const handleOpenUpdateModal = (
    value: string,
    label: string,
    name: string,
  ) => {
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
      <div>
        <ItemCard
          title="Business name"
          headerIcon={BuildingIcon}
          value={tenant.business_name}
          iconData={PencilIcon}
          openModal={handleOpenUpdateModal}
        />
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
