import { useForm } from "react-hook-form";
import axios from "axios";

import InputError from "../components/InputError";
import { endpoints } from "../api/endpoints";
import { useBasicAuth } from "../store";
import { useNavigate } from "react-router-dom";

interface Issue {
  title: string;
  details: string;
  emergency: boolean;
}

export function RaiseIssuePage() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();
  const {username, password} = useBasicAuth();
  const navigate = useNavigate();

  const onSubmit = (data: any) => {
    axios
      .post(endpoints.submit_issue, data, {
        auth: { username: username, password: password },
      })
      .then((res) => {
        alert("Issue created successfully.");
        navigate("/");
      })
      .catch((errors) => {
        alert(errors);
        console.log(errors);
      });
  };

  return (
    <section className="flex flex-col justify-center items-center min-h-screen">
      <h1 className="header-1">Submit an Issue</h1>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex flex-col space-y-4 w-[80%] sm:w-1/3 lg:w-1/4"
      >
        <div className="flex flex-col space-y-1">
          <label htmlFor="title" className="text-xl">
            Title:
          </label>
          <input
            type="text"
            {...register("title", {required:true})}
            id="title"
            className="input-text"
          />
          {errors.title?.type === 'required' && <InputError message="Title is required."/>}
        </div>

        <div className="flex flex-col space-y-1">
          <label htmlFor="details" className="text-xl">
            Description:
          </label>
          <textarea
            {...register("details", {required:true, minLength:20})}
            id="details"
            className="input-text h-[7rem]"
          />
          {errors.details?.type === 'required' && <InputError message="Description is also required."/>}
          {errors.details?.type === 'minLength' && <InputError message="Description must be least 20 characters long."/>}
        </div>

        <div className="flex items-center">
          <input
            type="checkbox"
            className="form-checkbox"
            {...register("emergency")}
            id="emergency"
          />
          <label htmlFor="emergency" className="text-md ml-3">
            Emergency
          </label>
        </div>

        <button type="submit" className="w-full btn-ghost">
          Submit
        </button>
      </form>
    </section>
  );
}
