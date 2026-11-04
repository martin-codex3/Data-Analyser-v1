<script lang="ts">
  import type { TenantResponse } from "#lib/types/tenant/tenant_response.ts";

  let { tenant }: { tenant: TenantResponse } = $props();
</script>

<div>
  <div>
    <h1 class="text-xl capitalize">organisation details</h1>
    <p>{tenant.business_name}</p>
  </div>
</div>
