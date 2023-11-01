interface Props {
  message: string;
}

export default function InputError({ message }: Props) {
  return <p className="text-red-500 text-sm">{message}</p>;
}
