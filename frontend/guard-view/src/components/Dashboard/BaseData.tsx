import { useGuardData } from "../../store";

export function BaseData() {
  const guard = useGuardData((state) => state.guard);

  return (
    <table id="base-data-table">
      <tbody>
        <tr>
          <td>Name</td>
          <td>{guard.human.user.fullname === ''? 'Name empty.' : guard.human.user.fullname}</td>
        </tr>
        <tr>
          <td>Date of birth</td>
          <td>{guard.human.date_of_birth}</td>
        </tr>
        <tr>
          <td>Joined</td>
          <td>{guard.human.user.since}</td>
        </tr>
      </tbody>
    </table>
  );
}
