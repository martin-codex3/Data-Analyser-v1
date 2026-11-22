import type { ValidationErrors } from "../validations/validation_errors";

export interface FormResponse {
    success?: boolean;
    message?: string | undefined;
    problem?: ValidationErrors
}