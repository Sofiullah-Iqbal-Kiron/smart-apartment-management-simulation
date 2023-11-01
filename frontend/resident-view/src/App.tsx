import { Navbar } from "./components/Navbar";
import { ProfilePage } from "./pages/ProfilePage";
import { Routes, Route } from "react-router-dom";
import { HomePage } from "./pages/HomePage";
import { RaiseIssuePage } from "./pages/RaiseIssuePage";
import { RequestTokenPage } from "./pages/RequestTokenPage";
import { useState } from "react";
import { PayBillPage } from "./pages/PayBillPage";

import bg from "../src/assets/bg.jpg";
import LoginPage from "./pages/LoginPage";
import { useBasicAuth } from "./store";
import axios from "axios";
import { endpoints } from "./api/endpoints";


function App() {
  const [active, setActive] = useState<number>(-1);
  const { username, password } = useBasicAuth();
  
  if (username === "" || password === "") return <LoginPage />;

  return (
    <div>
      <Navbar active={active} setActive={setActive} />

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="pay-bill" element={<PayBillPage />} />
        <Route path="request-token" element={<RequestTokenPage />} />
        <Route path="raise-issue" element={<RaiseIssuePage />} />
        <Route path="profile" element={<ProfilePage />} />
      </Routes>
    </div>
  );
}

export default App;
