import { GuardHome } from "./pages/GuardHome";
import { CheckIDBar } from "./components/MakeRecord/CheckIDBar";
import { Route, Routes } from "react-router-dom";
import { GuestRegistrationForm } from "./components/RegisterGuest/GuestRegistrationForm";
import { Dashboard } from "./pages/Dashboard";
import { InvalidID } from "./components/MakeRecord/InvalidID";
import { RecordGuestForm } from "./components/MakeRecord/RecordGuestForm";
import { RecordResidentForm } from "./components/MakeRecord/RecordResidentForm";
import { ReactQueryTest } from "./components/ReactQueryTest";
import { Navbar } from "./components/common/Navbar";
import { RecordSuccessMessage } from "./components/MakeRecord/RecordSuccessMessage";
import Login from "./pages/Login";
import { useAuthToken } from "./store";

function App() {
  const AUTH_TOKEN = useAuthToken(state=>state.AUTH_TOKEN)

  if(!AUTH_TOKEN) return <Login/>

  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <Navbar />

      <Routes>
        <Route path="/" element={<GuardHome />} />

        <Route path="make-record">
          <Route path="verify-id" element={<CheckIDBar />} />
          <Route path="record-resident" element={<RecordResidentForm />} />
          <Route path="record-guest" element={<RecordGuestForm />} />
          <Route path="record-success" element={<RecordSuccessMessage />} />
          <Route path="invalid-id" element={<InvalidID />} />
        </Route>

        <Route path="register-guest/" element={<GuestRegistrationForm />} />
        <Route path="dashboard" element={<Dashboard />} />

        <Route path="test/" element={<ReactQueryTest />} />
      </Routes>
    </div>
  );
}

export default App;
