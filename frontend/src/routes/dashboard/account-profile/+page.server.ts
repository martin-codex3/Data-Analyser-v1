import { redirect, type Actions } from "@sveltejs/kit";
import type { PageServerLoad } from "../../$types";

export const load: PageServerLoad = async ({ locals }) => {
    const user = locals.user;

    if (!user) {
        redirect(307, "/")
    }

    return { user }
}

export const actions: Actions = {
    updateProfile: async ({ locals, fetch }) => {
        const user = locals.user;

        if (!user) {
            redirect(307, "/")
        }

        console.log("hey mate here");
    }
}