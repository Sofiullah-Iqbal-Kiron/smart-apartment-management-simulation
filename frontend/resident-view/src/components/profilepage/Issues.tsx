import { useResidentProfileData } from "../../store";
import { MdCheck, MdClose } from "react-icons/md";
import SectionHeading from "../SectionHeading";

export default function Issues() {
  const residentProfileData = useResidentProfileData(
    (state) => state.residentProfileData
  );

  return (
    <section>
      <SectionHeading text="Issues" />
      <div className="-m-1.5 overflow-x-auto">
        <div className="p-1.5 min-w-full inline-block align-middle">
          <div className="table-wrapper-immediate">
            <table>
              <thead>
                <tr>
                  <th scope="col">SI</th>
                  <th scope="col">Title</th>
                  <th scope="col">Description</th>
                  <th scope="col">Raised at</th>
                  <th scope="col">Checked by Admin</th>
                  <th scope="col">Resolved</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-700">
                {residentProfileData.issues.map((issue, idx) => (
                  <tr>
                    <td>{idx + 1}</td>
                    <td>{issue.title}</td>
                    <td>{issue.details}</td>
                    <td>{issue.raised_at}</td>
                    <td>{issue.checked ? <MdCheck /> : <MdClose />}</td>
                    <td>{issue.resolved ? <MdCheck /> : <MdClose />}</td>
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
