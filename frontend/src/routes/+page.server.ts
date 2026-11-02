import { fail, type Actions } from "@sveltejs/kit";
import { PUBLIC_API_ENDPOINT } from "$app/env/public"
import type { ValidationErrors } from "#lib/types/validation_errors.ts";


export const actions: Actions = {
    signIn: async ({ fetch }) => {
        const response = await fetch(`${PUBLIC_API_ENDPOINT}/users/token`, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: FormData.toString()
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json();
            return fail(response.status, { problem: responseData });
        }

        if (response.ok) {
            console.log(await response.json());
        }

        return { success: true }
    }
}