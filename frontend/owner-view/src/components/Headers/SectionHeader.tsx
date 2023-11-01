interface Props {
  text: string;
}

export default function SectionHeader({ text }: Props) {
  return <h2 className="text-3xl text-center py-3">{text}</h2>;
}
