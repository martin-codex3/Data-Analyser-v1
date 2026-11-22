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
    },

    handleUploadedFile: async ({ request, fetch, locals }) => {
        const user = locals.user;

        if (!user) {
            redirect(307, "/")
        }
        const access_token = locals.token;

        const data = await request.formData();
        const file = data.get("file");

        if (!(file instanceof File) || file.size === 0) {
            return fail(400, { message: "Send valid files (JPEG, JPG, PNG, GIF)" });
        }

        const fileData = new FormData();
        fileData.append("file", file, file.name);

        const response = await fetch(`${PUBLIC_API_ENDPOINT}/users/${user.id}/picture`, {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${access_token}`
            },
            body: fileData
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json()
            return fail(response.status, { problem: responseData });
        }

        return { success: true }
    },

    logoutUsers: async ({ locals, cookies }) => {
        const access_token = locals.token;

        if (!access_token) {
            redirect(307, "/");
        }

        cookies.delete("access_token", { path: "/" });

    }
}