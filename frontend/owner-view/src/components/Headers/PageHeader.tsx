interface Props {
  text: string;
}

export default function PageHeader({ text }: Props) {
  return <h1 className="text-5xl text-center py-5">{text}</h1>;
}
