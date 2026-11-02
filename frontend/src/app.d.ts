// See https://svelte.dev/docs/kit/types#app.d.ts

import type { Token } from "#lib/types/tokens/token.ts";
import type { User } from "#lib/types/users/user.ts";
import type { ValidationError } from "@sveltejs/kit";

// for information about these interfaces
declare global {
	namespace App {
		interface Error {
			formErrors: ValidationError
		}
		interface Locals {
			token: Token,
			user: User
		}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export { };
