import {Form} from "./components/Form";
import background from '../src/assets/background.jpg';

function App() {
    return (
        <div style={{backgroundImage: `url(${background})`}}
             className='bg-cover h-screen flex flex-col justify-center items-center space-y-3'>
            <Form/>
        </div>
    )
}

export default App
