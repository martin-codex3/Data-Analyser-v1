// See https://svelte.dev/docs/kit/types#app.d.ts

import type { ValidationError } from "@sveltejs/kit";

// for information about these interfaces
declare global {
	namespace App {
		interface Error {
			formErrors: ValidationError
		}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export { };
