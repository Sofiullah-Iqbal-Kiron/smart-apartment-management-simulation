import {motion} from 'framer-motion'

// show all data that has been recorder at server

export function RecordSuccessMessage() {
    return (
        <motion.section
            initial={{opacity: 0, scale: 0.1}}
            animate={{opacity: 1, scale: 1}}
            transition={{type: 'spring', bounce: 0.7, duration: 1}}

            className='flex flex-col justify-center items-center text-center'>
            <p className='text-2xl md:text-3xl lg:text-5xl text-violet-700 font-semibold'>
                Successfully Recorded.
            </p>
            <svg width="1" height="1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"
                 className="w-[5rem] h-[5rem]">
                <path fill="#22c55e"
                      d="M.41 13.41L6 19l1.41-1.42L1.83 12m20.41-6.42L11.66 16.17L7.5 12l-1.43 1.41L11.66 19l12-12M18 7l-1.41-1.42l-6.35 6.35l1.42 1.41L18 7Z"/>
            </svg>
        </motion.section>
    )
}