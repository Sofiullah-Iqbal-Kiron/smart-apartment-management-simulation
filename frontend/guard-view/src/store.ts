import { create } from 'zustand'

const human_store = (set: any) => ({
    human_id: '',
    setHumanID: (new_id: string) => set({ human_id: new_id })
})

export const useHumanID = create(human_store)

// second global state hook
interface User {
    username: string,
    fullname: string,
    email: string,
    since: string,
}

interface Human {
    user: User,
    gender: string,
    nid_or_br: string,
    contact: string,
    date_of_birth: string,
    avatar: string,
}

export interface Record {
    record_of: string,
    record_type: string,
    recorded_at: string,
    recorded_by: string
}

interface Guard {
    human: Human,
    salary: number, // read only
    guard_id: string, // read only
    records: Array<Record>, // read only
    // salary_earned: number, // read only field at serializer
    // number_of_registered_guests: number, // read only
    // total_salary_withdrawal: number,
}

const a_user: User = {
    username: 'demo-username',
    fullname: 'demo-fullname',
    email: 'example@yahoo.com',
    since: 'no date: demo'
}

const a_human: Human = {
    user: a_user,
    gender: 'unknown',
    nid_or_br: 'unknown',
    contact: '01xxxxxxxxx',
    date_of_birth: 'no date - demo',
    avatar: 'https://i.postimg.cc/N0dmbCHk/logo-original.png'
}

const a_record: Record = {
    record_of: 'none',
    record_type: 'unknown',
    recorded_at: 'demo date-time',
    recorded_by: 'GA-demo'
}

const a_guard: Guard = {
    human: a_human,
    salary: 0,
    guard_id: 'GA-0000001',
    records: [a_record, a_record, a_record],
    // salary_earned: 0,
    // number_of_registered_guests: 0
}

const guard_store = (set: any) => ({
    guard: a_guard,
    setGuardData: (data: Guard) => set({ guard: data })
})

export const useGuardData = create(guard_store)

const auth_token_store = (set: any) => ({
    AUTH_TOKEN: "",
    setAuthToken: (token: string) => set({ AUTH_TOKEN: token })
})

export const useAuthToken = create(auth_token_store)