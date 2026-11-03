<script lang="ts">
  import CloseIcon from "@iconify-svelte/tabler/x";
  import TextInput from "../inputs/TextInput.svelte";

  //   for the typing
  interface Props {
    value: string;
    closeModal: () => {};
  }

  let { value, closeModal }: Props = $props();

  const handleCloseUpdateModal = () => {
    closeModal();
  };
</script>

<div
  class="fixed inset-0 z-10 backdrop-blur-sm bg-black/50 flex items-center justify-center"
>
  <div
    class="bg-white rounded-4xl px-10 py-5 w-full max-w-lg h-80 motion-preset-slide-down-sm motion-duration-300"
  >
    <div class="space-y-5">
      <div class="flex items-center justify-between">
        <h1 class="capitalize text-2xl">update</h1>
        <button
          aria-label="close modal button"
          onclick={handleCloseUpdateModal}
          title="Close Modal"
          class="flex items-center cursor-pointer hover:outline-1 transition duration-200 justify-center p-2 rounded-full bg-blue-50 text-blue-900"
        >
          <CloseIcon height="1.3em" />
        </button>
      </div>

      <div>
        <p class="text-lg">
          Make changes to your profile here. Click save when you're done.
        </p>
      </div>

      <div>
        <TextInput
          type="text"
          id={value}
          label={value}
          {value}
          placeholder=""
          name=""
          errorValue=""
        />
      </div>

      <div class="flex items-center justify-end">
        <div class="flex items-center gap-3">
          <button
            aria-label="cancel button"
            title="Cancel Button"
            class="flex items-center justify-center"
          >
            <span>Cancel</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</div>
