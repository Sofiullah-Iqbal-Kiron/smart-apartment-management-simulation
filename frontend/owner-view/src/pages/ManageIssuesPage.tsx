// Manage, Handle issues raised by Residents.

import { useIssues } from "../api/calls";
import FetchingError from "../components/FetchingError";
import LoadingIndicator from "../components/LoadingIndicator";

// list issues, check issues that are seen, resolved.

export default function ManageIssuesPage() {
  const { data, isError, isLoading } = useIssues();

  if (isLoading) return <LoadingIndicator />;
  if (isError) return <FetchingError text="Issues fetching error." />;

  return (
    <div style={{ minHeight: "100svh" }} className="w-full">
      <ul>
        {data.map((issue, idx)=><li key={idx}>{issue.title}</li>)}
      </ul>
    </div>
  );
}
