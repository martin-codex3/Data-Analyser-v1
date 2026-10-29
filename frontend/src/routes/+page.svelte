<script lang="ts">
  import { enhance } from "$app/forms";
  import { getCountryDataList } from "countries-list";
  import LoadingSvg from "@iconify-svelte/svg-spinners/180-ring";
  import { toast } from "svelte-sonner";
  import type { PageProps } from "./$types";

  const countries = $derived(getCountryDataList());

  let isCreatingAccount: boolean = $state(false);

  let errorTitle: string = $state("");

  let { data, form }: PageProps = $props();

  $effect(() => {
    if (form?.problem) {
      errorTitle = form?.problem?.title;
    }
  });

  //   for the errors
  const fieldErrors = $derived((field: string) => {
    return form?.problem?.errors.find((e) => e.pointer === field);
  });
</script>

<section>
  <div
    class="main__wrapper min-h-screen overflow-auto scrollbar-thin w-full max-w-6xl mx-auto"
  >
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5">
      <div class="py-10 px-8 space-y-10">
        <div class="space-y-2">
          <h1 class="text-6xl font-bold first-letter:uppercase">
            lets's get started.
          </h1>
          <p class="text-gray-500 text-2xl first-letter:capitalize">
            setup your account to get access to all the features.
          </p>
        </div>

        <!-- for the form here  -->
        <div>
          <form
            method="POST"
            action="?/createAccount"
            use:enhance={() => {
              isCreatingAccount = true;
              return async ({ result, update }) => {
                await update();
                isCreatingAccount = false;

                if (result.type === "failure") {
                  toast.error(errorTitle);
                  return;
                }
              };
            }}
          >
            <div class="main__form__wrapper space-y-5">
              <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                <div class="">
                  <label for="FirstName">First name</label>
                  <input
                    type="text"
                    name="first_name"
                    id="FirstName"
                    placeholder="john"
                    class={[
                      "w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue",
                      fieldErrors("#/first_name")
                        ? "border-red-600 bg-red-50/50"
                        : "",
                    ]}
                  />
                  {#if fieldErrors("#/first_name")}
                    <span class="text-red-600 text-sm"
                      >{fieldErrors("#/first_name")?.detail}</span
                    >
                  {/if}
                </div>

                <div class="">
                  <label for="Lastname">Last name</label>
                  <input
                    type="text"
                    name="last_name"
                    placeholder="doe"
                    id="Lastname"
                    class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                  {#if fieldErrors("#/last_name")}
                    <span class="text-red-600 text-sm"
                      >{fieldErrors("#/last_name")?.detail}</span
                    >
                  {/if}
                </div>
              </div>

              <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                <div class="">
                  <label for="Email">Email</label>
                  <input
                    type="email"
                    name="email"
                    id="Email"
                    class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                  {#if fieldErrors("#/email")}
                    <span class="text-red-600 text-sm"
                      >{fieldErrors("#/email")?.detail}</span
                    >
                  {/if}
                </div>

                <div class="">
                  <label for="Address">Address</label>
                  <input
                    type="text"
                    name="address"
                    placeholder="Blantyre"
                    id="Address"
                    class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                  {#if fieldErrors("#/address")}
                    <span class="text-red-600 text-sm"
                      >{fieldErrors("#/address")?.detail}</span
                    >
                  {/if}
                </div>
              </div>

              <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                <div class="">
                  <label for="PhoneNumber">Phone number</label>
                  <input
                    type="text"
                    name="phone_number"
                    id="PhoneNumber"
                    class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                  {#if fieldErrors("#/phone_number")}
                    <span class="text-red-600 text-sm"
                      >{fieldErrors("#/phone_number")?.detail}</span
                    >
                  {/if}
                </div>

                <div class="">
                  <label for="Nationality">Nationality</label>
                  <select
                    name="nationality"
                    id="Nationality"
                    class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  >
                    {#each countries as country}
                      <option value={country.name}>{country.name}</option>
                    {/each}
                  </select>
                  {#if fieldErrors("#/nationality")}
                    <span class="text-red-600 text-sm"
                      >{fieldErrors("#/nationality")?.detail}</span
                    >
                  {/if}
                </div>
              </div>

              <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                <div class="">
                  <label for="BusinessName">Business name</label>
                  <input
                    type="text"
                    name="business_name"
                    id="BusinessName"
                    class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                  {#if fieldErrors("#/business_name")}
                    <span class="text-red-600 text-sm"
                      >{fieldErrors("#/business_name")?.detail}</span
                    >
                  {/if}
                </div>

                <div class="">
                  <label for="BusinessType">Business type</label>
                  <input
                    type="text"
                    name="business_type"
                    id="BusinessType"
                    class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                  {#if fieldErrors("#/business_type")}
                    <span class="text-red-600 text-sm"
                      >{fieldErrors("#/business_type")?.detail}</span
                    >
                  {/if}
                </div>
              </div>

              <div class="grid grid-cols-1 lg:grid-cols-1 gap-5">
                <div class="">
                  <label for="Password">Password</label>
                  <input
                    type="password"
                    name="password"
                    id="Password"
                    class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                  {#if fieldErrors("#/password_hash")}
                    <span class="text-red-600 text-sm"
                      >{fieldErrors("#/password_hash")?.detail}</span
                    >
                  {/if}
                </div>
              </div>

              <div>
                <button
                  aria-label="save-button"
                  title="Create Account"
                  class="flex items-center justify-center bg-primary-main-blue first-letter:capitalize rounded-full h-12 w-54 text-blue-100 cursor-pointer hover:shadow-xl transition duration-200"
                >
                  {#if isCreatingAccount}
                    <LoadingSvg height="1em" />
                  {:else}
                    <span class="capitalize">create account</span>
                  {/if}
                </button>
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
