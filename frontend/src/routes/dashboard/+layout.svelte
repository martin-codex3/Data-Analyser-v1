<script lang="ts">
  import { page } from "$app/state";
  import OverviewIcon from "@iconify-svelte/tabler/dashboard";
  import DocumentsIcon from "@iconify-svelte/tabler/file";
  import DataSetIcon from "@iconify-svelte/tabler/database";
  import GroupIcon from "@iconify-svelte/tabler/users-group";
  import ChatIcon from "@iconify-svelte/tabler/message";
  import ProcessingIcon from "@iconify-svelte/tabler/filter";
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
    { label: "Datasets", to: "/dashboard/datasets", icon: DataSetIcon },
  ];

  //   for the collaborations
  let collaborationLinks: any[] = [
    { label: "Team Members", to: "/dashboard/team-members", icon: GroupIcon },
    {
      label: "Comments & Activity",
      to: "/dashboard/comments-and-activity",
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
      to: "/dashboard/workspace-settings",
      icon: SettingsIcon,
    },

    {
      label: "Security & Audit Logs",
      to: "dashboard/audit-logs",
      icon: SecurityIcon,
    },
  ];
</script>

<div class="main__content__wrapper bg-gray-100">
  <nav
    class="main__navigation fixed h-[calc(100vh)] w-80 top-1/2 -translate-y-1/2 bg-white border-r px-5 py-5 border-gray-300"
  >
    <div class="">
      <!-- for the documents -->
      <div>
        <ul class="space-y-1">
          {#each overviewLinks as link}
            <li>
              <a
                href={link.to}
                title={link.label}
                class="flex items-center gap-3 hover:bg-blue-50 hover:text-blue-900 rounded-full px-3 py-2"
              >
                <link.icon height="1.7em" class="shrink-0" />
                <span>{link.label}</span>
              </a>
            </li>
          {/each}
        </ul>
      </div>
    </div>
  </nav>

  <main class="min-h-screen">
    <section class="ms-33">
      {@render children()}
    </section>
  </main>
</div>
