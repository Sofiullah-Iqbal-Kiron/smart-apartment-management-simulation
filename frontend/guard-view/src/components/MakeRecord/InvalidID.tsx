import {motion} from "framer-motion";

export function InvalidID() {
    return (
        <motion.p
            initial={{y: "100vh", opacity: 0}}
            animate={{y: 0, opacity: 1}}
            transition={{ease: "easeInOut", duration: 2, type: 'spring'}}
            className='text-7xl text-center text-red-600 font-bold uppercase'>

            Ups! Invalid ID.
        </motion.p>
    )
}