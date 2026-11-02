import { error, redirect } from "@sveltejs/kit";
import type { Handle } from "@sveltejs/kit/hooks";
import { PUBLIC_API_ENDPOINT } from "$app/env/public";


export const handle: Handle = async ({ event, resolve }) => {
    event.locals.token = event.cookies.get("access_token");
    const access_token = event.locals.token;
    event.locals.user = null;

    if (!access_token) {
        if (event.url.pathname.startsWith("/dashboard")) {
            redirect(307, "/");
        }
    }

    if (access_token) {
        const response = await fetch(`${PUBLIC_API_ENDPOINT}/users/me`, {
            method: "GET",
            headers: { "Content-Type": "application/json", Authorization: `Bearer ${access_token}` }
        });

        if (response.status === 401 || response.status === 403) {
            event.cookies.delete("access_token", { path: "/" });
        } else if (!response.ok) {
            redirect(307, "Unable to verify authentication");
        } else {
            event.locals.user = await response.json()
        }
    }

    const response = await resolve(event);
    return response;
}