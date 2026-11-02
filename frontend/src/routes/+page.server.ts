import type { Actions } from "@sveltejs/kit";
import { PUBLIC_API_ENDPOINT } from "$app/env/public"

export const actions: Actions = {
    signIn: async ({ fetch, request }) => {
        const data = await request.formData()

        const response = await fetch(`${PUBLIC_API_ENDPOINT}/users/token`, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: FormData.toString()
        });

        if (!response.ok) {
            console.log(await response.json());
        }

        if (response.ok) {
            console.log(await response.json());
        }
    }
}