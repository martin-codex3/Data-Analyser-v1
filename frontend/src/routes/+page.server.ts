import type { Actions } from "@sveltejs/kit";

export const actions: Actions = {
    createAccount: async ({ request, fetch }) => {
        const data = await request.formData()

        console.log(data)
    }
}