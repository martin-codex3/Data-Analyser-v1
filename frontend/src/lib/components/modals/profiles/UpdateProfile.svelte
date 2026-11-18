<script lang="ts">
    import TextInput from "#lib/components/inputs/TextInput.svelte";

    interface Props {
        type: string;
        name: string;
        id: string;
        placeholder: string;
        inputError: string;
        value: String;
        label: string;
    }

    const { type, name, id, placeholder, inputError, value, label } = $props();
</script>

{#snippet modalBody()}
    <div>
        <TextInput
            {type}
            {name}
            {id}
            {placeholder}
            {inputError}
            {value}
            {label}
        />
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
            <p class="text-gray-500">
                Make changes to your profile. The changes will reflect
                automatically when the action is successful
            </p>
        </div>

        <div>
            <h1>for the main content</h1>
        </div>
    </div>
</div>
