// Manage, Handle issues raised by Residents.

import { useIssues } from "../api/calls";
import FetchingError from "../components/FetchingError";
import LoadingIndicator from "../components/LoadingIndicator";

// list issues, check issues that are seen, resolved.

export default function ManageIssuesPage() {
  const { data, isError, isLoading } = useIssues();

  if (isError) return <FetchingError text="Issues fetching error." />;
  if (isLoading) return <LoadingIndicator />;

  return (
    <div style={{ minHeight: "100svh" }} className="w-full">
      ManageIssuesPage
    </div>
  );
}
