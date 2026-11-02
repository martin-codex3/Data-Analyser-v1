import { redirect, type Actions } from "@sveltejs/kit";
import type { PageServerLoad } from "../../$types";

export const load: PageServerLoad = async ({ locals }) => {
    if (!locals.user) {
        redirect(307, "/");
    }

    return { user: locals.user }

}

export const actions: Actions = {
    default: async () => {
        console.log("hey")
    }
}