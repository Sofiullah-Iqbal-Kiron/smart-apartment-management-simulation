import axios from "axios";
import { useForm } from "react-hook-form";

import { endpoints } from "../api/endpoints";
import { useAuthToken } from "../store";
import { useNavigate } from "react-router-dom";

interface LoginData {
  expiry: string;
  token: string;
}

export default function () {
  const { register, handleSubmit } = useForm();
  const setAuthToken = useAuthToken(state => state.setAuthToken);
  const navigate = useNavigate();

  const onSubmit = (data: any) => {
    const req_config = {
      // 'auth' used for basic authentication
      auth: { username: data.username, password: data.password },
    };
    axios
      .post(endpoints.login, data, req_config)
      .then((res) => {
        setAuthToken(res.data.token);
        alert("Token Obtained.");
        setTimeout(() => {
          navigate("..");
        }, 500);
      })
      .catch((error) => console.log(error));
  };

  return (
    <div style={{minHeight: "100dvh"}} className="flex flex-col justify-center items-center">
      <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col space-y-5">

        <legend className="text-center font-semibold">
          <p className="text-4xl">Guard App</p>
          <p className="text-3xl">Login Required</p>
        </legend>

        <div>
          <label htmlFor="username">Username:</label>
          <input {...register("username")} id="username" type="text" className="text-input" />
        </div>

        <div>
          <label htmlFor="password">Password:</label>
          <input {...register("password")} id="password" type="password" className="text-input" />
        </div>

        <button type="submit" className="ghost">Submit</button>

      </form>
    </div>
  );
}
