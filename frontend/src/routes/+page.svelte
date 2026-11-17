<script lang="ts">
  import TextInput from "#lib/components/inputs/TextInput.svelte";
</script>

<div
  class="h-screen overflow-auto scrollbar-thin flex items-center justify-center"
>
  <div class="w-full max-w-5xl mx-auto grid grid-cols-1 lg:grid-cols-2">
    <!-- for the form here -->
    <div class="">
      <div>
        <h1 class="text-3xl lg:text-6xl font-extrabold first-letter:uppercase">
          welcome back
        </h1>
        <p class="text-xl">log in to access your account and all features.</p>
      </div>

      <!-- for the form here -->
      <div>
        <form action="" method="POST">
          <div class="input__wrapper">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
              <TextInput />
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
