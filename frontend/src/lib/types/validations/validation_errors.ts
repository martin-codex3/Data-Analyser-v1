export interface ErrorDetail {
    code: string,
    detail: string,
    pointer: string
}

export interface ValidationErrors {
    type: string,
    title: string,
    status: number,
    code: string,
    detail: string,
    errors: ErrorDetail[]
}