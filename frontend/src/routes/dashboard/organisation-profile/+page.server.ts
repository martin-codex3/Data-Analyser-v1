import { error, redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";
import { PUBLIC_API_ENDPOINT } from "$app/env/public";
import type { ValidationErrors } from "#lib/types/validations/validation_errors.ts";

export const load: PageServerLoad = async ({ locals, fetch }) => {

    const current_user = locals.user;
    if (!current_user) {
        redirect(307, "/");
    }

    const access_token = locals.token;

    const response = await fetch(`${PUBLIC_API_ENDPOINT}/tenants/${current_user.id}`, {
        method: "GET",
        headers: { "Content-Type": "application/json", "Authorization": `Bearer ${access_token}` }
    });

    if (!response.ok) {
        error(401, 'Failed to fetch the data');
    }

    const tenant = await response.json();

    return { tenant }
}