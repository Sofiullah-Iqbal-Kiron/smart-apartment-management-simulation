import { Link } from "react-router-dom";
import { useAuthToken } from "../store";

function BackendConnected() {
  return <p className="text-sm font-mono text-green-600">Backend Connected.</p>;
}

function BackendNotConnected() {
  return (
    <p className="text-sm font-mono text-red-600">
      Backend Disconnected, <Link to='login/' className='italic underline underline-offset-4'>login first</Link>.
    </p>
  );
}

export const GuardHome = () => {
  const AUTH_TOKEN = useAuthToken((state) => state.AUTH_TOKEN);

  return (
    <div className="flex flex-col justify-center items-center space-y-2">
      <Link to="make-record/verify-id/" className="ghost w-full uppercase">
        make record
      </Link>
      <Link to="register-guest/" className="ghost w-full uppercase">
        register guest
      </Link>

      <div className="fixed bottom-[3rem] inset-x-0 text-center">
        {AUTH_TOKEN && <BackendConnected />}
        {!AUTH_TOKEN && <BackendNotConnected />}
      </div>
    </div>
  );
};
