import { json, redirect, type Actions } from "@sveltejs/kit";
import type { PageServerLoad } from "../../$types";
import { PUBLIC_API_ENDPOINT } from "$app/env/public"

export const load: PageServerLoad = async ({ locals }) => {
    const user = locals.user;

    if (!user) {
        redirect(307, "/");
    }
    return { user }
}

export const actions: Actions = {
    editProfile: async ({ request, fetch, locals }) => {
        // we will check if the user is still logges in
        const user = locals.user
        if (!user) {
            redirect(307, "/")
        }

        const data = await request.formData();
        const payload = Object.fromEntries(data.entries());

        console.log(payload)

        // we will attempt to update the client here 
        // const response = await fetch(`${PUBLIC_API_ENDPOINT}/`)
    }
}