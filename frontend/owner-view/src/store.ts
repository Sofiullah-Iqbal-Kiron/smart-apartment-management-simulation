import { create } from "zustand";
import { THEMES } from "./constants";

const theme_store = (set: any) => ({
    theme: THEMES[2],
    setTheme: (name: string) => set({ theme: name })
})

export const useTheme = create(theme_store)