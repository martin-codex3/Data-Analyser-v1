export interface TenantResponse {
    id: string
    business_name: string
    business_type: string
    business_email: string
    business_phone: string
    registration_number: string
    industry: string
    address_line_1: string
    address_line_2: string
    city: string
    region: string
    postal_code: string
    country_code: string
    status: string
    website_url: string
    slug: string
    settings: object
    created_by_id: string
    created_at: string
    updated_at: string
    is_deleted: boolean
    description: string
    business_logo: string
}