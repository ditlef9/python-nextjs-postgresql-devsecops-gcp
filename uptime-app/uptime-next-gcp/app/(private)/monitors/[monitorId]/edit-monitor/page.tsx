// app/(private)/monitors/[monitorId]/edit-monitor/page.tsx

"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useParams } from "next/navigation"; // Import the `useParams` hook

export default function EditMonitor() {
  const { monitorId } = useParams(); // Get the monitorId from the route params
  const [monitor, setMonitor] = useState<any | null>(null); // Monitor data
  const [title, setTitle] = useState("");
  const [whatToMonitor, setWhatToMonitor] = useState<"URL becomes unavailable">("URL becomes unavailable");
  const [urlToMonitor, setUrlToMonitor] = useState("");
  const [escalationEmailOn, setEscalationEmailOn] = useState(false);
  const [escalationEmailTo, setEscalationEmailTo] = useState("");
  const [loading, setLoading] = useState(false);
  
  const [feedbackMessage, setFeedbackMessage] = useState('');
  const [feedbackType, setFeedbackType] = useState('');
  

  const router = useRouter(); // ???

  useEffect(() => {
    if (!monitorId) return; // If monitorId is not available, don't attempt to fetch data

    const fetchMonitorData = async () => {
      try {
        const response = await fetch(`/monitors/${monitorId}/api-get-monitor`);
        if (response.ok) {
          const json = await response.json();
          setMonitor(json.data);
          setTitle(json.data.title);
          setWhatToMonitor(json.data.what_to_monitor);
          setUrlToMonitor(json.data.url_to_monitor);
          setEscalationEmailOn(json.data.escalation_email_on);
          setEscalationEmailTo(json.data.escalation_email_to);
        } else {
          setFeedbackMessage('Failed to fetch monitor details!');
          setFeedbackType('error');
        }
      } catch (error) {
        console.error(`edit-monitor · ${error}`);
        setFeedbackMessage(`An error occurred while fetching monitor data: ${error}`);
        setFeedbackType('error');
      }
    };

    fetchMonitorData();
  }, [monitorId]); // Fetch when monitorId changes

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);

    setFeedbackMessage(``);
    setFeedbackType('');

    const monitorData = {
      monitor_id: monitorId, // Include the monitor_id for the update
      title,
      what_to_monitor: whatToMonitor,
      url_to_monitor: urlToMonitor,
      escalation_email_on: escalationEmailOn,
      escalation_email_to: escalationEmailTo,
    };

    try {
      const response = await fetch(`/monitors/${monitorId}/edit-monitor/api-edit-monitor`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(monitorData),
      });

      if (!response.ok) {
        throw new Error("Failed to edit monitor");
      }
      else{
        setFeedbackMessage(`Changes saved.`);
        setFeedbackType('success');
      }

    } catch (error) {
      console.error(error);
      
      setFeedbackMessage(`An error occurred while editing the monitor.`);
      setFeedbackType('error');
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="main_box">
      <h1>Edit Monitor {title}</h1>

      {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

      <form onSubmit={handleSubmit}>
        <p>
          <label htmlFor="title">Title</label><br />
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            style={{ width: "99%" }}
            autoFocus
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
            {loading ? "Editing Monitor..." : "Save Changes to Monitor"}
          </button>
        </p>
      </form>
    </div>
  );
}
