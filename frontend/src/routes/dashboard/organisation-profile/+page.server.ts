import type { Actions } from "@sveltejs/kit";

export const actions: Actions = {
    updateTenantProfile: async ({ fetch, locals, request }) => {
        console.log("Hey mate we are here too");
    }
}