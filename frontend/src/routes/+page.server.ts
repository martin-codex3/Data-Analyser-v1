import type { Actions } from "@sveltejs/kit";

export const actions: Actions = {
    signIn: async () => {
        console.log("We will hit here")
    }
}