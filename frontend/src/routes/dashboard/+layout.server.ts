import { error, redirect } from "@sveltejs/kit";
import type { LayoutServerLoad } from "./$types";
import { PUBLIC_API_ENDPOINT } from "$app/env/public";
import type { TenantResponse } from "#lib/types/tenants/tenant_response.ts";

export const load: LayoutServerLoad = async ({ locals }) => {
    const user = locals.user;

    if (!user) {
        redirect(307, "/")
    }
    const access_token = locals.token;

    const response = await fetch(`${PUBLIC_API_ENDPOINT}/tenants/${user.id}`, {
        method: "GET",
        headers: { "Content-Type": "application/json", "Authorization": `Bearer ${access_token}` }
    });

    if (!response.ok) {
        error(401, 'Failed to fetch the data');
    }

    const tenant: TenantResponse = await response.json();

    return { user: user, tenant }
}