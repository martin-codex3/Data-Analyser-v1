import { fail, type Actions } from "@sveltejs/kit";
import { PUBLIC_API_ENDPOINT } from "$app/env/public"
import type { ValidationErrors } from "#lib/types/validation_errors.ts";


export const actions: Actions = {
    signIn: async ({ fetch, request }) => {
        const data = await request.formData();
        const username = data.get("username")?.toString().trim() ?? "";
        const password = data.get("password")?.toString().trim() ?? "";

        const payload = new URLSearchParams({
            "username": username,
            "password": password
        });

        const response = await fetch(`${PUBLIC_API_ENDPOINT}/users/token`, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: payload
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json();
            console.log(responseData);
            return fail(response.status, { problem: responseData });
        }

        if (response.ok) {
            console.log(await response.json());
        }

        return { success: true }
    }
}