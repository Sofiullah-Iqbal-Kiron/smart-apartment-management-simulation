interface Props {
  what: string;
  data: string;
}

export function Card({ what, data }: Props) {
  return (
    <div className="min-w-[10rem] min-h-[6rem] flex flex-col justify-center items-center text-center border border-cyan-200 rounded-md shadow-md p-2">
      <h2 className="text-3xl text-gray-800 font-mono">{data}</h2>
      <p className="text-gray-600">{what}</p>
    </div>
  );
}
