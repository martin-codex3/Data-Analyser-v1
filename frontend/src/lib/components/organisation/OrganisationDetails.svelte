<script lang="ts">
  import type { TenantResponse } from "#lib/types/tenant/tenant_response.ts";
  import PencilIcon from "@iconify-svelte/tabler/pencil";
  import BuildingIcon from "@iconify-svelte/tabler/building";
  import ItemCard from "../cards/ItemCard.svelte";

  let openUpdateModal: boolean = $state(false);

  let { tenant }: { tenant: TenantResponse } = $props();
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
        />
      </div>
    </div>
  </div>
</div>
