import { fail, type Actions } from "@sveltejs/kit";
import { PUBLIC_API_ENDPOINT } from "$app/env/public";
import type { CreateTenant } from "#lib/types/tenants/create_tenant.ts";
import type { ValidationErrors } from "#lib/types/validations/validation_errors.ts";

export const actions: Actions = {
    createAccount: async ({ request, fetch }) => {
        const data = await request.formData();

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
        const password_hash = data.get("password_hash")?.toString() ?? "";

        const payload: CreateTenant = {
            first_name: first_name,
            last_name: last_name,
            address_line_1: address_line_1,
            country_code: country_code,
            business_name: business_name,
            business_type: business_type,
            business_email: business_email,
            business_phone: business_phone,
            email: email,
            phone_number: phone_number,
            password_hash: password_hash
        }

        const response = await fetch(`${PUBLIC_API_ENDPOINT}/tenants/create-tenant-account`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json();
            console.log(responseData);
            return fail(response.status, { problem: responseData });
        }

        return { success: true }

    }
}