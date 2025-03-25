// app/(private)/monitors/[monitorId]/delete-monitor/page.tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useParams } from "next/navigation"; // Import the `useParams` hook

export default function DeleteMonitor() {
  const { monitorId } = useParams(); // Get the monitorId from the route params
  const [monitor, setMonitor] = useState<any | null>(null); // Monitor data
  const [title, setTitle] = useState("");
  const [userInput, setUserInput] = useState(""); // For confirmation input
  const [loading, setLoading] = useState(false);
  const [feedbackMessage, setFeedbackMessage] = useState("");
  const [feedbackType, setFeedbackType] = useState("");

  const router = useRouter();

  useEffect(() => {
    if (!monitorId) return;

    const fetchMonitorData = async () => {
      try {
        const response = await fetch(`/monitors/${monitorId}/api-get-monitor`);
        if (response.ok) {
          const json = await response.json();
          setMonitor(json.data);
          setTitle(json.data.title);
        } else {
          setFeedbackMessage("Failed to fetch monitor details!");
          setFeedbackType("error");
        }
      } catch (error) {
        console.error(error);
        setFeedbackMessage("An error occurred while fetching monitor data.");
        setFeedbackType("error");
      }
    };

    fetchMonitorData();
  }, [monitorId]);

  const handleDelete = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setFeedbackMessage("");
    setFeedbackType("");

    try {
      const response = await fetch(`/monitors/${monitorId}/delete-monitor/api-delete-monitor`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("Failed to delete monitor");
      }

      setFeedbackMessage("Monitor deleted successfully.");
      setFeedbackType("success");

      // Redirect user after successful deletion
      setTimeout(() => {
        router.push("/monitors");
      }, 2000);
    } catch (error) {
      console.error(error);
      setFeedbackMessage("An error occurred while deleting the monitor.");
      setFeedbackType("error");
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="main_box">
      <h1>Delete Monitor {title}</h1>

      {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

      <p>Are you sure you want to delete this monitor?</p>
      <p>To confirm deletion, type <b>{title}</b> below:</p>

      <form onSubmit={handleDelete}>
        <label htmlFor="confirmTitle">Monitor Title</label><br />
        <input
          type="text"
          id="confirmTitle"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          required
          style={{ width: "99%" }}
          autoFocus
        />
        <p>
          <button type="submit" disabled={loading || userInput !== title}>
            {loading ? "Deleting..." : "Delete Monitor"}
          </button>
        </p>
      </form>
    </div>
  );
}
