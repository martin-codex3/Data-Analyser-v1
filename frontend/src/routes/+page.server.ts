import { fail, type Actions } from "@sveltejs/kit";
import { PUBLIC_API_ENDPOINT } from "$app/env/public"
import type { ValidationErrors } from "#lib/types/validations/validation_errors.ts";
import type { AccessToken } from "#lib/types/token/access_token.ts";



export const actions: Actions = {
    signIn: async ({ fetch, request, cookies }) => {
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
            console.log(responseData)
            return fail(response.status, { problem: responseData });
        }

        if (response.ok) {
            const responseData: AccessToken = await response.json();
            cookies.set("access_token", responseData.access_token ?? "", {
                secure: true,
                httpOnly: true,
                sameSite: "lax"
            });
        }

        return { success: true }
    }
}