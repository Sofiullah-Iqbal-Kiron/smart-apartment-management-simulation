import {UserIcon} from "./icons/UserIcon";
import {LockIcon} from "./icons/LockIcon";
import {AtIcon} from "./icons/AtIcon";

import {SubmitHandler, useForm} from "react-hook-form";

export function Form() {
    const {
        register,
        handleSubmit,
        watch,
        formState: {errors}
    } = useForm();

    const onSubmit = (data: any) => alert(JSON.stringify(data));

    return (
        <div id='form-holder'>
            <form method='POST'
                  id='the-form'
                  onSubmit={handleSubmit(onSubmit)}
            >
                <legend id='the-legend'>
                    Dear Resident<br/>Please Login First
                </legend>

                <div className='input-div'>
                    <label htmlFor='username'>
                        <UserIcon/>
                    </label>
                    <input type='text' {...register("username", {required: true})} id='username' placeholder='username'
                           className='input-field'/>
                </div>

                <div className='input-div'>
                    <label htmlFor='human-id'>
                        <AtIcon/>
                    </label>
                    <input type='text' {...register("human-id")} id='human-id' placeholder='human id'
                           className='input-field'/>
                </div>

                <div className='input-div'>
                    <label htmlFor='passo'>
                        <LockIcon/>
                    </label>
                    <input type='password' {...register("passo")} id='passo' placeholder='password'
                           className='input-field'/>
                </div>

                <div className='h-[0.5rem]'/>
                <button type='submit' className='btn-primary w-full'>Login</button>

                <p className='text-sm text-gray-400'>Not registered yet? then
                    <a href='#register' className='text-yellow-300'>register</a>
                </p>
            </form>
        </div>
    )
}