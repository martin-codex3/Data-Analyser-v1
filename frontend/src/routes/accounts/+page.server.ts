import { fail, type Actions } from "@sveltejs/kit";
import { PUBLIC_API_ENDPOINT } from "$app/env/public"
import type { ValidationErrors } from "#lib/types/validation_errors.ts";
import type { CreateTenant } from "#lib/types/tenant/create_tenant.ts";
import type { Token } from "#lib/types/tokens/token.ts";

export const actions: Actions = {
    createAccount: async ({ request, fetch, cookies }) => {
        const data = await request.formData()

        const first_name = data.get("first_name")?.toString().trim() ?? "";
        const last_name = data.get("last_name")?.toString().trim() ?? "";
        const address_line_1 = data.get("address_line_1")?.toString().trim() ?? "";
        const country_code = data.get("country_code")?.toString().trim() ?? "";
        const business_name = data.get("business_name")?.toString().trim() ?? "";
        const business_type = data.get("business_type")?.toString().trim() ?? "";
        const business_email = data.get("business_email")?.toString().trim() ?? "";
        const business_phone = data.get("business_phone")?.toString().trim() ?? "";
        const email = data.get("email")?.toString().trim() ?? "";
        const phone_number = data.get("phone_number")?.toString().trim() ?? "";
        const password = data.get("password")?.toString() ?? "";

        const payload: CreateTenant = {
            first_name: first_name,
            last_name: last_name,
            phone_number: phone_number,
            address_line_1: address_line_1,
            email: email,
            business_name: business_name,
            business_type: business_type,
            business_email: business_email,
            business_phone: business_phone,
            password_hash: password
        }

        // we will attempt to save the details here
        const response = await fetch(`${PUBLIC_API_ENDPOINT}/tenants/create-tenant-account`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json()
            return fail(response.status, { problem: responseData });
        }

        // we will set the cookies here 
        if (response.ok) {
            const responseData: Token = await response.json();
            cookies.set("access_token", responseData.access_token, {
                httpOnly: true,
                secure: true,
                sameSite: "lax"
            });
        }

        return { success: true }
    }
}