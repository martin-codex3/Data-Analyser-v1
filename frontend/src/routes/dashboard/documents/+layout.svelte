<script lang="ts">
  import { page } from "$app/state";
  let { children } = $props();
  import DocumentsIcon from "@iconify-svelte/tabler/files";
  import UpdalodIcon from "@iconify-svelte/tabler/upload";

  const documentLinks = [
    { label: "All Documents", to: "dashboard/documents", icon: DocumentsIcon },
    {
      label: "Upload Document",
      to: "dashboard/documents",
      icon: DocumentsIcon,
    },
    {
      label: "Document Details",
      to: "dashboard/documents",
      icon: DocumentsIcon,
    },
    { label: "Archive", to: "dashboard/documents", icon: DocumentsIcon },
    {
      label: "Delete Documents",
      to: "dashboard/documents",
      icon: DocumentsIcon,
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
      <ul class="">
        <li class="">
          <a
            href="/dashboard/documents"
            class={[
              "flex items-center gap-2 rounded-full px-4 py-2 hover:bg-blue-50 hover:text-blue-800",
              page.url.pathname === "/dashboard/documents"
                ? "bg-blue-50 text-blue-900"
                : "",
            ]}
          >
            <DocumentsIcon height="1.8em" class="shrink-0" />
            <span class="capitalize">all documents</span>
          </a>
        </li>

        <li class="">
          <a href="/documents/all-documents" class="flex items-center gap-2">
            <DocumentsIcon height="1.8em" class="shrink-0" />
            <span class="capitalize">upload documents</span>
          </a>
        </li>

        <li class="">
          <a href="/documents/all-documents" class="flex items-center gap-2">
            <DocumentsIcon height="1.8em" class="shrink-0" />
            <span class="capitalize">document details</span>
          </a>
        </li>

        <li class="">
          <a href="/documents/all-documents" class="flex items-center gap-2">
            <DocumentsIcon height="1.8em" class="shrink-0" />
            <span class="capitalize">archived</span>
          </a>
        </li>

        <li class="">
          <a href="/documents/all-documents" class="flex items-center gap-2">
            <DocumentsIcon height="1.8em" class="shrink-0" />
            <span class="capitalize">deleted documents</span>
          </a>
        </li>
      </ul>
    </div>
  </div>
</section>

<section class="ms-80 py-3">
  {@render children()}
</section>
