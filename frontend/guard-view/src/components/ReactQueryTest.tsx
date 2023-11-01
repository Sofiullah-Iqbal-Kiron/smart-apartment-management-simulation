import {useQuery} from "react-query";
import axios from "axios";

export function ReactQueryTest() {
    const {isLoading, error, data} = useQuery("demoData", () =>
        fetch('https://jsonplaceholder.typicode.com/todos/1').then(res => res.json())
    )

    if (isLoading) return <h1>Loading...</h1>
    if (error) return <h1>error</h1>

    return (
        <>
            here is the data:
            <h1>{data.userId}{data.title}</h1>
        </>
    )
}