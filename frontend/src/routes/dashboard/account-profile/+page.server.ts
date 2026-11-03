import { redirect, type Actions } from "@sveltejs/kit";
import type { PageServerLoad } from "../../$types";

export const load: PageServerLoad = async ({ locals }) => {
    const user = locals.user;

    if (!user) {
        redirect(307, "/");
    }
    return { user }
}

export const actions: Actions = {
    editProfile: async ({ request, fetch, locals }) => {

        const data = await request.formData();
        const first_name = data.get("first_name")?.toString().trim() ?? "";
        console.log(first_name)
    }
}