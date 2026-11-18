<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";

    interface Props {
        name: string;
        value: string | undefined | boolean | object;
        label: string;
    }

    const { name, value, label }: Props = $props();
</script>

{#snippet modalBody()}
    <div>
        <form action="">
            <TextInput
                type="text"
                {name}
                id={label}
                placeholder=""
                inputError=""
                {value}
                {label}
            />
            <StyledButton isLoading={true} title="Update detail" />
        </form>
    </div>
{/snippet}

<div
    class="fixed inset-0 z-100 backdrop-blur-sm bg-black/20 flex items-center justify-center"
>
    <div
        class="w-full max-w-md rounded-4xl px-5 py-5 space-y-5 bg-primary-slight-black border border-orange-50/10"
    >
        <div class="space-y-2">
            <h1 class="text-xl font-semibold first-letter:capitalize">
                update profile
            </h1>
            <p class="text-gray-400">
                Make changes to your profile. The changes will reflect
                automatically when the action is successful
            </p>
        </div>

        <div>
            {@render modalBody()}
        </div>
    </div>
</div>
