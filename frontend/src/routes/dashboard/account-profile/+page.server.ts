import { fail, json, redirect, type Actions, type ValidationError } from "@sveltejs/kit";
import type { PageServerLoad } from "../../$types";
import { PUBLIC_API_ENDPOINT } from "$app/env/public"
import type { ValidationErrors } from "#lib/types/validation_errors.ts";

export const load: PageServerLoad = async ({ locals, fetch }) => {
    const user = locals.user;
    const token = locals.token;

    if (!user) {
        redirect(307, "/");
    }

    if (!token) {
        redirect(307, "/");
    }

    // we will attempt to fetch the current tenant here 
    const response = await fetch(`${PUBLIC_API_ENDPOINT}/tenants`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${locals.token}`
        }
    });

    if (!response.ok) {
        const responseData: ValidationErrors = await response.json();
        fail(response.status, { problem: responseData });
    }

    const tenant = await response.json()

    return { user, tenant }
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
            headers: { "Content-Type": "application/json", "Authorization": `Bearer ${locals.token}` },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationError = await response.json();
            return fail(response.status, { problem: responseData })
        }

        // if the response if okay
        return { success: true }
    },

    // for updating the tenant data
    editTenant: async ({ locals, fetch, request }) => {
        const user = locals.user;

        const data = await request.formData()

        if (!user) {
            redirect(307, "/")
        }


        const payload = Object.fromEntries(data.entries())

        const response = await fetch(`${PUBLIC_API_ENDPOINT}/tenants`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json", "Authorization": `Bearer ${locals.token}` },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationError = await response.json();
            return fail(response.status, { problem: responseData });
        }

        return { success: true }

    },

    // for logging out the users 
    logoutUser: async ({ locals, fetch, cookies }) => {
        const user = locals.user

        if (!user) {
            redirect(307, "/");
        }

        cookies.delete("access_token", { path: "/" });

        return { success: true }

    }
}