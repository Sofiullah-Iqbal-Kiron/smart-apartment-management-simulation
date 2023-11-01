// library import
import { Link } from "react-router-dom";
import { MdOutlineHome } from "react-icons/md";
import { CgProfile } from "react-icons/cg";
import { useState } from "react";

const nav_links = [
  {
    content: "Pay Bill",
    link: "pay-bill",
    index: 0,
  },
  {
    content: "Request Token",
    link: "request-token",
    index: 1,
  },
  {
    content: "Raise Issue",
    link: "raise-issue",
    index: 2,
  },
];

interface Props {
  active: any;
  setActive: any;
}

export function Navbar({ active, setActive }: Props) {
  return (
    <div className="fixed top-0 inset-x-0 h-[3rem] sm:h-[3.5rem] z-10 bg-white/60 backdrop-blur-sm px-1 sm:px-2 flex justify-between items-center">
      <Link to="/" onClick={() => setActive(-1)}>
        <MdOutlineHome className={`text-4xl sm:text-5xl text-blue-700`} />
      </Link>

      <ul className="flex space-x-3 sm:space-x-8">
        {nav_links.map((link, idx) => (
          <li
            key={idx}
            onClick={() => setActive(link.index)}
            className={`${
              active === link.index && "text-blue-500"
            } hover:text-blue-600 transition-all duration-200`}
          >
            <Link to={link.link}>{link.content}</Link>
          </li>
        ))}
      </ul>

      <Link to="profile" onClick={() => setActive(3)}>
        <CgProfile className="text-3xl sm:text-4xl text-green-500" />
      </Link>
    </div>
  );
}
