import { fail, json, redirect, type Actions, type ValidationError } from "@sveltejs/kit";
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

        // we will attempt to update the client here 
        const response = await fetch(`${PUBLIC_API_ENDPOINT}/users/${user.id}`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json", "Authorization": "Bearer" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationError = await response.json();
            fail(response.status, { problem: responseData })
        }

        // if the response if okay
        return { success: true }
    }
}