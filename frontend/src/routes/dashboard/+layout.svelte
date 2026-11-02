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
      to: "/dashboard/workspace-settings",
      icon: SettingsIcon,
    },

    {
      label: "User management",
      to: "dashboard/audit-logs",
      icon: SecurityIcon,
    },
  ];
</script>

<div class="main__content__wrapper">
  <nav
    class="main__navigation fixed h-[calc(100vh)] w-80 bg-white border-r px-3 py-5 border-gray-300 overflow-auto scrollbar-thin"
  >
    <div class="space-y-7">
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

      <!-- for the organisation settings -->
    </div>

    <!-- for the profile image and settings -->
    <div class="absolute bottom-3 right-3 left-3">
      <a
        href="/dashboard/account-profile"
        title="User profile"
        class={[
          "flex w-full rounded-full px-2 py-1 border border-gray-200 hover:bg-blue-50 transition duration-300 items-center gap-2",
          page.url.pathname === "/dashboard/account-profile"
            ? "bg-blue-50 text-blue-900"
            : "",
        ]}
      >
        <div
          class="bg-primary-main-blue h-9 w-9 rounded-full flex items-center justify-center"
        ></div>

        <div>
          <h1 class="text-sm">Martin Silungwe</h1>
          <p class="text-sm">active</p>
        </div>
      </a>
    </div>
  </nav>

  <main class="min-h-screen">
    <section class="ms-80">
      {@render children()}
    </section>
  </main>
</div>
