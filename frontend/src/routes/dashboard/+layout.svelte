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
            label: "Workspace & document management",
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

<nav class="h-[calc(100vh)] w-80 overflow-hidden flex flex-col items-start">
    <div class="main__app__logo">
        <h1>site logo</h1>
    </div>

    <!-- for the app links -->
    <div class="h-full overflow-auto scrollbar-thin">
        <ul>
            {#each mainLinks as link}
                <li>
                    <a
                        href={link.to}
                        title={link.label}
                        class="flex items-center gap-3"
                    >
                        <link.icon height="1.5em" class="shrink-0" />
                        <span>{link.label}</span>
                    </a>
                </li>
            {/each}
        </ul>
    </div>
</nav>
