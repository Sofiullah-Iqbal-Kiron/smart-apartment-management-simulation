import {Link} from "react-router-dom";

import {RxAvatar} from "react-icons/rx";
import {CiViewTable} from "react-icons/ci";
import {SiTableau} from "react-icons/si";

const navlinks = [
    {
        content: <RxAvatar/>,
        hover_data: 'You',
        link: 'primary-info'
    },
    {
        content: <SiTableau/>,
        hover_data: 'Achievements',
        link: 'achievements'
    },
    {
        content: <CiViewTable/>,
        hover_data: 'Records',
        link: 'your-records'
    },
]

export function BottomNav() {
    return (
        <ul className='flex justify-around items-center w-full py-3 bg-sky-300'>
            {navlinks.map((nl, idx) =>
                <li key={idx} className={`text-4xl`}>
                    <Link to={nl.link}>{nl.content}</Link>
                </li>
            )}
        </ul>
    );
}