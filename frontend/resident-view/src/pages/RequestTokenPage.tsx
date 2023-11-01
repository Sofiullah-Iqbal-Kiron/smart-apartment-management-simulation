import {useForm} from "react-hook-form";
import {useState} from "react";
import {ReturnInfoCard} from "../components/ReturnInfoCard";

export function RequestTokenPage() {
    const {register, handleSubmit} = useForm()

    const [token, setToken] = useState('demo token')
    const [remains, setRemains] = useState('demo remains 3 guests')
    const [reducer_clock, setReducerClock] = useState('demo 3 minutes 3 seconds remains.')
    const [data_returned, setDataReturned] = useState<boolean>(false)

    return (
        <section className='min-h-screen flex flex-col justify-center items-center'>
            <h1 className='header-1'>Request a token</h1>
            <form className='w-2/3 sm:w-1/2 flex flex-col justify-center items-center space-y-4'>
                <div className='flex space-x-4 justify-center items-center'>
                    <label>For</label>
                    <input type='number'
                           min={1}
                           max={50}
                           {...register('number_of_allowed_guests')}
                           className='form-input w-1/3 rounded px-2 py-1'/>
                    <label>guests.</label>
                </div>
                <p className='italic'>
                    Max 50 guests allowed at a time.
                </p>
                <button type='submit' className='btn-ghost'>Seek token</button>
            </form>
            {
                data_returned &&
                <div className='flex flex-col justify-center items-center'>
                    <h1 className='header-1'>Returned</h1>
                    <div id='infos' className='flex flex-col sm:flex-row space-x-0 sm:space-x-4 space-y-4 sm:space-y-0'>
                        <ReturnInfoCard title='Token' data={token}/>
                        <ReturnInfoCard title='Remains' data={remains}/>
                        <ReturnInfoCard title='Valid till' data={reducer_clock}/>
                    </div>
                </div>
            }
        </section>
    )
}