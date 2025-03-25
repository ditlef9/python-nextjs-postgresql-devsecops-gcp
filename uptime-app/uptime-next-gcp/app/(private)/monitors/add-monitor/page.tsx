// app/(private)/monitors/add-monitor/page.tsx

"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function AddMonitor() {
  const [title, setTitle] = useState("");
  const [whatToMonitor, setWhatToMonitor] = useState<"URL becomes unavailable">("URL becomes unavailable");
  const [urlToMonitor, setUrlToMonitor] = useState("");
  const [escalationEmailOn, setEscalationEmailOn] = useState(false);
  const [escalationEmailTo, setEscalationEmailTo] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError(null);

    const monitorData = {
      title,
      what_to_monitor: whatToMonitor,
      url_to_monitor: urlToMonitor,
      escalation_email_on: escalationEmailOn,
      escalation_email_to: escalationEmailTo
    };

    try {
      const response = await fetch("/monitors/add-monitor/api-add-monitor", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(monitorData),
      });

      if (!response.ok) {
        throw new Error("Failed to add monitor");
      }

      router.push("/monitors"); // Redirect to the dashboard page on success
    } catch (error) {
      console.error(error);
      setError("An error occurred while adding the monitor.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="main_box">
      <h1>Add Monitor</h1>
      {error && <p className="error">{error}</p>}

      <form onSubmit={handleSubmit}>
        <p>
          <label htmlFor="title">Title</label><br />
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            autoFocus
            style={{ width: "99%" }}
          />
        </p>

        <p>
          <label htmlFor="whatToMonitor">What to Monitor</label><br />
          <select id="whatToMonitor" value={whatToMonitor} onChange={(e) => setWhatToMonitor(e.target.value as "URL becomes unavailable")}>
            <option value="URL becomes unavailable">URL becomes unavailable</option>
          </select>
        </p>

        <p>
          <label htmlFor="urlToMonitor">URL to Monitor</label><br />
          <input
            type="text"
            id="urlToMonitor"
            value={urlToMonitor}
            onChange={(e) => setUrlToMonitor(e.target.value)}
            required
            style={{ width: "99%" }}
          />
        </p>

        <p>
          <label htmlFor="escalationEmailOn">Escalation Email On</label><br />
          <input
            type="checkbox"
            id="escalationEmailOn"
            checked={escalationEmailOn}
            onChange={(e) => setEscalationEmailOn(e.target.checked)}
          />
        </p>

        {escalationEmailOn && (
          <p>
            <label htmlFor="escalationEmailTo">Escalation Email To</label><br />
            <input
              type="email"
              id="escalationEmailTo"
              value={escalationEmailTo}
              onChange={(e) => setEscalationEmailTo(e.target.value)}
              required
              style={{ width: "99%" }}
            />
          </p>
        )}


        <p>
        <button type="submit" disabled={loading}>
          {loading ? "Adding Monitor..." : "Add Monitor"}
        </button>
        </p>
      </form>
    </div>
  );
}
