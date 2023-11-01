import { motion } from "framer-motion";
import { SubmitHandler, useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import axios from "axios";

// local imports
import { useAuthToken, useHumanID } from "../../store";
import { InputError } from "../common/InputError";
import { endpoints } from "../../api/endpoints";

type Inputs = {
  human_id: string;
  entry_type: string;
};

export function RecordResidentForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Inputs>();

  const navigate = useNavigate();

  const cur_human_id = useHumanID((state) => state.human_id);
  const AUTH_TOKEN = useAuthToken((state) => state.AUTH_TOKEN);

  const onSubmit: SubmitHandler<Inputs> = async (data: Inputs) => {
    const post_data = {
      record_of: cur_human_id,
      record_type: data.entry_type,
    };

    const req_config = {
      headers: { Authorization: `Token ${AUTH_TOKEN}` },
    };

    axios
      .post(endpoints.create_record, post_data, req_config)
      .then((res) => {
        if (res.status === 200) {
          console.log(res.data);
          navigate("../record-success");
        } else {
          console.log("Connection damaged with status code: " + res.status);
        }
      })
      .catch((err) => console.log(err));};

    return (
      <motion.section
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
      >
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="flex flex-col space-y-8"
        >
          <legend className="text-3xl mb-8">Make a resident record</legend>

          <div className="flex flex-col space-y-1">
            <label htmlFor="human_id" className="text-lg">
              Human ID
            </label>
            <input
              type="text"
              id="human_id"
              {...register("human_id", {
                required: true,
                maxLength: {
                  value: 10,
                  message: "Human ID does not exit length 10.",
                },
              })}
              className="text-input"
              value={cur_human_id}
              contentEditable={false}
            />
            {errors.human_id?.type === "maxLength" && (
              <InputError error_message="HumanID length must be less than or equal 10." />
            )}
            {errors.human_id?.type === "required" && (
              <InputError error_message="This field is required, but here you can not edit it." />
            )}
          </div>

          <div className="flex flex-col space-y-1">
            <label htmlFor="entry_type" className="text-lg">
              Record Type
            </label>
            <select
              id="entry_type"
              {...register("entry_type")}
              defaultValue="entry"
              className="w-full rounded-md bg-gray-50"
            >
              <option value="entry">Entry</option>
              <option value="exit">Exit</option>
            </select>
          </div>

          <button type="submit" className="ghost text-lg">
            Submit
          </button>
        </form>
      </motion.section>
    );
  }