interface Props {
  text: string;
}

export default function SectionHeading({ text }: Props) {
  return <h1 className="text-3xl text-center mb-2">{text}</h1>;
}
