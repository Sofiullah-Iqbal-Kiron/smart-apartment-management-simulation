interface Props {
  text?: string;
}

export default function FetchingError({ text }: Props) {
  return <div className="text-red-500">FetchingError: {text}</div>;
}
