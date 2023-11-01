import { Link } from "react-router-dom";
import TOP_BLANK_SPACE from "../../constants";

function HomeIcon() {
  return (
    <svg
      width="3rem"
      height="3rem"
      viewBox="0 0 1024 1024"
      className="icon"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M981.4 502.3c-9.1 0-18.3-2.9-26-8.9L539 171.7c-15.3-11.8-36.7-11.8-52 0L70.7 493.4c-18.6 14.4-45.4 10.9-59.7-7.7-14.4-18.6-11-45.4 7.7-59.7L435 104.3c46-35.5 110.2-35.5 156.1 0L1007.5 426c18.6 14.4 22 41.1 7.7 59.7-8.5 10.9-21.1 16.6-33.8 16.6z"
        fill="#5F6379"
      />
      <path
        d="M810.4 981.3H215.7c-70.8 0-128.4-57.6-128.4-128.4V534.2c0-23.5 19.1-42.6 42.6-42.6s42.6 19.1 42.6 42.6v318.7c0 23.8 19.4 43.2 43.2 43.2h594.8c23.8 0 43.2-19.4 43.2-43.2V534.2c0-23.5 19.1-42.6 42.6-42.6s42.6 19.1 42.6 42.6v318.7c-0.1 70.8-57.7 128.4-128.5 128.4z"
        fill="#3688FF"
      />
    </svg>
  );
}

function ManIcon() {
  return (
    <svg
      version="1.0"
      id="Layer_1"
      xmlns="http://www.w3.org/2000/svg"
      width="3rem"
      height="3rem"
      viewBox="0 0 64 64"
      enableBackground="new 0 0 64 64"
    >
      <g>
        <g>
          <path
            fill="#394240"
            d="M63.329,57.781C62.954,57.219,53.892,44,31.999,44C10.112,44,1.046,57.219,0.671,57.781
           c-1.223,1.84-0.727,4.32,1.109,5.547c1.836,1.223,4.32,0.727,5.547-1.109C7.397,62.117,14.347,52,31.999,52
           c17.416,0,24.4,9.828,24.674,10.219C57.446,63.375,58.712,64,60.009,64c0.758,0,1.531-0.219,2.211-0.672
           C64.056,62.102,64.556,59.621,63.329,57.781z"
          />
          <path
            fill="#394240"
            d="M31.999,40c8.836,0,16-7.16,16-16v-8c0-8.84-7.164-16-16-16s-16,7.16-16,16v8
           C15.999,32.84,23.163,40,31.999,40z M23.999,16c0-4.418,3.586-8,8-8c4.422,0,8,3.582,8,8v8c0,4.418-3.578,8-8,8
           c-4.414,0-8-3.582-8-8V16z"
          />
        </g>
        <path
          fill="#F9EBB2"
          d="M23.999,16c0-4.418,3.586-8,8-8c4.422,0,8,3.582,8,8v8c0,4.418-3.578,8-8,8c-4.414,0-8-3.582-8-8V16z"
        />
      </g>
    </svg>
  );
}

export function Navbar() {
  return (
    <div
      className={`fixed top-0 inset-x-0 h-[${TOP_BLANK_SPACE}] shadow-md bg-white/60 backdrop-blur-md flex justify-between px-5 items-center text-xl sm:text-2xl`}
    >
      <Link to="/" className="py-2">
        <HomeIcon />
      </Link>
      <ul className="flex space-x-5">
        <li>
          <Link to="dashboard">
            <ManIcon />
          </Link>
        </li>
      </ul>
    </div>
  );
}
