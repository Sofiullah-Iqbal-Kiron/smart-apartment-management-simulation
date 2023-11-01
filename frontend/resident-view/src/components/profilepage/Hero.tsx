import { useResidentProfileData } from "../../store";
import Divider from "../Divider";

interface Props {
  rs_id: string;
  username: string;
  fullname?: string;
  accommodation?: string;
  since?: any;
  avatar_link?: string;
}

interface BasicInfoProps {
  heading: string;
  data: string;
}

function BasicInfoCard({ heading, data }: BasicInfoProps) {
  return (
    <div className="w-full flex justify-between px-3 py-1 bg-green-100 text-gray-950 text-sm rounded-sm shadow-md">
      <h4>{heading}</h4>
      <p>{data}</p>
    </div>
  );
}

export function Hero({rs_id = "RS-none", fullname = "No name", accommodation = "Not found", since = "unknown", avatar_link = "#",}: Props) {
  const residentProfileData = useResidentProfileData(state=>state.residentProfileData)

  return (
    <section className="my-2">
      <div id="avatar-portion">
        <img src={avatar_link} alt={fullname} width={150} height={150} className="rounded-xl ring-2 ring-offset-2 ring-violet-500" />
        <p className="text-lg font-mono">{rs_id}</p>
      </div>

      <Divider/>

      <div className="text-center flex flex-col justify-center items-center space-y-1.5">
        <h2 className="text-2xl capitalize">{fullname || "fullname not found"}</h2>
        <BasicInfoCard heading="Resident since" data={residentProfileData.human.user.since}/>
        <BasicInfoCard heading="Date of birth" data={residentProfileData.human.date_of_birth}/>
        <BasicInfoCard heading="Gender" data={residentProfileData.human.gender.charAt(0).toUpperCase()+residentProfileData.human.gender.slice(1)}/>
        <BasicInfoCard heading="Contact" data={residentProfileData.human.contact}/>
        <BasicInfoCard heading="Email" data={residentProfileData.human.user.email || "email_empty"}/>
        <BasicInfoCard heading="NID or BR" data={residentProfileData.human.nid_or_br}/>
      </div>

      <Divider/>

    </section>
  );
}
