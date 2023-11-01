interface Props {
  error_message: string;
}

export function InputError({ error_message }: Props) {
  return (
    <p className="text-sm text-center text-red-600 font-light">
      {error_message}
    </p>
  );
}
