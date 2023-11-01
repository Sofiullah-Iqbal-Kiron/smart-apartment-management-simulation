// import { Record } from "../store";

import { useGuardData } from "../../store";

export function RecordsTable() {
  const guard = useGuardData((state) => state.guard);
  const records = guard.records;

  return (
    <section className="overflow-x-auto border p-2 w-full flex flex-col justify-center items-center shadow-sm">
      <h1 className="text-center text-2xl font-semibold mb-5">Records Created</h1>
      <table id="records-table">
        <thead>
          <tr className="bg-cyan-100">
            <th>SN</th>
            <th>Human ID</th>
            <th>Type</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {records.map((record, idx) => (
            <tr key={idx}>
              <td>{idx+1}</td>
              <td>{record.record_of}</td>
              <td><span className={`${record.record_type === 'entry'? 'bg-green-500' : 'bg-red-500'} px-2 py-1 rounded-2xl`}>{record.record_type}</span></td>
              <td>{record.recorded_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
