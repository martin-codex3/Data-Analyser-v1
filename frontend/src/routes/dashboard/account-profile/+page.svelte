<script lang="ts">
  import ProfileDetails from "#lib/components/profile/ProfileDetails.svelte";
  import UpdateProfileDetails from "#lib/components/profile/UpdateProfileDetails.svelte";
  import type { PageProps } from "./$types";

  let toggleProfilePage: number = $state(1);

  const handleToggleProfilePage = (index: number) => {
    toggleProfilePage = index;
  };

  let { data }: PageProps = $props();
</script>

<section class="min-h-screen flex flex-col justify-center items-center">
  <div
    class="w-full max-w-3xl mx-auto bg-white h-[calc(100vh-1rem)] px-10 py-4 space-y-10 rounded-4xl border border-gray-300"
  >
    <!-- for the main header -->
    <div class="flex items-center border rounded-full px-2 py-1 w-fit gap-2">
      <button
        aria-label="Profile details"
        title="Profile Details"
        onclick={() => handleToggleProfilePage(1)}
        class={[
          "flex items-center justify-center rounded-full py-2 px-5 bg-gray-50 cursor-pointer w-52",
          toggleProfilePage === 1 ? "bg-primary-main-blue text-blue-50" : "",
        ]}
      >
        <span>Profile details</span>
      </button>

      <button
        aria-label="Update Profile Details"
        title="Update Profile Details"
        onclick={() => handleToggleProfilePage(2)}
        class={[
          "flex items-center justify-center py-2 px-5 w-52 cursor-pointer bg-gray-50 rounded-full",
          toggleProfilePage === 2 ? "bg-primary-main-blue text-blue-50" : "",
        ]}
      >
        <span>Edit profile details</span>
      </button>
    </div>

    <!-- for the main content  -->
    <div>
      {#if toggleProfilePage === 1}
        <ProfileDetails user={data.user} />
      {:else if toggleProfilePage === 2}
        <UpdateProfileDetails />
      {/if}
    </div>
  </div>
</section>
