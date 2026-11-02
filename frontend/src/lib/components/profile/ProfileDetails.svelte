<script lang="ts">
  import type { User } from "#lib/types/users/user.ts";
  import CameraIcon from "@iconify-svelte/tabler/camera";
  import NameIcon from "@iconify-svelte/tabler/user";
  import PencilIcon from "@iconify-svelte/tabler/pencil";

  let { user }: { user: User } = $props();
</script>

<div>
  <div class="motion-preset-slide-down-sm motion-duration-200">
    <div class="space-y-5">
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
      <div class="space-y-1">
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-tr-3xl rounded-tl-3xl rounded-bl-lg rounded-br-lg"
        >
          <div class="flex items-center gap-2">
            <NameIcon height="1.8em" class="shrink-0" />
            <h1 class="first-letter:uppercase">first name</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2>{user.first_name}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <NameIcon height="1.8em" class="shrink-0" />
            <h1 class="first-letter:uppercase">last name</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.last_name}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- for the phone number -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <NameIcon height="1.8em" class="shrink-0" />
            <h1 class="first-letter:uppercase">phone number</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.phone_number}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- for the username -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <NameIcon height="1.8em" class="shrink-0" />
            <h1 class="first-letter:uppercase">username</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.username}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- for the email -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <NameIcon height="1.8em" class="shrink-0" />
            <h1 class="first-letter:uppercase">last name</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.last_name}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- if the email confirmed -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <NameIcon height="1.8em" class="shrink-0" />
            <h1 class="first-letter:uppercase">is email confirmed</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.is_email_verified}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- email confirmed at -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <NameIcon height="1.8em" class="shrink-0" />
            <h1 class="first-letter:uppercase">email confirmed at</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.account_verified_at}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
