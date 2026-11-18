<script lang="ts">
    import type { PageProps } from "./$types";

    const { data }: PageProps = $props();

    interface Props {
        title: string;
        description: string;
        icon: any;
        value: string | undefined;
    }

    const profileData: Props[] = $derived([
        {
            title: "First Name",
            description: "The name for the account",
            icon: "",
            value: data.user.first_name,
        },
    ]);
</script>

<div class="h-screen flex items-center justify-center overflow-hidden">
    <div
        class="bg-primary-slight-black w-full max-w-4xl px-10 py-5 rounded-4xl h-[calc(100vh-2rem)]"
    >
        <div class="h-full overflow-auto scrollbar-thin">
            <!-- for the main header -->
            <div class="flex items-center gap-5">
                <div class="rounded-full border h-20 w-20"></div>
                <div>
                    <h1 class="capitalize text-lg font-semibold">
                        {data.user.first_name}
                    </h1>
                    <p>{data.user.email}</p>
                </div>
            </div>
        </div>
    </div>
</div>
