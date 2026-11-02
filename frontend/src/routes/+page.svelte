<script lang="ts">
  import StyledButton from "#lib/components/buttons/StyledButton.svelte";
  import TextInput from "#lib/components/inputs/TextInput.svelte";
  import { enhance } from "$app/forms";
  import { goto } from "$app/navigation";
  import { toast } from "svelte-sonner";

  let isSigningin: boolean = $state(false);
</script>

<svelte:head>
  <title>Login</title>
</svelte:head>

<section>
  <div
    class="main__wrapper min-h-screen overflow-auto scrollbar-thin w-full max-w-6xl mx-auto"
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
            action="?/createAccount"
            use:enhance={() => {
              isSigningin = true;
              return async ({ result, update }) => {
                await update();
                isSigningin = false;

                if (result.type === "failure") {
                  toast.error("Hey mate");
                  return;
                }

                if (result.type === "success") {
                  toast.success("Account created successfully");
                  await goto("/dashboard");
                }
              };
            }}
          >
            <div class="main__form__wrapper space-y-7">
              <TextInput
                type="email"
                name="email"
                label="Email"
                id="Email"
                placeholder="example@gmail.com"
              ></TextInput>

              <TextInput
                type="password"
                name="password_hash"
                label="Password"
                id="Password"
                placeholder=""
              ></TextInput>
              <div>
                <StyledButton
                  isLoading={isSigningin}
                  label="Login"
                  title="Log in"
                />
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
