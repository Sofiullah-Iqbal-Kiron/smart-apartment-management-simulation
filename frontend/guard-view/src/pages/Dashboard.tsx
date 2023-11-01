import {PrimaryInfo} from "../components/Dashboard/PrimaryInfo";
import {Achievements} from "../components/Dashboard/Achievements";
import {RecordsTable} from "../components/Dashboard/RecordsTable";
import { useQuery } from "react-query";
import axios from "axios";
import { endpoints } from "../api/endpoints";
import { useGuardData, useAuthToken } from "../store";

export function Dashboard() {
    const setGuardData = useGuardData((state) => state.setGuardData);
    const AUTH_TOKEN = useAuthToken((state) => state.AUTH_TOKEN);

    const getGuardProfileData = () => {
      const req_config = {
        headers: { Authorization: `Token ${AUTH_TOKEN}` },
      };
      axios
        .get(endpoints.guard_profile, req_config)
        .then((res) => setGuardData(res.data))
        .catch((err) => console.log(err));
    };

    useQuery({
      queryKey: ["guard-profile-data"],
      queryFn: getGuardProfileData,
    });

    return (
        <section className="w-full flex flex-col space-y-12">
            <div className='h-[100vh]'/>
            <PrimaryInfo/>
            <Achievements/>
            <RecordsTable/>
        </section>
    );
}
