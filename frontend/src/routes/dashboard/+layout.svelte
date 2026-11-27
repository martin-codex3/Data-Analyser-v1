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
    import ChevronRightIcon from "@iconify-svelte/tabler/chevron-right";

    import type { LayoutProps } from "./$types";
    import { page } from "$app/state";

    let { children, data }: LayoutProps = $props();

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
            to: "/dashboard/document-management",
            label: "Document management",
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

    const abbreviatedName = $derived((word: string) => {
        if (!word) {
            return;
        }
        let words = word.split(" ");

        return words
            .map((e) => e[0])
            .join("")
            .toUpperCase();
    });
</script>

<svelte:head>
    <title>Dashboard</title>
</svelte:head>

<nav
    class="fixed h-[calc(100vh)] w-90 overflow-hidden border-r border-r-gray-100/30 flex flex-col items-stretch space-y-5 py-3 px-3"
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
                        class={[
                            "flex items-center w-full gap-3 hover:bg-white hover:text-primary-main-black rounded-full py-2 px-2 transiion duration-200 first-letter:capitalize",
                            page.url.pathname === link.to
                                ? "bg-white text-black"
                                : "",
                        ]}
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
            href="/dashboard/account-profile"
            title="Profile"
            class="flex items-center border border-white rounded-full text-white px-2 py-1 w-full"
        >
            <div class="flex items-center justify-between w-full">
                <div class="flex items-center gap-2">
                    <div
                        class="h-10 w-10 rounded-full bg-primary-main-orange text-orange-950 flex items-center justify-center"
                    >
                        <h1>
                            {abbreviatedName(
                                `${data.user.first_name} ${data.user.last_name}`,
                            )}
                        </h1>
                    </div>

                    <div class="space-y-px">
                        <h1 class="font-semibold capitalize">
                            {data.user.first_name}
                        </h1>
                        <p class="first-letter:capitalize">get full details</p>
                    </div>
                </div>

                <div>
                    <ChevronRightIcon height="1.5em" />
                </div>
            </div>
        </a>
    </div>
</nav>

<main class="ms-90 px-5">
    <section>
        {@render children()}
    </section>
</main>
