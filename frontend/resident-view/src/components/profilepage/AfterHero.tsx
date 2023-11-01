import { useResidentProfileData } from "../../store";

interface CardProps {
  heading: string;
  data: string;
}

function Card({ heading, data }: CardProps) {
  return (
    <div className="p-5 flex flex-col justify-center items-center w-[18rem] h-[8rem] bg-sky-400 shadow-lg rounded-lg">
      <h1 className="text-2xl font-semibold">{heading}</h1>
      <p>{data}</p>
    </div>
  );
}

export function AfterHero() {
  const residentProfileData = useResidentProfileData(state=>state.residentProfileData)

  return (
    <section className="flex flex-col md:flex-row justify-center md:justify-evenly items-center space-y-5 md:space-y-0">
      <Card heading="Accommodation" data={`${residentProfileData.accommodation.floor} floor, Flat-${residentProfileData.accommodation.label}`} />
      <Card heading="Number of Records" data={`${residentProfileData.records.length}`} />
      <Card heading="Number of Issues" data={`${residentProfileData.issues.length}`} />
    </section>
  );
}