<script lang="ts">
  import type { User } from "#lib/types/users/user.ts";
  import CameraIcon from "@iconify-svelte/tabler/camera";
  import NameIcon from "@iconify-svelte/tabler/user";
  import PencilIcon from "@iconify-svelte/tabler/pencil";
  import PhoneIcon from "@iconify-svelte/tabler/phone";
  import EmailIcon from "@iconify-svelte/tabler/message";
  import MessageIcon from "@iconify-svelte/tabler/message";
  import ConfirmIcon from "@iconify-svelte/tabler/exclamation-circle";
  import BioIcon from "@iconify-svelte/tabler/file";
  import TimeIcon from "@iconify-svelte/tabler/calendar-time";
  import UsernameIcon from "@iconify-svelte/tabler/user-star";
  import UpdateAccount from "../modals/UpdateAccount.svelte";
  import type { ActionData } from "../../../routes/$types";
  import { format } from "date-fns";
  import { enhance } from "$app/forms";
  import { toast } from "svelte-sonner";
  import LoadingSVG from "@iconify-svelte/svg-spinners/180-ring";
  import LockIcon from "@iconify-svelte/tabler/key";

  let { user, form }: { user: User; form: ActionData } = $props();
  let openUpdateModal: boolean = $state(false);
  let isLoggingOut: boolean = $state(false);

  let fieldValue: string = $state("");
  let fieldLabel: string = $state("");
  let fieldName: string = $state("");

  const handleOpenUpdateModal = async (
    value: string,
    label: string,
    name: string,
  ) => {
    if (value != null) {
      fieldValue = value;
      fieldLabel = label;
      fieldName = name;
      openUpdateModal = true;
    }
  };

  const handleCloseUpdateModal = async () => {
    openUpdateModal = false;
  };

  let isEmailVerified = $derived((value: boolean) => {
    return value
      ? "bg-green-500 text-green-900 rounded-full px-3 py-1 text-sm"
      : "bg-orange-300 text-orange-900 rounded-full px-3 py-1 text-sm";
  });
</script>

<div>
  <div class="motion-preset-slide-down-sm motion-duration-200">
    <div class="space-y-10">
      <div class="flex items-center gap-3">
        <div class="relative">
          <div class="h-18 w-18 rounded-full bg-blue-100">
            <img src="lib/assets/images/profile.jpg" alt="" />
          </div>
          <div class="absolute bottom-0 right-0">
            <button
              aria-label="update-profile-button"
              class="flex items-center justify-center bg-primary-main-blue p-2 rounded-full border cursor-pointer text-blue-100"
            >
              <CameraIcon height="1.2em" class="shrink-0" />
            </button>
          </div>
        </div>
        <div>
          <h1>{user.first_name}</h1>
          <p>{user.account_created_at}</p>
        </div>
      </div>

      <!-- for the other content here -->
      <div class="space-y-1">
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-tr-3xl rounded-tl-3xl rounded-bl-lg rounded-br-lg"
        >
          <div class="flex items-center gap-2">
            <NameIcon height="1.5em" class="shrink-0" />
            <h1 class="first-letter:uppercase">first name</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2>{user.first_name ?? "Not set"}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              onclick={() =>
                handleOpenUpdateModal(
                  user.first_name,
                  "First name",
                  "first_name",
                )}
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <NameIcon height="1.5em" class="shrink-0" />
            <h1 class="first-letter:uppercase">last name</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.last_name ?? "Not set"}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              onclick={() =>
                handleOpenUpdateModal(user.last_name, "Last name", "last_name")}
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- for the phone number -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <PhoneIcon height="1.5em" class="shrink-0" />
            <h1 class="first-letter:uppercase">phone number</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.phone_number ?? "Not set"}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              onclick={() =>
                handleOpenUpdateModal(
                  user.phone_number,
                  "Phone number",
                  "phone_number",
                )}
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- for the username -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <UsernameIcon height="1.5em" class="shrink-0" />
            <h1 class="first-letter:uppercase">username</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.username ?? "Not set"}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              onclick={() =>
                handleOpenUpdateModal(
                  user.username ?? "",
                  "Username",
                  "username",
                )}
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- for the email -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <EmailIcon height="1.5em" class="shrink-0" />
            <h1 class="first-letter:uppercase">email</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.email ?? "Not set"}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              onclick={() =>
                handleOpenUpdateModal(user.email, "Email", "email")}
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- if the email confirmed -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <ConfirmIcon height="1.5em" class="shrink-0" />
            <h1 class="first-letter:uppercase">is email confirmed</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class={isEmailVerified(user.is_email_verified)}>
              {user.is_email_verified ? "Verified" : "Not verified"}
            </h2>
          </div>
        </div>

        <!-- email confirmed at -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <TimeIcon height="1.5em" class="shrink-0" />
            <h1 class="first-letter:uppercase">account created at</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{format(user.account_created_at, "dd/MM/yyyy")}</h2>
          </div>
        </div>

        <!-- for the bio -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-lg"
        >
          <div class="flex items-center gap-2">
            <BioIcon height="1.5em" class="shrink-0" />
            <h1 class="first-letter:uppercase">bio</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">{user.bio?.slice(0, 30) ?? "Not set"}</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              onclick={() =>
                handleOpenUpdateModal(user.bio ?? "Not set", "Bio", "bio")}
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>

        <!-- for udpdating the password -->
        <div
          class="flex items-center justify-between bg-mauve-50 px-5 py-3 rounded-br-3xl rounded-bl-3xl rounded-tr-lg rounded-tl-lg"
        >
          <div class="flex items-center gap-2">
            <LockIcon height="1.5em" class="shrink-0" />
            <h1 class="first-letter:uppercase">Password</h1>
          </div>

          <div class="flex items-center gap-5">
            <h2 class="">Update password</h2>
            <button
              aria-label="Update details button"
              title="Update Name"
              onclick={() =>
                handleOpenUpdateModal(user.bio ?? "Not set", "Bio", "bio")}
              class="flex items-center justify-center rounded-full p-2 hover:bg-blue-50 hover:text-blue-900 transition-all duration-300 cursor-pointer"
            >
              <PencilIcon height="1.4em" class="shrink-0" />
            </button>
          </div>
        </div>
      </div>

      <!-- for updating the password -->
      <div class="border rounded-4xl px-5 py-4 border-gray-300 space-y-5">
        <h1 class="text-xl capitalize">log out</h1>
        <div>
          <form
            method="POST"
            action="?/logoutUser"
            use:enhance={() => {
              isLoggingOut = true;
              return async ({ update, result }) => {
                await update();
                isLoggingOut = false;
                if (result.type === "failure") {
                  toast.error("Something went wrong.");
                }

                if (result.type === "success") {
                  toast.success("Logged out successfully");
                }
              };
            }}
          >
            <button
              aria-label="Account logout button"
              title="Log out"
              class="flex items-center justify-center rounded-full w-44 px-10 py-2 cursor-pointer bg-blue-200/50 text-primary-main-blue"
            >
              {#if isLoggingOut}
                <div class="flex items-center gap-3">
                  <span>Processing</span>
                  <LoadingSVG height="1.3em" />
                </div>
              {:else}
                <span>Log out</span>
              {/if}
            </button>
          </form>
        </div>
      </div>

      <!-- for removing the account here -->
      <div class="border rounded-4xl px-5 py-4 border-gray-300 space-y-5">
        <h1 class="text-xl capitalize">delete account</h1>
        <p>
          Once you delete you're account you will not be able to recover it. All
          the work relating to your account will also get deleted.
        </p>

        <button
          aria-label="delete-button"
          title="Delete Account"
          class="flex items-center justify-center rounded-full px-10 py-2 cursor-pointer bg-red-200/50 text-red-800"
        >
          <span>Delete</span>
        </button>
      </div>
    </div>
  </div>

  <!-- for the modal here -->
  <div>
    {#if openUpdateModal}
      <UpdateAccount
        closeModal={handleCloseUpdateModal}
        {fieldValue}
        {fieldLabel}
        {fieldName}
        {form}
      />
    {/if}
  </div>
</div>
