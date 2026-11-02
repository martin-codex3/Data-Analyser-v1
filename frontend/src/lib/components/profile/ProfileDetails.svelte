<script lang="ts">
  import type { User } from "#lib/types/users/user.ts";
  import CameraIcon from "@iconify-svelte/tabler/camera";

  let { user }: { user: User } = $props();
</script>

<div>
  <div class="motion-preset-slide-down-sm motion-duration-200">
    <div class="">
      <div class="flex items-center gap-3">
        <div class="relative">
          <div class="h-18 w-18 rounded-full bg-blue-100"></div>
          <div class="absolute bottom-0 right-0">
            <button
              aria-label="update-profile-button"
              class="flex items-center justify-center bg-primary-main-blue p-2 rounded-full border cursor-pointer text-blue-100"
            >
              <CameraIcon height="1.2em" class="shrink-0" />
            </button>
          </div>
        </div>
        <div>
          <h1>{user.first_name}</h1>
          <p>{user.account_verified_at}</p>
        </div>
      </div>

      <!-- for the other content here -->
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2"></div>
      </div>
    </div>
  </div>
</div>
