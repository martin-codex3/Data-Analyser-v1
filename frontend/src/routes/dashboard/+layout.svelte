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

<div class="main__content__wrapper bg-gray-100 px-5">
  <nav
    class="main__navigation fixed h-[calc(100vh-1rem)] w-32 top-1/2 -translate-y-1/2 rounded-3xl bg-white border px-7 py-5 border-gray-300"
  >
    <div class="">
      <ul class="space-y-5">
        <div class="space-y-2">
          {#each overviewLinks as link}
            <li class="">
              <a
                href={link.to}
                title={link.label}
                class={[
                  "flex items-center justify-center hover:bg-blue-100 hover:text-blue-800 rounded-full p-2",
                  page.url.pathname === link.to
                    ? "bg-primary-main-blue text-blue-100"
                    : "",
                ]}
              >
                <link.icon height="1.8em" />
              </a>
            </li>
          {/each}
        </div>

        <!-- for the collaborations here -->
        <div class="space-y-2">
          {#each collaborationLinks as link}
            <li>
              <a
                href={link.to}
                title={link.label}
                class={[
                  "flex items-center justify-center hover:bg-blue-100 hover:text-blue-800 rounded-full p-2",
                  page.url.pathname === link.to
                    ? "bg-primary-main-blue text-blue-100"
                    : "",
                ]}
              >
                <link.icon height="1.8em" />
              </a>
            </li>
          {/each}
        </div>

        <!-- for the workspace management -->
        <div class="space-y-2">
          {#each administrationLinks as link}
            <li>
              <a
                href={link.to}
                title={link.label}
                class={[
                  "flex items-center justify-center hover:bg-blue-100 hover:text-blue-800 rounded-full p-2",
                  page.url.pathname === link.to
                    ? "bg-primary-main-blue text-blue-100"
                    : "",
                ]}
              >
                <link.icon height="1.5em" />
              </a>
            </li>
          {/each}
        </div>

        <div
          class="absolute bottom-5 flex items-center justify-center left-0 right-0"
        >
          <button
            aria-label="profile-image-button"
            title="ProfileImage"
            class="bg-blue-100 border border-primary-main-blue rounded-full p-7"
          ></button>
        </div>
      </ul>
    </div>
  </nav>

  <main class="min-h-screen">
    <section class="ms-33">
      {@render children()}
    </section>
  </main>
</div>
