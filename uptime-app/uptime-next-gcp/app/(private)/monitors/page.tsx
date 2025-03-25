// app/(private)/monitors/page.tsx

"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { useLoginRequiredClient } from "@/app/lib/useLoginRequiredClient";
import { MonitorsI } from "@/app/types/monitorsI";

export default function Dashboard() {
  const { session, status } = useLoginRequiredClient();
  const [monitors, setMonitors] = useState<MonitorsI[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {

      try {
        const apiUrl = `/monitors/api-get-monitors`;
        console.log("dashboard · Fetching monitors from:", apiUrl);
        const response = await fetch(apiUrl);
        const data = await response.json();

        if (response.ok) {
          setMonitors(data.data);
        } else {
          setError(data.message || "Failed to fetch monitors");
        }
      } catch (error) {
        console.error("dashboard · Error fetching:", error);
        setError("An error occurred while fetching monitors.");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <div className="main_box">
      <h1>Monitors</h1>

      <p>
      <Link href="/monitors/add-monitor">Add Monitor</Link>
      </p>

      {monitors.length > 0 ? (
        <table className="generic-table">
          <thead>
            <tr>
              <th><span>Status</span></th>
              <th><span>Title</span></th>
              <th><span>What</span></th>
              <th><span>Last checked</span></th>
              <th><span>Actions</span></th>
            </tr>
          </thead>
          <tbody>
            {monitors.map((monitor) => (
              <tr key={monitor.monitor_id}>
               <td>
                <span>
                  {monitor.is_offline === null ? (
                    "⚪" // White circle for unknown
                  ) : monitor.is_offline ? (
                    "🔴" // Red circle for offline
                  ) : (
                    "🟢" // Green circle for online
                  )}
                  </span>
               </td>
                <td><span>{monitor.title}</span></td>
                <td><span>{monitor.what_to_monitor}</span></td>
                <td>
                  <span>
                    {monitor.last_checked_datetime
                    ? new Date(monitor.last_checked_datetime)
                        .toLocaleString("en-GB", {
                          day: "2-digit",
                          month: "short",
                          year: "numeric",
                          hour: "2-digit",
                          minute: "2-digit",
                          hour12: false,
                        })
                        .replace(",", "") // Removes the comma
                    : "N/A"}
                  </span>
                </td>
                <td>
                  <span>
                  <Link href={`/monitors/${monitor.monitor_id}/edit-monitor`}>Edit</Link>
                  &nbsp;&middot;&nbsp;
                  <Link href={`/monitors/${monitor.monitor_id}/delete-monitor`}>Delete</Link>
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No monitors found.</p>
      )}
    </div>
  );
}
