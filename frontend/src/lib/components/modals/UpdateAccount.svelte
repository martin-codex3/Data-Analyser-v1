<script lang="ts">
  import CloseIcon from "@iconify-svelte/tabler/x";
  import TextInput from "../inputs/TextInput.svelte";
  import { enhance } from "$app/forms";
  import LoadingSVG from "@iconify-svelte/svg-spinners/180-ring";
  import { toast } from "svelte-sonner";
  import type { ActionData, PageProps } from "../../../routes/$types";

  let isUpdating: boolean = $state(false);
  let errorTitle: string = $state("");

  //   for the typing
  interface Props {
    fieldLabel: string;
    fieldValue: string;
    fieldName: string;
    form: ActionData;
    closeModal: () => void;
  }

  let { fieldLabel, closeModal, fieldValue, fieldName, form }: Props = $props();

  $effect(() => {
    if (form?.problem) {
      errorTitle = form.problem?.title;
    }
  });

  const handleCloseUpdateModal = () => {
    closeModal();
  };
</script>

<div
  class="fixed inset-0 z-10 backdrop-blur-sm bg-black/50 flex items-center justify-center"
>
  <div
    class="bg-white rounded-4xl px-10 py-5 w-full max-w-md h-fit motion-preset-slide-down-sm motion-duration-300"
  >
    <div class="space-y-5">
      <div class="flex items-center justify-between">
        <h1 class="capitalize text-2xl">update</h1>
        <button
          aria-label="close modal button"
          onclick={handleCloseUpdateModal}
          title="Close Modal"
          class="flex items-center cursor-pointer transition duration-200 justify-center p-2 rounded-full hover:bg-blue-50 hover:text-blue-900"
        >
          <CloseIcon height="1.3em" />
        </button>
      </div>

      <div>
        <p class="text-lg text-gray-500">
          Make changes to your profile here. Click save when you're done.
        </p>
      </div>

      <div class="">
        <form
          method="POST"
          use:enhance={() => {
            isUpdating = true;
            return async ({ update, result }) => {
              await update();
              isUpdating = false;

              if (result.type === "failure") {
                toast(errorTitle);
              }

              if (result.type === "error") {
                toast(errorTitle);
              }

              if (result.type === "success") {
                toast.success("Profile updated successfully");
                handleCloseUpdateModal();
              }
            };
          }}
        >
          <div class="space-y-5">
            <div>
              <TextInput
                type="text"
                id={fieldLabel}
                label={fieldLabel}
                value={fieldValue}
                placeholder=""
                errorValue=""
                name={fieldName}
              />
            </div>

            <div class="flex items-center justify-end">
              <div class="flex items-center gap-3">
                <button
                  aria-label="cancel button"
                  title="Cancel"
                  onclick={handleCloseUpdateModal}
                  class="flex items-center justify-center bg-blue-100 rounded-full px-5 py-2 text-primary-main-blue cursor-pointer"
                >
                  <span>Cancel</span>
                </button>

                <button
                  aria-label="save button"
                  title="Save"
                  formaction="account-profile?/editProfile"
                  class="flex items-center justify-center bg-primary-main-blue rounded-full px-5 py-2 text-blue-100 cursor-pointer"
                >
                  <span class="flex items-center gap-2">
                    Save
                    {#if isUpdating}
                      <LoadingSVG height="1.1em" />
                    {/if}
                  </span>
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
