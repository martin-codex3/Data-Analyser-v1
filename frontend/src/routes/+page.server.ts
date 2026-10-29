import { fail, type Actions } from "@sveltejs/kit";
import { PUBLIC_API_ENDPOINT } from "$app/env/public"
import type { ValidationErrors } from "#lib/types/validation_errors.ts";
import type { CreateTenant } from "#lib/types/tenant/create_tenant.ts";

export const actions: Actions = {
    createAccount: async ({ request, fetch }) => {
        const data = await request.formData()

        const first_name = data.get("first_name")?.toString().trim() ?? "";
        const last_name = data.get("last_name")?.toString().trim() ?? "";
        const address = data.get("address")?.toString().trim() ?? "";
        const nationality = data.get("nationality")?.toString().trim() ?? "";
        const business_name = data.get("business_name")?.toString().trim() ?? "";
        const business_type = data.get("business_type")?.toString().trim() ?? "";
        const email = data.get("email")?.toString().trim() ?? "";
        const phone_number = data.get("phone_number")?.toString().trim() ?? "";
        const password = data.get("password")?.toString() ?? "";

        const payload: CreateTenant = {
            first_name: first_name,
            last_name: last_name,
            phone_number: phone_number,
            address: address,
            email: email,
            nationality: nationality,
            business_name: business_name,
            business_type: business_type,
            password_hash: password
        }

        // we will attempt to save the details here
        const response = await fetch(`${PUBLIC_API_ENDPOINT}/tenants/create-account`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json()
            return fail(response.status, { problem: responseData });
        }

        return { success: true }
    }
}