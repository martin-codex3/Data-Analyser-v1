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

  let organisationSettings: any[] = [
    {
      label: "Organisation Settings",
      to: "/dashboard/",
      icon: SettingsIcon,
    },

    {
      label: "User management",
      to: "dashboard/user-management",
      icon: SecurityIcon,
    },
  ];
</script>

<div class="main__content__wrapper">
  <nav
    class="main__navigation fixed h-[calc(100vh)] w-80 bg-white border-r px-3 py-5 border-gray-300 overflow-hidden"
  >
    <div>
      <h1>logo</h1>
    </div>

    <!-- for the site links -->
    <div
      class="space-y-7 h-full overflow-auto scrollbar-thin scrollbar-gutter-stable scrollbar-thumb-gray-400 py-10"
    >
      <!-- for the documents -->
      <div class="space-y-2">
        <h1 class="capitalize text-gray-500">general</h1>
        <ul class="space-y-1">
          {#each overviewLinks as link}
            <li>
              <a
                href={link.to}
                title={link.label}
                class={[
                  "flex items-center gap-3 hover:bg-blue-50 hover:text-blue-900 rounded-full px-3 py-2",
                  page.url.pathname === link.to
                    ? "bg-blue-50 text-blue-900"
                    : "",
                ]}
              >
                <link.icon height="1.7em" class="shrink-0" />
                <span>{link.label}</span>
              </a>
            </li>
          {/each}
        </ul>
      </div>

      <!-- for the collaborations -->
      <div class="space-y-2">
        <h1 class="capitalize text-gray-500">collaborations</h1>
        <ul class="space-y-1">
          {#each collaborationLinks as link}
            <li>
              <a
                href={link.to}
                title={link.label}
                class={[
                  "flex items-center gap-3 hover:bg-blue-50 hover:text-blue-900 rounded-full px-3 py-2",
                  page.url.pathname === link.to
                    ? "bg-blue-50 text-blue-900"
                    : "",
                ]}
              >
                <link.icon height="1.7em" class="shrink-0" />
                <span>{link.label}</span>
              </a>
            </li>
          {/each}
        </ul>
      </div>

      <!-- for the administration links -->
      <div class="space-y-2">
        <h1 class="capitalize text-gray-500">organisation</h1>
        <ul class="space-y-1">
          {#each organisationSettings as link}
            <li>
              <a
                href={link.to}
                title={link.label}
                class={[
                  "flex items-center gap-3 hover:bg-blue-50 hover:text-blue-900 rounded-full px-3 py-2",
                  page.url.pathname === link.to
                    ? "bg-blue-50 text-blue-900"
                    : "",
                ]}
              >
                <link.icon height="1.7em" class="shrink-0" />
                <span>{link.label}</span>
              </a>
            </li>
          {/each}
        </ul>
      </div>

      <!-- for the organisation settings -->
      <div class="space-y-2">
        <h1 class="capitalize text-gray-500">settings</h1>
        <ul class="space-y-1">
          {#each administrationLinks as link}
            <li>
              <a
                href={link.to}
                title={link.label}
                class={[
                  "flex items-center gap-3 hover:bg-blue-50 hover:text-blue-900 rounded-full px-3 py-2",
                  page.url.pathname === link.to
                    ? "bg-blue-50 text-blue-900"
                    : "",
                ]}
              >
                <link.icon height="1.7em" class="shrink-0" />
                <span>{link.label}</span>
              </a>
            </li>
          {/each}
        </ul>
      </div>
    </div>

    <div class="bg-blue-500 fixed bottom-0 w-full">
      <h1>hey</h1>
    </div>
  </nav>

  <main class="min-h-screen">
    <section class="ms-80">
      {@render children()}
    </section>
  </main>
</div>
