const API_BASE_URL = "http://127.0.0.1:8000"

export const endpoints = {
    login: `${API_BASE_URL}/api/knox/auth/login/`,
    check_id: `${API_BASE_URL}/check-id/`,
    create_record: `${API_BASE_URL}/guard/record/create/`,
    guard_profile: `${API_BASE_URL}/guard/profile/me/`
}

// examples
// check_id: http://127.0.0.1:8000/check-id/{human_id}
// list_create_record: http://127.0.0.1:8000/records
// guard_profile: http://127.0.0.1:8000/{guard_id}