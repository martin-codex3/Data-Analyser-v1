<script lang="ts">
    import LayoutDashboardIcon from "@iconify-svelte/tabler/layout-dashboard";
    import FolderKanbanIcon from "@iconify-svelte/tabler/folder";
    import FolderIcon from "@iconify-svelte/tabler/folder";
    import DatabaseIcon from "@iconify-svelte/tabler/database";
    import ChartBarIcon from "@iconify-svelte/tabler/chart-bar";
    import RobotIcon from "@iconify-svelte/tabler/robot";
    import FileReportIcon from "@iconify-svelte/tabler/file-report";
    import UsersIcon from "@iconify-svelte/tabler/users";
    import MessageCircleIcon from "@iconify-svelte/tabler/message-circle";
    import CpuIcon from "@iconify-svelte/tabler/cpu";
    import SettingsIcon from "@iconify-svelte/tabler/settings";
    import ShieldCheckIcon from "@iconify-svelte/tabler/shield-check";

    let { children } = $props();

    interface Props {
        to: string;
        label: string;
        icon: any;
    }

    const mainLinks: Props[] = $state([
        {
            to: "/dashboard",
            label: "Dashboard",
            icon: LayoutDashboardIcon,
        },
        {
            to: "/dashboard/workspaces-document-management",
            label: "document management",
            icon: FolderKanbanIcon,
        },
        {
            to: "/dashboard/projects",
            label: "Projects & folders",
            icon: FolderIcon,
        },
        {
            to: "/dashboard/datasets",
            label: "Datasets",
            icon: DatabaseIcon,
        },
        {
            to: "/dashboard/analyses",
            label: "Analyses",
            icon: ChartBarIcon,
        },
        {
            to: "/dashboard/assistance",
            label: "AI assistance",
            icon: RobotIcon,
        },
        {
            to: "/dashboard/reports",
            label: "Reports",
            icon: FileReportIcon,
        },
        {
            to: "/dashboard/team-members",
            label: "Team members",
            icon: UsersIcon,
        },
        {
            to: "/dashboard/comments-activity",
            label: "Comments and activity",
            icon: MessageCircleIcon,
        },
        {
            to: "/dashboard/processing-jobs",
            label: "Processing jobs",
            icon: CpuIcon,
        },
        {
            to: "/dashboard/workspace-settings",
            label: "Workspace settings",
            icon: SettingsIcon,
        },
        {
            to: "/dashboard/security",
            label: "Security & audit logs",
            icon: ShieldCheckIcon,
        },
    ]);
</script>

<svelte:head>
    <title>Dashboard</title>
</svelte:head>

<nav
    class="fixed h-[calc(100vh)] w-90 overflow-hidden flex flex-col items-stretch space-y-5 py-3 px-3"
>
    <div class="main__app__logo px-5">
        <h1>site logo</h1>
    </div>

    <!-- for the app links -->
    <div class="h-full overflow-auto scrollbar-thin px-3">
        <ul class="space-y-3">
            {#each mainLinks as link}
                <li class="w-full">
                    <a
                        href={link.to}
                        title={link.label}
                        class="flex items-center w-full gap-3 hover:bg-orange-50 hover:text-orange-950 rounded-full py-2 px-2 transiion duration-200"
                    >
                        <link.icon height="1.5em" class="shrink-0" />
                        <span>{link.label}</span>
                    </a>
                </li>
            {/each}
        </ul>
    </div>

    <!-- for the profile page -->
    <div>
        <a
            href="/dashboard/profile"
            title="Profile"
            class="flex items-center bg-orange-50 rounded-3xl text-orange-950 px-5 py-5"
        >
            <div class="flex items-center">
                <div
                    class="h-10 w-10 rounded-full bg-primary-main-orange/50 flex items-center justify-center"
                >
                    <h1>MS</h1>
                </div>
            </div>
        </a>
    </div>
</nav>

<main class="ms-80">
    <section>
        {@render children()}
    </section>
</main>
