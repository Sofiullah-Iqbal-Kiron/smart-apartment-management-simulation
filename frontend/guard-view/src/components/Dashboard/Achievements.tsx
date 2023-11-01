import {Card} from "./Card";
import {useGuardData} from "../../store";

export function Achievements() {
    const guard = useGuardData(state => state.guard)
    return (
        <div className="w-full flex flex-row justify-around sm:justify-center sm:space-x-5 items-center flex-wrap ">
            <Card what="Salary" data={`${guard.salary}`}/>
            <Card what="Records Created" data={`${guard.records.length}`}/>
        </div>
    );
}