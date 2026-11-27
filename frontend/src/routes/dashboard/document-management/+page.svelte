<script lang="ts">
    import AddIcon from "@iconify-svelte/tabler/plus";
    import CancelIcon from "@iconify-svelte/tabler/x";
    import { fly } from "svelte/transition";
    import IconFileTypePdf from "@iconify-svelte/tabler/file-type-pdf";
    import IconFileWord from "@iconify-svelte/tabler/file-word";
    import IconFileSpreadsheet from "@iconify-svelte/tabler/file-spreadsheet";
    import IconFileCode from "@iconify-svelte/tabler/file-code";
    import IconPhoto from "@iconify-svelte/tabler/photo";
    import DotsIcon from "@iconify-svelte/tabler/dots-vertical";
    import IconArrowsUpDown from "@iconify-svelte/tabler/arrows-up-down";
    import IconSortAscending from "@iconify-svelte/tabler/sort-ascending";
    import IconSortDescending from "@iconify-svelte/tabler/sort-descending";
    import ReloadIcon from "@iconify-svelte/tabler/reload";
    import FilterIcon from "@iconify-svelte/tabler/filter";
    import ChevronLeftIcon from "@iconify-svelte/tabler/chevron-left";
    import ChevronRightIcon from "@iconify-svelte/tabler/chevron-right";

    import {
        columnFilteringFeature,
        createFilteredRowModel,
        createPaginatedRowModel,
        createSortedRowModel,
        createTable,
        filterFn_includesString,
        FlexRender,
        globalFilteringFeature,
        rowPaginationFeature,
        rowSortingFeature,
        sortFn_alphanumeric,
        sortFn_datetime,
        sortFn_text,
        tableFeatures,
        type ColumnDef,
    } from "@tanstack/svelte-table";

    let toggleOptions: boolean = $state(false);

    const handleToggleOptions = () => {
        toggleOptions = !toggleOptions;
    };

    interface Props {
        title: string;
        label: string;
        Icon?: any;
        onClick?: () => void;
    }

    // for the sample data
    interface Document {
        document_name: string;
        document_type: string;
        document_size: number; // size in bytes
        uploaded_by: string;
        uploaded_date: string;
    }

    const document_data: Document[] = $derived([
        {
            document_name: "Q4_Financial_Report.pdf",
            document_type: "pdf",
            document_size: 2458624,
            uploaded_by: "Chisomo Banda",
            uploaded_date: "2026-11-24",
        },
        {
            document_name: "Vendor_Contract_2026.docx",
            document_type: "word",
            document_size: 842752,
            uploaded_by: "Thandiwe Phiri",
            uploaded_date: "2026-11-23",
        },
        {
            document_name: "Inventory_Stock_Nov.xlsx",
            document_type: "excel",
            document_size: 1572864,
            uploaded_by: "Kondwani Mwale",
            uploaded_date: "2026-11-23",
        },
        {
            document_name: "Invoice_Feed_Batch_88.xml",
            document_type: "xml",
            document_size: 194560,
            uploaded_by: "Madalitso Nyirenda",
            uploaded_date: "2026-11-22",
        },
        {
            document_name: "Site_Inspection_01.jpg",
            document_type: "image",
            document_size: 3145728,
            uploaded_by: "Chimwemwe Gondwe",
            uploaded_date: "2026-11-22",
        },
        {
            document_name: "Compliance_Policy_v3.pdf",
            document_type: "pdf",
            document_size: 1126400,
            uploaded_by: "Tadala Tembo",
            uploaded_date: "2026-11-21",
        },
        {
            document_name: "Onboarding_Checklist.docx",
            document_type: "word",
            document_size: 419840,
            uploaded_by: "Yamikani Chirwa",
            uploaded_date: "2026-11-21",
        },
        {
            document_name: "Regional_Sales_Targets.xlsx",
            document_type: "excel",
            document_size: 962560,
            uploaded_by: "Chisomo Banda",
            uploaded_date: "2026-11-20",
        },
        {
            document_name: "ERP_Export_Orders.xml",
            document_type: "xml",
            document_size: 524288,
            uploaded_by: "Kondwani Mwale",
            uploaded_date: "2026-11-20",
        },
        {
            document_name: "Warehouse_Layout_Plan.png",
            document_type: "image",
            document_size: 2097152,
            uploaded_by: "Chimwemwe Gondwe",
            uploaded_date: "2026-11-19",
        },
        {
            document_name: "Tax_Clearance_Certificate.pdf",
            document_type: "pdf",
            document_size: 737280,
            uploaded_by: "Thandiwe Phiri",
            uploaded_date: "2026-11-19",
        },
        {
            document_name: "Project_Proposal_Draft.docx",
            document_type: "word",
            document_size: 1280000,
            uploaded_by: "Tadala Tembo",
            uploaded_date: "2026-11-18",
        },
        {
            document_name: "Payroll_Summary_Oct.xlsx",
            document_type: "excel",
            document_size: 688128,
            uploaded_by: "Madalitso Nyirenda",
            uploaded_date: "2026-11-18",
        },
        {
            document_name: "Payment_Gateway_Log.xml",
            document_type: "xml",
            document_size: 311296,
            uploaded_by: "Yamikani Chirwa",
            uploaded_date: "2026-11-17",
        },
        {
            document_name: "Signed_Receipt_Scan.jpg",
            document_type: "image",
            document_size: 1474560,
            uploaded_by: "Chisomo Banda",
            uploaded_date: "2026-11-17",
        },
        {
            document_name: "Annual_Audit_Guidelines.pdf",
            document_type: "pdf",
            document_size: 3670016,
            uploaded_by: "Thandiwe Phiri",
            uploaded_date: "2026-11-16",
        },
        {
            document_name: "Meeting_Minutes_Nov15.docx",
            document_type: "word",
            document_size: 358400,
            uploaded_by: "Kondwani Mwale",
            uploaded_date: "2026-11-15",
        },
        {
            document_name: "Supplier_Price_List.xlsx",
            document_type: "excel",
            document_size: 1048576,
            uploaded_by: "Chimwemwe Gondwe",
            uploaded_date: "2026-11-15",
        },
        {
            document_name: "Config_Schema_v2.xml",
            document_type: "xml",
            document_size: 131072,
            uploaded_by: "Tadala Tembo",
            uploaded_date: "2026-11-14",
        },
        {
            document_name: "Equipment_Photo_Front.webp",
            document_type: "image",
            document_size: 983040,
            uploaded_by: "Madalitso Nyirenda",
            uploaded_date: "2026-11-14",
        },
        {
            document_name: "Service_Level_Agreement.pdf",
            document_type: "pdf",
            document_size: 1843200,
            uploaded_by: "Yamikani Chirwa",
            uploaded_date: "2026-11-13",
        },
        {
            document_name: "SOP_Safety_Procedures.docx",
            document_type: "word",
            document_size: 921600,
            uploaded_by: "Chisomo Banda",
            uploaded_date: "2026-11-12",
        },
        {
            document_name: "Expense_Tracker_2026.xlsx",
            document_type: "excel",
            document_size: 1351680,
            uploaded_by: "Thandiwe Phiri",
            uploaded_date: "2026-11-12",
        },
        {
            document_name: "Customs_Manifest_402.xml",
            document_type: "xml",
            document_size: 466944,
            uploaded_by: "Kondwani Mwale",
            uploaded_date: "2026-11-11",
        },
        {
            document_name: "Fleet_Vehicle_Damage.jpg",
            document_type: "image",
            document_size: 2621440,
            uploaded_by: "Chimwemwe Gondwe",
            uploaded_date: "2026-11-10",
        },
        {
            document_name: "Insurance_Policy_Schedule.pdf",
            document_type: "pdf",
            document_size: 2211840,
            uploaded_by: "Tadala Tembo",
            uploaded_date: "2026-11-09",
        },
        {
            document_name: "Client_Brief_Template.docx",
            document_type: "word",
            document_size: 512000,
            uploaded_by: "Madalitso Nyirenda",
            uploaded_date: "2026-11-08",
        },
        {
            document_name: "Quarterly_Budget_Forecast.xlsx",
            document_type: "excel",
            document_size: 1769472,
            uploaded_by: "Yamikani Chirwa",
            uploaded_date: "2026-11-07",
        },
        {
            document_name: "Accounting_Journal_Sync.xml",
            document_type: "xml",
            document_size: 614400,
            uploaded_by: "Chisomo Banda",
            uploaded_date: "2026-11-06",
        },
        {
            document_name: "Office_Badge_Sample.png",
            document_type: "image",
            document_size: 786432,
            uploaded_by: "Thandiwe Phiri",
            uploaded_date: "2026-11-05",
        },
    ]);

    const uploadOptions: Props[] = $derived([
        {
            title: "PDF Document",
            label: "Upload PDF (.pdf)",
            Icon: IconFileTypePdf,
            accept: ".pdf,application/pdf",
        },
        {
            title: "Word Document",
            label: "Upload Word (.doc, .docx)",
            Icon: IconFileWord,
            accept: ".doc,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        },
        {
            title: "Excel Spreadsheet",
            label: "Upload Excel (.xls, .xlsx)",
            Icon: IconFileSpreadsheet,
            accept: ".xls,.xlsx,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        },
        {
            title: "XML File",
            label: "Upload XML (.xml)",
            Icon: IconFileCode,
            accept: ".xml,application/xml,text/xml",
        },
        {
            title: "Image",
            label: "Upload Image (PNG, JPG, WebP)",
            Icon: IconPhoto,
            accept: "image/*",
        },
    ]);

    // for the sample tanstack table here
    const features = tableFeatures({
        columnFilteringFeature,
        globalFilteringFeature,
        rowSortingFeature,
        rowPaginationFeature,
        sortedRowModel: createSortedRowModel(),
        filteredRowModel: createFilteredRowModel(),
        paginatedRowModel: createPaginatedRowModel(),
        sortFns: {
            alphanumeric: sortFn_alphanumeric,
            text: sortFn_text,
            datetime: sortFn_datetime,
        },
        filterFns: {
            includesString: filterFn_includesString,
        },
    });

    const columns: ColumnDef<typeof features, Document>[] = [
        {
            accessorKey: "document_name",
            header: "Document name",
        },
        {
            accessorKey: "document_type",
            header: "Document type",
        },
        {
            accessorKey: "document_size",
            header: "Document size",
        },
        {
            accessorKey: "uploaded_by",
            header: "Uploaded by",
        },
        {
            accessorKey: "uploaded_date",
            header: "Uploaded date",
        },
    ];

    // for toggling the main options here
    let toggleRow: boolean = $state(false);

    // the table instance here
    const table = createTable({
        features,
        columns,
        get data() {
            return document_data;
        },
        globalFilterFn: "includesString",
    });

    const handleToggleRow = () => {
        toggleRow = true;
    };

    // for the page sizes
    let pageSize: number[] = $state([10, 20, 30, 40, 50]);
</script>

<div class="h-screen overflow-hidden flex items-center justify-end">
    <!-- for the preview card here -->
    <div
        class="relative bg-primary-slight-black rounded-4xl h-[calc(100vh-2rem)] w-full"
    >
        <div class="h-full flex flex-col items-stretch justify-between">
            <!-- for the table header here -->
            <div class="flex items-center px-5 py-5 justify-between">
                <div class="">
                    <h1 class="text-xl font-semibold first-letter:capitalize">
                        manage your files
                    </h1>
                </div>

                <div class="hidden md:block">
                    <input
                        type="search"
                        value={table.atoms.globalFilter.get() ?? ""}
                        oninput={(e) =>
                            table.setGlobalFilter(
                                (e.target as HTMLInputElement).value,
                            )}
                        placeholder="Search all columns"
                        class="w-full border outline-none px-3 bg-transparent rounded-xl border-white ring-0"
                    />
                </div>

                <div class="flex items-center gap-3">
                    <button
                        aria-label="refresh data"
                        title="Refresh"
                        class="flex items-center justify-center p-2 rounded-full text-gray-300 bg-black hover:border-black/10 cursor-pointer transition duration-200"
                    >
                        <ReloadIcon height="1.5em" class="shrink-0" />
                    </button>

                    <button
                        aria-label="filter"
                        title="Filter"
                        class="flex items-center justify-center p-2 rounded-full text-gray-300 bg-black cursor-pointer transition duration-200"
                    >
                        <FilterIcon height="1.5em" class="shrink-0" />
                    </button>
                </div>
            </div>

            <div class="h-full overflow-auto scrollbar-none">
                <table class="w-full table-auto border-collapse">
                    <thead>
                        {#each table.getHeaderGroups() as headerGroup (headerGroup.id)}
                            <tr class="">
                                {#each headerGroup.headers as header}
                                    <th
                                        onclick={header.column.getToggleSortingHandler()}
                                        class="text-start p-4 font-normal border-b border-b-white/10 cursor-pointer hover:bg-black/30"
                                    >
                                        <div class="flex items-center gap-2">
                                            {#if !header.isPlaceholder}
                                                <FlexRender {header} />
                                            {/if}

                                            {#if header.column.getIsSorted() === "asc"}
                                                <IconSortAscending
                                                    height="1.2em"
                                                    class="shrink-0"
                                                />
                                            {:else if header.column.getIsSorted() === "desc"}
                                                <IconSortDescending
                                                    height="1.2em"
                                                    class="shrink-0"
                                                />
                                            {:else if header.column.getCanSort()}
                                                <IconArrowsUpDown
                                                    height="1.2em"
                                                    class="shrink-0"
                                                />
                                            {/if}
                                        </div>
                                    </th>
                                {/each}

                                <th
                                    class="text-start p-4 border-b border-b-white/10"
                                ></th>
                            </tr>
                        {/each}
                    </thead>

                    <tbody class="max-w-full">
                        {#each table.getRowModel().rows as rows (rows.id)}
                            <tr
                                class="relative odd:bg-black/10 text-start border-b border-b-white/10"
                            >
                                {#each rows.getAllCells() as cell (cell.id)}
                                    <td
                                        transition:fly={{
                                            x: 100,
                                            y: 40,
                                            duration: 300,
                                        }}
                                        class="font-normal p-4 py-5"
                                    >
                                        <FlexRender {cell} />
                                    </td>
                                {/each}

                                {#if rows.getAllCells().length === 0}
                                    <td class="">
                                        <div>
                                            <h1>No records available</h1>
                                        </div>
                                    </td>
                                {/if}

                                <td class="border-b border-b-white/10">
                                    <button
                                        aria-label="more options button"
                                        title="More Options"
                                        onclick={handleToggleRow}
                                        class="flex items-center justify-center cursor-pointer hover:bg-black rounded-full p-2"
                                    >
                                        <DotsIcon
                                            height="1.3em"
                                            class="shrink-0"
                                        />
                                    </button>
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>

            <!-- for the table footer here -->
            <div class="flex items-center justify-center px-20 py-3">
                <div class="flex items-center gap-1">
                    <button
                        aria-label="pagination-page-1"
                        onclick={() => table.firstPage()}
                        disabled={!table.getCanPreviousPage()}
                        class="flex items-center justify-cneter px-5 text-sm font-semibold py-2 bg-white text-black rounded-l-full rounded-r-lg cursor-pointer disabled:bg-white/70"
                    >
                        <span class="first-letter:capitalize shrink-0"
                            >first</span
                        >
                    </button>

                    <button
                        aria-label="pagination-page-1"
                        title="Previous"
                        onclick={() => table.previousPage()}
                        disabled={!table.getCanPreviousPage()}
                        class="flex items-center justify-cneter px-3 text-sm font-semibold py-2 bg-white text-black cursor-pointer"
                    >
                        <ChevronLeftIcon height="1.3em" />
                        <span class="first-letter:capitalize">prev</span>
                    </button>

                    <button
                        aria-label="pagination-page-1"
                        title="Next"
                        class="flex items-center justify-cneter px-5 text-sm font-semibold py-2 bg-white text-black cursor-pointer"
                    >
                        <span class="first-letter:capitalize">next</span>
                        <ChevronRightIcon height="1.3em" />
                    </button>

                    <button
                        aria-label="pagination-page-1"
                        onclick={() => table.lastPage()}
                        disabled={!table.getCanLastPage()}
                        class="flex items-center justify-center disabled:bg-white/70 px-5 text-sm font-semibold py-2 bg-white text-black rounded-r-full cursor-pointer"
                    >
                        <span class="first-letter:capitalize">last</span>
                    </button>
                </div>
            </div>
        </div>
        <div class="absolute bottom-5 right-3">
            <button
                aria-label="more options"
                title="More Options"
                onclick={() => handleToggleOptions}
                class="flex items-center justify-center bg-primary-main-black rounded-full p-2 cursor-pointer border shadow-sm"
            >
                {#if toggleOptions}
                    <CancelIcon
                        height="1.5em"
                        class={[
                            toggleOptions
                                ? "rotate-180 transition duration-300 shrink-0"
                                : "shrink-0",
                        ]}
                    />
                {:else}
                    <AddIcon height="1.5em" class="shrink-0" />
                {/if}
            </button>
        </div>
    </div>
</div>

<!-- for the more options -->
{#if toggleOptions}
    <div class="fixed bg-black/30 inset-0">
        <div
            transition:fly={{ duration: 200, x: 10, y: 30 }}
            class="absolute bottom-20 space-y-5 flex flex-col items-start px-5 py-5 right-18 bg-primary-main-black rounded-4xl w-sm border border-gray-100/10 shadows-m"
        >
            {#each uploadOptions as upload}
                <button
                    aria-label="Uploading options"
                    title={upload.title}
                    class="flex items-center gap-2 cursor-pointer"
                >
                    <upload.Icon height="1.5em" class="shrink-0" />
                    <span>{upload.title}</span>
                </button>
            {/each}
        </div>
    </div>
{/if}
