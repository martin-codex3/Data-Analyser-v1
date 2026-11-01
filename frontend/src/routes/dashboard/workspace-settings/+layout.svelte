<script lang="ts">
  import GeneralIcon from "@iconify-svelte/tabler/settings";
  import AppearanceIcon from "@iconify-svelte/tabler/brightness-auto-filled";
  import NotificationsIcon from "@iconify-svelte/tabler/bell";
  import SecurityIcon from "@iconify-svelte/tabler/lock";
  import KeyboardIcon from "@iconify-svelte/tabler/keyboard";
  import UsageIcon from "@iconify-svelte/tabler/dashboard";
  import StorageIcon from "@iconify-svelte/tabler/folder";
  import BillingIcon from "@iconify-svelte/tabler/wallet";
  import CookieIcon from "@iconify-svelte/tabler/cookie";
  import { page } from "$app/state";

  let { children } = $props();

  interface Link {
    label: string;
    to: string;
    icon: any;
  }

  let settingsLinks: Link[] = [
    {
      label: "General",
      to: "/dashboard/workspace-settings",
      icon: GeneralIcon,
    },
    {
      label: "Appearance",
      to: "/dashboard/settings/appearance",
      icon: AppearanceIcon,
    },
    {
      label: "Notifications",
      to: "/dashboard/settings/notifications",
      icon: NotificationsIcon,
    },
    {
      label: "Security and Login",
      to: "/dashboard/settings/security",
      icon: SecurityIcon,
    },
    { label: "Storage", to: "/dashboard/settings/storage", icon: StorageIcon },
    {
      label: "Keyboard",
      to: "/dashboard/settings/keyboard",
      icon: KeyboardIcon,
    },
    { label: "Usage", to: "/dashboard/settings/usage", icon: UsageIcon },
    { label: "Billing", to: "/dashboard/settings/billing", icon: BillingIcon },
    {
      label: "Cookie Preferences",
      to: "/dashboard/settings/cookie-preferences",
      icon: CookieIcon,
    },
  ];
</script>

<div class="main__main__wrapper">
  <nav
    class="fixed bg-white border-r border-r-gray-300 px-5 space-y-10 py-3 h-[calc(100vh)] min-w-90 overflow-auto scrollbar-thin"
  >
    <div>
      <h1 class="text-2xl capitalize">settings</h1>
    </div>

    <div>
      <ul class="space-y-2">
        {#each settingsLinks as link}
          <li>
            <a
              href={link.to}
              title={link.label}
              class={[
                "flex items-center gap-2 px-3 py-3 rounded-full hover:bg-blue-50 hover:text-blue-900 transition duration-300",
                page.url.pathname === link.to ? "bg-blue-50 text-blue-900" : "",
              ]}
            >
              <link.icon height="1.7em" />
              <span>{link.label}</span>
            </a>
          </li>
        {/each}
      </ul>
    </div>
  </nav>
  <main class="ms-90">
    {@render children()}
  </main>
</div>
