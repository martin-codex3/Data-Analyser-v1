import { error, redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";

import type { ValidationErrors } from "#lib/types/validations/validation_errors.ts";

export const load: PageServerLoad = async ({ locals, fetch }) => {


}