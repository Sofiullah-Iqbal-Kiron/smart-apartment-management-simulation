import { create } from "zustand";

interface User {
    username: string;
    fullname: string;
    email: string;
    since: string;
}

interface Human {
    user: User;
    gender: string;
    nid_or_br: string;
    contact: string;
    date_of_birth: string;
    avatar: string;
}

interface Accommodation {
    label: string;
    floor: string;
}

interface Record {
    record_of: string;
    record_type: string;
    recorded_at: string;
    recorded_by: string;
}

interface Issue {
    id: number,
    title: string,
    details: string,
    raised_at: string,
    last_updated: string,
    emergency: boolean,
    checked: boolean,
    resolved: boolean,
    edited: boolean
}

interface Resident {
    human: Human;
    accommodation: Accommodation;
    ID: string;
    issues: Array<Issue>;
    records: Array<Record>;
}

let demo_resident_data: Resident = {
    human: {
        user: {
            username: "demo username",
            fullname: "Sofiullah Iqbal Kiron",
            email: "example@gmail.com",
            since: "demo date",
        },
        gender: "demo unknown",
        nid_or_br: "demo nid",
        contact: "01701928374",
        date_of_birth: "demo date of birth",
        avatar: "demo link src",
    },
    accommodation: {
        label: "demo label",
        floor: "demo block",
    },
    ID: "RS-painai",
    issues: [],
    records: []
};

const residentProfileDataStore = (set: any) => ({
    residentProfileData: demo_resident_data,
    setResidentProfileData: (profileData: Resident) => set({ residentProfileData: profileData })
})

export const useResidentProfileData = create(residentProfileDataStore)

interface BasicAuthDataType {
    username: string,
    password: string
}

interface BasicAuthStoreType {
    username: string,
    password: string,
    setAuth: () => void
}

const basic_auth_store = (set: any) => ({
    username: "",
    password: "",
    setAuth: ({ username, password }: BasicAuthDataType) => set({ username: username, password: password })
})

export const useBasicAuth = create(basic_auth_store);