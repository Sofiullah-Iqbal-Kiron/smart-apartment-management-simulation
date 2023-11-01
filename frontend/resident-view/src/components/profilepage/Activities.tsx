import { useResidentProfileData } from "../../store";
import { MdCheck, MdClose } from "react-icons/md";
import SectionHeading from "../SectionHeading";

export function Activities() {
  const residentProfileData = useResidentProfileData(
    (state) => state.residentProfileData
  );

  return (
    <section>
      <SectionHeading text="Activities" />
      <div className="-m-1.5 overflow-x-auto">
        <div className="p-1.5 min-w-full inline-block align-middle">
          <div className="table-wrapper-immediate">
            <table>
              <thead>
                <tr>
                  <th scope="col">SI</th>
                  <th scope="col">Type</th>
                  <th scope="col">Timestamp</th>
                  <th scope="col">Recorder</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-700">
                {residentProfileData.records.map((record, idx) => (
                  <tr>
                    <td>{idx + 1}</td>
                    <td>{record.record_type.charAt(0).toUpperCase() + record.record_type.slice(1)}</td>
                    <td>{record.recorded_at}</td>
                    <td>{record.recorded_by}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
  );
}
