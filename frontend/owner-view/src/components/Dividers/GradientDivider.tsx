import { DIVIDER_HEIGHT } from "../../constants";

export default function GradientDivider() {
  return <div className={`w-full h-[${DIVIDER_HEIGHT}] bg-gradient-to-r from-violet-500 via-sky-200 to-pink-400`} />
}
