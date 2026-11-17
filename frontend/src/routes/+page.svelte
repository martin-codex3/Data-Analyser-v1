<script lang="ts">
  import StyledButton from "#lib/components/buttons/StyledButton.svelte";
  import TextInput from "#lib/components/inputs/TextInput.svelte";
  import { enhance } from "$app/forms";
  import { toast } from "svelte-sonner";
  import type { PageProps } from "./$types";
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

<div
  class="h-screen overflow-auto scrollbar-thin flex items-center justify-center px-5 lg:px-0"
>
  <div class="w-full max-w-5xl mx-auto grid grid-cols-1 lg:grid-cols-2">
    <!-- for the form here -->
    <div class="space-y-10">
      <div class="space-y-2">
        <h1 class="text-4xl lg:text-6xl font-extrabold first-letter:uppercase">
          welcome back
        </h1>
        <p class="text-xl">log in to access your account and all features.</p>
      </div>

      <div class="flex items-center gap-5">
        <div class="w-full border-b flex-1"></div>
        <div class="">
          <h1 class="first-letter:uppercase">continue with email</h1>
        </div>

        <div class="w-full border-b flex-1"></div>
      </div>

      <!-- for the form here -->
      <div>
        <form
          action="?/signIn"
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
                goto("/dashboard");
              }
            };
          }}
        >
          <div class="input__wrapper">
            <div class="space-y-7">
              <TextInput
                type="text"
                name="username"
                id="Email"
                placeholder="user@example.com"
                inputError={fieldErrors("#/username")?.detail}
                value=""
                label="Email"
              />

              <TextInput
                type="password"
                name="password"
                id="Password"
                placeholder=""
                inputError={fieldErrors("#/password")?.detail}
                value=""
                label="Password"
              />

              <StyledButton isLoading={isloggingIn} title="Log in" />
            </div>
          </div>
        </form>
      </div>

      <div class="flex items-center gap-2">
        <p>Don't have an accoun?</p>
        <a href="/create-account" class="underline text-lg underline-offset-4"
          >Create account</a
        >
      </div>
    </div>

    <!-- for the design here -->
    <div>
      <!-- for the header -->
      <div></div>
    </div>
  </div>
</div>
