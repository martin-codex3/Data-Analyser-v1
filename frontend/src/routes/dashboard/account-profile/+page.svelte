<script lang="ts">
  let toggleProfilePage: number = $state(1);

  const handleToggleProfilePage = (index: number) => {
    toggleProfilePage = index;
  };
</script>

<section class="min-h-screen flex flex-col justify-center items-center">
  <div
    class="w-full max-w-3xl mx-auto bg-white h-[calc(100vh-1rem)] px-5 py-4 rounded-4xl border border-gray-300"
  >
    <!-- for the main header -->
    <div class="flex items-center">
      <button
        aria-label="Profile details"
        title="Profile Details"
        onclick={() => handleToggleProfilePage(1)}
        class={[
          "flex items-center justify-center border border-gray-300 py-2 px-5 rounded-tl-full rounded-bl-full cursor-pointer",
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
          "flex items-center justify-center py-2 px-5 rounded-tr-full border border-gray-300 rounded-br-full cursor-pointer",
          toggleProfilePage === 2 ? "bg-primary-main-blue text-blue-50" : "",
        ]}
      >
        <span>Edit profile details</span>
      </button>
    </div>
  </div>
</section>
