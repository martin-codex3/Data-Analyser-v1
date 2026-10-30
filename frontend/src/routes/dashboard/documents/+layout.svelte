<script lang="ts">
  import { page } from "$app/state";
  let { children } = $props();
  import DocumentsIcon from "@iconify-svelte/tabler/files";
  import UpdalodIcon from "@iconify-svelte/tabler/upload";
  import DocumentDetails from "@iconify-svelte/tabler/details";
  import DocumentArchiveIcon from "@iconify-svelte/tabler/archive";

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
    class="fixed overflow-auto top-1/2 -translate-y-1/2 space-y-10 border border-gray-300 bg-white px-5 py-6 rounded-4xl w-80 h-[calc(100vh-1rem)]"
  >
    <h1 class="capitalize text-lg font-semibold">documents manager</h1>

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
