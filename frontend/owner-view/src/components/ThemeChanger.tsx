import { useForm } from "react-hook-form";
import { THEMES } from "../constants";
import { useTheme } from "../store";

export default function ThemeChanger() {
  const { register } = useForm();
  const currTheme = useTheme(state => state.theme);
  const setTheme = useTheme(state => state.setTheme);

  return (
    <form className="flex flex-col items-center space-y-0">
      <label htmlFor="themeChanger">Theme</label>
      <select id="themeChanger" {...register("theme")} onChange={e => setTheme(e.target.value)} className="select select-info select-sm">
        {THEMES.map((theme, idx) => <option key={idx} value={theme} selected={theme === currTheme}> {theme.charAt(0).toUpperCase()+theme.slice(1)} </option>)}
      </select>
    </form>
  );
}
