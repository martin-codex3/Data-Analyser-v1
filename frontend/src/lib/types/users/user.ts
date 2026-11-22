export interface User {
    id: string,
    first_name: string,
    last_name: string,
    phone_number: string,
    email: string,
    username: string | undefined,
    profile_image: string | undefined,
    is_email_verified: boolean | undefined
    bio: string | undefined,
    account_created_at: string,
    profile_image_url: string
}