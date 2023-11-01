import { Link } from "react-router-dom";
import TopBlank from "../components/TopBlank";
import Divider from "../components/Divider";
import LoginModal from "../components/LoginModal";

export function HomePage() {
  return (
    <section className="text-center text-xl min-h-screen">
      <TopBlank/>

      <h1 className="text-6xl font-serif font-bold py-5">Hello and Welcome!</h1>
      <p className="text-2xl px-2 md:px-10 text-center">
        Welcome to our smart apartment management simulation system. Just smartly handle issues
        without ever leaving your relax mood.
      </p>

      <div className="flex flex-col space-y-8 mx-6 mt-20 mb-16">
        <h2 className="text-4xl font-bold">Actions</h2>
        <Link to="pay-bill" className="action-card">
          <h3>Pay Bills</h3>
          <p>Pay home rent and other utility bills.</p>
        </Link>
        <Link to="request-token" className="action-card">
          <h3>Seek Token</h3>
          <p>Request for a temporary token to register your guests.</p>
        </Link>
        <Link to="raise-issue" className="action-card">
          <h3>Submit an Issue</h3>
          <p>Any hassle? Let us know by submitting an issue.</p>
        </Link>
        <Link to="profile" className="action-card">
          <h3>See Your Profile</h3>
          <p>View, edit, organize your profile and connect social accounts to reveal your lifestyle.</p>
        </Link>
      </div>
    </section>
  );
}
