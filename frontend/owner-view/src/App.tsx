import Topnav from "./components/Topnav";
import IndexPage from "./pages/IndexPage";
import ManageIssuesPage from "./pages/ManageIssuesPage";
import { useTheme } from "./store";

export default function App() {
  const currTheme = useTheme((state) => state.theme);
  
  return (
    <div data-theme={`${currTheme}`}>
      <Topnav />
      <IndexPage />
    </div>
  );
}
