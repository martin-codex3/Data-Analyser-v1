<script lang="ts">
  import { page } from "$app/state";
  import OverviewIcon from "@iconify-svelte/tabler/dashboard";
  import DocumentsIcon from "@iconify-svelte/tabler/file";
  import DataSetIcon from "@iconify-svelte/tabler/database";
  import GroupIcon from "@iconify-svelte/tabler/users-group";
  import ChatIcon from "@iconify-svelte/tabler/message";
  import ProcessingIcon from "@iconify-svelte/tabler/time-duration-0";
  import SettingsIcon from "@iconify-svelte/tabler/settings";
  import SecurityIcon from "@iconify-svelte/tabler/shield";

  let { children } = $props();

  interface Link {
    label: string;
    to: string;
    icon: any;
  }

  //   for the overview links
  let overviewLinks: Link[] = [
    { label: "Overview", to: "/dashboard", icon: OverviewIcon },
    { label: "Documents", to: "/dashboard/documents", icon: DocumentsIcon },
    { label: "", to: "/dashboard", icon: DataSetIcon },
  ];

  //   for the collaborations
  let collaborationLinks: any[] = [
    { label: "Team Members", to: "dashboard/team-members", icon: GroupIcon },
    {
      label: "Comments & Activity",
      to: "dashboard/comments-activity",
      icon: ChatIcon,
    },
    {
      label: "Processing Jobs",
      to: "dashboard/processing-jobs",
      icon: ProcessingIcon,
    },
  ];

  let administrationLinks: any[] = [
    {
      label: "Workspace Settings",
      to: "dashboard/workspace-settings",
      icon: SettingsIcon,
    },

    {
      label: "Security & Audit Logs",
      to: "dashboard/audit-logs",
      icon: SecurityIcon,
    },
  ];
</script>

<div class="main__content__wrapper bg-gray-100 px-5 py-5">
  <nav
    class="main__navigation fixed h-screen w-32 rounded-3xl bg-white border px-7 py-5 border-gray-200"
  >
    <div class="nav__wrapper">
      <div></div>
      <div class="">
        <ul class="flex flex-col gap-5">
          <div class="space-y-2">
            {#each overviewLinks as link}
              <li class="">
                <a
                  href={link.to}
                  class="flex items-center justify-center hover:bg-mauve-100 rounded-full p-2"
                >
                  <link.icon height="1.8em" />
                </a>
              </li>
            {/each}
          </div>

          <!-- for the collaborations here -->
          <div class="space-y-2">
            {#each overviewLinks as link}
              <li>
                <a
                  href={link.to}
                  class="flex items-center justify-center hover:bg-mauve-100 rounded-full p-2"
                >
                  <link.icon height="1.8em" />
                </a>
              </li>
            {/each}
          </div>
        </ul>
      </div>
    </div>
  </nav>

  <main class="min-h-screen">
    <section class="ms-32">
      {@render children()}
    </section>
  </main>
</div>
