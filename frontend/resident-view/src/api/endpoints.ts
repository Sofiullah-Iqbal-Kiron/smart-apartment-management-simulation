const API_BASE = 'http://127.0.0.1:8000/'

export const endpoints = {
    basic_auth: `${API_BASE}resident/auth/basic/`,
    submit_issue: `${API_BASE}resident/issue/create/`,
    delete_issue: `${API_BASE}resident/issue/delete/`,
    sought_token: `${API_BASE}resident/token/sought/`,
    my_profile: `${API_BASE}resident/profile/me/`,
}