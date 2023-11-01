import ThemeChanger from "./ThemeChanger";

export default function Topnav() {
  return (
    <div className="navbar shadow-2xl flex flex-row justify-between items-center">
      <h1>Owner</h1>
      <ThemeChanger />
    </div>
  );
}
