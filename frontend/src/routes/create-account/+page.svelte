<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import { toast } from "svelte-sonner";
    import type { PageProps } from "../$types";
    import SelectInput from "#lib/components/inputs/SelectInput.svelte";
    import BackIcon from "@iconify-svelte/tabler/arrow-left";
    import { goto } from "$app/navigation";

    let isloggingIn: boolean = $state(false);

    const { form }: PageProps = $props();
    let errorTitle: string = $state("");

    $effect(() => {
        if (form?.problem?.title) {
            errorTitle = form?.problem?.title;
        }

        if (form?.problem?.detail) {
            errorTitle = form?.problem?.detail;
        }
    });

    const fieldErrors = $derived((field: string) => {
        return form?.problem?.errors?.find((e) => field === e.pointer);
    });

    $inspect(fieldErrors("#/username"));
</script>

<div class="px-5 lg:px-0 py-10">
    <div class="w-full max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2">
        <!-- for the form here -->
        <div class="space-y-10">
            <div>
                <button
                    aria-label="Go back buton"
                    title="Go back"
                    onclick={() => goto("/")}
                    class="flex items-center justify-center border rounded-full p-3 cursor-pointer"
                >
                    <BackIcon height="1.5em" />
                </button>
            </div>

            <div class="space-y-2">
                <h1
                    class="text-4xl lg:text-6xl font-extrabold first-letter:uppercase"
                >
                    create account
                </h1>
                <p class="text-xl first-letter:capitalize">
                    create an account to access all the features
                </p>
            </div>

            <!-- for the form here -->
            <div>
                <form
                    action="?/createAccount"
                    method="POST"
                    use:enhance={() => {
                        isloggingIn = true;
                        return async ({ result, update }) => {
                            await update();
                            isloggingIn = false;

                            if (result.type === "failure") {
                                toast.error(errorTitle);
                            }

                            if (result.type === "error") {
                                toast.error(errorTitle);
                            }

                            if (result.type === "success") {
                                toast.success("Logged in successfully");
                            }
                        };
                    }}
                >
                    <div class="input__wrapper">
                        <div class="space-y-7">
                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                                <TextInput
                                    type="text"
                                    name="first_name"
                                    id="FirstName"
                                    placeholder="John"
                                    inputError={fieldErrors("#/first_name")
                                        ?.detail}
                                    value=""
                                    label="First name"
                                />

                                <TextInput
                                    type="text"
                                    name="last_name"
                                    id="LastName"
                                    placeholder="Doe"
                                    inputError={fieldErrors("#/last_name")
                                        ?.detail}
                                    value=""
                                    label="Last name"
                                />
                            </div>

                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                                <TextInput
                                    type="text"
                                    name="phone_number"
                                    id="PhoneNumber"
                                    placeholder=""
                                    inputError={fieldErrors("#/phone_number")
                                        ?.detail}
                                    value=""
                                    label="Phone number"
                                />

                                <TextInput
                                    type="email"
                                    name="email"
                                    id="Email"
                                    placeholder="user@example.com"
                                    inputError={fieldErrors("#/email")?.detail}
                                    value=""
                                    label="Email"
                                />
                            </div>

                            <div class="grid grid-cols-1 lg:grid-cols-1">
                                <TextInput
                                    type="text"
                                    name="address_line_1"
                                    id="Address"
                                    placeholder=""
                                    inputError={fieldErrors("#/address_line_1")
                                        ?.detail}
                                    value=""
                                    label="Address"
                                />
                            </div>

                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                                <TextInput
                                    type="text"
                                    name="business_name"
                                    id="BusinessName"
                                    placeholder=""
                                    inputError={fieldErrors("#/business_name")
                                        ?.detail}
                                    value=""
                                    label="Business name"
                                />

                                <SelectInput
                                    name="business_type"
                                    id="BusinessType"
                                    placeholder=""
                                    inputError={fieldErrors("#/business_type")
                                        ?.detail}
                                    value=""
                                    label="Business type"
                                >
                                    <option value="">Select option</option>
                                    <option value="Private">Private</option>
                                    <option value="Health">Health</option>
                                    <option value="Education">Education</option>
                                    <option value="Agriculture"
                                        >Agriculture</option
                                    >
                                    <option value="Other">Other</option>
                                </SelectInput>
                            </div>

                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                                <TextInput
                                    type="email"
                                    name="business_email"
                                    id="BusinessEmail"
                                    placeholder=""
                                    inputError={fieldErrors("#/business_email")
                                        ?.detail}
                                    value=""
                                    label="Business email"
                                />

                                <TextInput
                                    type="text"
                                    name="business_phone"
                                    id="BusinessPhone"
                                    placeholder=""
                                    inputError={fieldErrors("#/business_phone")
                                        ?.detail}
                                    value=""
                                    label="Business phone"
                                />
                            </div>

                            <div class="grid grid-cols-1 lg:grid-cols-1 gap-5">
                                <TextInput
                                    type="password"
                                    name="password_hash"
                                    id="Password"
                                    placeholder=""
                                    inputError={fieldErrors("#/password_hash")
                                        ?.detail}
                                    value=""
                                    label="Password"
                                />
                            </div>

                            <StyledButton
                                isLoading={isloggingIn}
                                title="Create account"
                            />
                        </div>
                    </div>
                </form>
            </div>
        </div>

        <!-- for the design here -->
        <div>
            <!-- for the header -->
            <div></div>
        </div>
    </div>
</div>
