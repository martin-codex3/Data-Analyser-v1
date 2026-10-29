import type { ErrorDetails } from "./error_detail";

export interface ValidationErrors {
    type: string,
    title: string,
    status: number,
    code: string,
    errors: [ErrorDetails]
}