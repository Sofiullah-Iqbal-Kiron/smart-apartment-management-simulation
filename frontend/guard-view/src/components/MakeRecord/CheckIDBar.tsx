import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { SubmitHandler, useForm } from "react-hook-form";
import { motion } from "framer-motion";
import axios from "axios";

import { useAuthToken, useHumanID } from "../../store";
import { endpoints } from "../../api/endpoints";

type HumanID = {
  human_id: string;
};

export function CheckIDBar() {
  const [idStatus, setIdStatus] = useState("Not verified yet.");
  const navigate = useNavigate();

  const { human_id, setHumanID } = useHumanID();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<HumanID>();

  const AUTH_TOKEN = useAuthToken(state => state.AUTH_TOKEN);

  const onSubmit: SubmitHandler<HumanID> = async (data: HumanID) => {
    setHumanID(data.human_id);

    // here, useQuery, and page loading until checking is success.
    const config = { headers: { Authorization: `Token ${AUTH_TOKEN}` } };
    axios.get(`${endpoints.check_id}${data.human_id}/`, config).then((res) => {
      if (res.data.exists) {
        setIdStatus("Verified.");

        if (data.human_id.startsWith("RS-")) {
          navigate("../record-resident");
        } else if (data.human_id.startsWith("GS-")) {
          navigate("../record-guest");
        }
      } else {
        console.log(res.data);
        navigate("../invalid-id");
      }
    });
  };

  // framer-motion animation variants
  const littleFadeIn = {
    from: { opacity: 0, y: 20 },
    to: { opacity: 1, y: 0 },
  };

  return (
    <motion.section
      initial="from"
      animate="to"
      transition={{ duration: 0.5 }}
      variants={littleFadeIn}
      className="flex flex-col space-y-8 text-center"
    >
      <h3 className="text-2xl">Insert Human ID:</h3>

      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex flex-col space-y-2 m-auto"
      >
        <input
          type="text"
          placeholder="RS-EXAMPLE"
          {...register("human_id")}
          autoFocus={true}
          className="text-input"
        />
        <button type="submit" className="ghost">
          Check ID
        </button>
      </form>

      <p className="">{idStatus}</p>
    </motion.section>
  );
}
