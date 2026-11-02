<script lang="ts">
  import StyledButton from "#lib/components/buttons/StyledButton.svelte";
  import TextInput from "#lib/components/inputs/TextInput.svelte";
  import { enhance } from "$app/forms";
  import { goto } from "$app/navigation";
  import { toast } from "svelte-sonner";
  import type { PageProps } from "./$types";
  import { derived } from "svelte/store";
  import { error } from "@sveltejs/kit";

  let isSigningin: boolean = $state(false);

  let { form }: PageProps = $props();
  let errorTitle: string = $state("");

  $effect(() => {
    if (form?.problem) {
      errorTitle = form?.problem?.title;
    }

    if (form?.problem?.detail) {
      errorTitle = form?.problem?.title;
    }
  });

  let fieldError = $derived((field: string) => {
    return form?.problem?.errors?.find((e) => e.pointer === field);
  });
</script>

<svelte:head>
  <title>Login</title>
</svelte:head>

<section>
  <div
    class="main__wrapper min-h-screen overflow-auto scrollbar-thin w-full max-w-5xl mx-auto"
  >
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5">
      <div class="py-10 px-8 space-y-10">
        <div class="space-y-2">
          <h1 class="text-6xl font-bold first-letter:uppercase">
            welcome back.
          </h1>
          <p class="text-gray-500 text-2xl first-letter:capitalize">
            log in to your account
          </p>
        </div>

        <div class="flex items-center gap-5">
          <div class="border-b w-full border-b-gray-300 flex-1"></div>
          <div>
            <h1 class="first-letter:uppercase">continue with email</h1>
          </div>
          <div class="border-b w-full border-b-gray-300 flex-1"></div>
        </div>

        <!-- for the form here  -->
        <div>
          <form
            method="POST"
            action="?/signIn"
            use:enhance={() => {
              isSigningin = true;
              return async ({ result, update }) => {
                await update();
                isSigningin = false;

                if (result.type === "failure") {
                  toast.error(errorTitle);
                  return;
                }

                if (result.type === "success") {
                  toast.success("Account created successfully");
                }
              };
            }}
          >
            <div class="main__form__wrapper space-y-7">
              <TextInput
                type="email"
                name="username"
                label="Email"
                id="Email"
                placeholder="example@gmail.com"
                errorValue={fieldError("#/username")?.detail}
              />

              <TextInput
                type="password"
                name="password_hash"
                label="Password"
                id="Password"
                placeholder=""
                errorValue={fieldError("#/password_hash")?.detail}
              />
              <div>
                <StyledButton
                  isLoading={isSigningin}
                  label="Login"
                  title="Log in"
                />
              </div>

              <div class="flex items-center justify-center gap-2">
                <p class="first-letter:uppercase">don't have an account?</p>
                <a
                  href="/accounts"
                  class="underline text-lg capitalize hover:text-primary-main-blue transition duration-300"
                  >create account.</a
                >
              </div>
            </div>
          </form>
        </div>
      </div>

      <!-- for the design here -->
      <div class=""></div>
    </div>
  </div>
</section>
