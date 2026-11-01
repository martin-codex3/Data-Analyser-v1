<script lang="ts">
  import { page } from "$app/state";
  let { children } = $props();
  import DocumentsIcon from "@iconify-svelte/tabler/files";
  import UpdalodIcon from "@iconify-svelte/tabler/upload";
  import DocumentDetails from "@iconify-svelte/tabler/details";
  import DocumentArchiveIcon from "@iconify-svelte/tabler/archive";
  import CloseIcon from "@iconify-svelte/tabler/x";

  const documentLinks = [
    { label: "All Documents", to: "/dashboard/documents", icon: DocumentsIcon },
    {
      label: "Upload Document",
      to: "documents/upload-document",
      icon: UpdalodIcon,
    },
    {
      label: "Document Details",
      to: "documents/document-details",
      icon: DocumentDetails,
    },
    { label: "Archive", to: "documents/arichived", icon: DocumentsIcon },
    {
      label: "Deleted Documents",
      to: "documents/deleted-documents",
      icon: DocumentArchiveIcon,
    },
  ];
</script>

<section>
  <div
    class="fixed overflow-auto space-y-10 border-r border-gray-300 bg-white px-5 py-3 w-80 h-[calc(100vh)]"
  >
    <div class="flex items-center justify-between">
      <h1 class="capitalize text-lg font-semibold">manager</h1>
      <button
        aria-label="close-button"
        title="Close Panel"
        class="flex items-center justify-center text-blue-50 bg-primary-main-blue rounded-full p-2 cursor-pointer hover:shadow-sm transition duration-200"
      >
        <CloseIcon height="1.3em" />
      </button>
    </div>

    <!-- for the main navigation -->
    <div>
      <ul class="space-y-2">
        {#each documentLinks as link}
          <li>
            <a
              href={link.to}
              title={link.label}
              class={[
                "flex items-center gap-2 px-3 py-3 rounded-full hover:bg-blue-50 hover:text-blue-900 transition duration-300",
                page.url.pathname === link.to ? "bg-blue-50 text-blue-900" : "",
              ]}
            >
              <link.icon height="1.7em" />
              <span>{link.label}</span>
            </a>
          </li>
        {/each}
      </ul>
    </div>
  </div>
</section>

<section class="ms-80 py-3">
  {@render children()}
</section>
