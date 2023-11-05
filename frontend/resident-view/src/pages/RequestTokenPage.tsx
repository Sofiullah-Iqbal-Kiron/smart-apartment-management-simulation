import {useForm} from "react-hook-form";
import {useState} from "react";
import {ReturnInfoCard} from "../components/ReturnInfoCard";
import axios from "axios";
import { endpoints } from "../api/endpoints";
import { useBasicAuth } from "../store";

interface TokenData {
  token_key: string;
  number_of_allowed_guests: number;
  used: boolean;
  valid_till: string;
}

let tokenData: TokenData = {token_key: "demo_key", number_of_allowed_guests: 0, used: false, valid_till: "no_date"}

export function RequestTokenPage() {
    const {register, handleSubmit} = useForm()

    const [token, setToken] = useState('demo token')
    const [remains, setRemains] = useState('demo remains 3 guests')
    const [reducer_clock, setReducerClock] = useState('demo 3 minutes 3 seconds remains.')
    const [data_returned, setDataReturned] = useState<boolean>(false)

    const { username, password } = useBasicAuth();

    const onSubmit = (data: any) => {
      const number_of_allowed_guests = parseInt(data.number_of_allowed_guests);
      axios
        .post(
          endpoints.sought_token,
          { number_of_allowed_guests: number_of_allowed_guests },
          { auth: { username: username, password: password } }
        )
        .then((res) => {tokenData = res.data; setDataReturned(true);})
        .catch((err) => console.log(err));
    };

    return (
        <section className='min-h-screen flex flex-col justify-center items-center space-y-5'>
            <h1 className='header-1'>Request a token</h1>

            <form onSubmit={handleSubmit(onSubmit)} className='w-2/3 sm:w-1/2 flex flex-col justify-center items-center space-y-4'>
                <div className='flex space-x-4 justify-center items-center'>
                    <label>For</label>
                    <input type='number'
                           min={1}
                           max={50}
                           {...register('number_of_allowed_guests')}
                           className='form-input w-1/3 rounded px-2 py-1'/>
                    <label>guests.</label>
                </div>
                <p className='italic'>Max 50 guests allowed at a time.</p>
                <button type='submit' className='btn-ghost'>Seek token</button>
            </form>

            {
                data_returned &&
                <div className="p-4 border rounded-lg shadow-md">
                    <p><span className="font-semibold">Token</span> {tokenData.token_key}</p>
                    <p><span className="font-semibold">Number of allowed guests</span> {tokenData.number_of_allowed_guests}</p>
                    <p>{tokenData.used?"Token used.":"Token not used yet."}</p>
                    <p><span className="font-semibold">Valid till</span> {tokenData.valid_till}</p>
                </div>
            }

            {/* {
                data_returned &&
                <div className='flex flex-col justify-center items-center'>
                    <h1 className='header-1'>Returned</h1>
                    <div id='infos' className='flex flex-col sm:flex-row space-x-0 sm:space-x-4 space-y-4 sm:space-y-0'>
                        <ReturnInfoCard title='Token' data={token}/>
                        <ReturnInfoCard title='Remains' data={remains}/>
                        <ReturnInfoCard title='Valid till' data={reducer_clock}/>
                    </div>
                </div>
            } */}
        </section>
    )
}