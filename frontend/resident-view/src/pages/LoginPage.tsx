import axios from "axios";
import { useForm } from "react-hook-form";
import { endpoints } from "../api/endpoints";
import { useBasicAuth } from "../store";

export default function LoginPage() {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const setAuth = useBasicAuth(state => state.setAuth);

  const onSubmit = (data: any) => {
    axios
      .post(endpoints.basic_auth, data)
      .then(
        (res) => res.data.is_authenticated && setAuth(data)
      )
      .catch((err) => {
        alert("Request refused from backend. Inspect page and look at the console for more.");
        console.log(err);
      });
  };

  return (
    <div className="h-screen w-screen flex flex-col justify-center items-center">
      <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col space-y-5 bg-gradient-to-br from-rose-300 to-cyan-300 p-10 rounded-xl">
        <legend className="text-center font-semibold">
          <p className="text-4xl">Resident App</p>
          <p className="text-3xl">Login Required</p>
        </legend>

        <div className="flex flex-col justify-center items- space-y-1">
          <label htmlFor="username-login-field">Username:</label>
          <input id="username-login-field" type="text" {...register("username")} className="input-text" />
        </div>

        <div className="flex flex-col justify-center items-start space-y-1">
          <label htmlFor="password-login-field">Password:</label>
          <input id="password-login-field" type="password" {...register("password")} className="input-text" />
        </div>

        <div className="flex flex-row justify-center items-center">
          <button type="submit" className="btn-secondary">Login</button>
        </div>
      </form>
    </div>
  );
}
