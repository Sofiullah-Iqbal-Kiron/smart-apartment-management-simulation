import {BaseData} from "./BaseData";
import {useGuardData} from "../../store";
import {BottomNav} from "./BottomNav";

export function PrimaryInfo() {
    const guard = useGuardData(state => state.guard)

    return (
        <div className="py-3 flex flex-col sm:flex-row space-y-3 sm:space-y-0 w-full justify-center sm:justify-evenly items-center">
            <div className="text-center flex flex-col space-y-2">
                <img
                    src={guard.human.avatar}
                    alt="avatar"
                    width={130}
                    height={130}
                    className="ring-2 ring-offset-2 rounded-3xl"
                />
                <p className="text-lg font-semibold">{guard.guard_id}</p>
            </div>

            <BaseData/>
        </div>
    );
}