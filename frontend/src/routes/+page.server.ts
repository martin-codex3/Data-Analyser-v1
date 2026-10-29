import { fail, type Actions } from "@sveltejs/kit";
import { PRIVATE_API_ENDPOINT } from "$app/env/public"

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

        // we will attempt to save the details here
        const response = await fetch(`${PRIVATE_API_ENDPOINT}/tenants`, {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        });

        if (!response.ok) {
            const responseData = await response.json()
            return fail(response.status, { message: "Failed to create account" });
        }

        return { success: true }
    }
}