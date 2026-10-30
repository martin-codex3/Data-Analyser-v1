<script lang="ts">
  import GeneralIcon from "@iconify-svelte/tabler/settings";
  import BrightnessIcon from "@iconify-svelte/tabler/brightness-auto-filled";
  import NotificationsIcon from "@iconify-svelte/tabler/notification";
  import SecurityIcon from "@iconify-svelte/tabler/lock";
  import KeyboardIcon from "@iconify-svelte/tabler/keyboard";
  import UsageIcon from "@iconify-svelte/tabler/meter-cube";
  let { children } = $props();

  interface Link {
    label: string;
    to: string;
    icon: any;
  }

  let settingsLinks: Link[] = [
    { label: "General", to: "/dashboard/settings", icon: GeneralIcon },
    { label: "General", to: "/dashboard/settings", icon: GeneralIcon },
  ];
</script>

<div class="main__main__wrapper">
  <nav
    class="bg-white border-x border-x-gray-300 h-[calc(100vh)] max-w-90 overflow-auto scrollbar-thin"
  >
    <div>
      <h1 class="text-2xl capitalize">settings</h1>
    </div>
  </nav>
  <main class=""></main>
</div>
