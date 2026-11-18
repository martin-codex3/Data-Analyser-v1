import { fail, redirect, type Actions } from "@sveltejs/kit";
import type { PageServerLoad } from "../../$types";
import { PUBLIC_API_ENDPOINT } from "$app/env/public"
import type { ValidationErrors } from "#lib/types/validations/validation_errors.ts";

export const load: PageServerLoad = async ({ locals }) => {
    const user = locals.user;

    if (!user) {
        redirect(307, "/")
    }

    return { user }
}

export const actions: Actions = {
    updateProfile: async ({ locals, fetch, request }) => {
        const user = locals.user;

        if (!user) {
            redirect(307, "/")
        }

        const access_token = locals.token;

        const data = await request.formData();
        const payload = Object.fromEntries(data);

        const response = await fetch(`${PUBLIC_API_ENDPOINT}/users/${user.id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${access_token}`
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json();
            return fail(response.status, { problem: responseData });
        }

        return { success: true }
    }
}