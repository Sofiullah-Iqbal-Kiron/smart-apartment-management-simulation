interface Props {
  text: string;
}

export default function SubSectionHeader({ text }: Props) {
  return <h3 className="text-2xl text-center py-2">{text}</h3>;
}
