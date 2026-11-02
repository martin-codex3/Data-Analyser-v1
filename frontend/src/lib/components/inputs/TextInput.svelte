<script lang="ts">
  interface Props {
    id: string;
    label: string;
    type: string;
    name: string;
    placeholder: string;
  }

  let { id, label, type, name, placeholder }: Props = $props();
</script>

<div class="space-y-1">
  <label for={id}>{label}</label>
  <input
    {type}
    {name}
    {id}
    {placeholder}
    class={[
      "w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue",
    ]}
  />
</div>
