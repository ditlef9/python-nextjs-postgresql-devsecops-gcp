// app/(private)/users/[userId]/delete-user/page.tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useParams } from "next/navigation"; // Import the `useParams` hook

export default function DeleteMonitor() {
  const { userId } = useParams(); // Get the monitorId from the route params
  const [user, setUser] = useState<any | null>(null);
  const [displayName, setDisplayName] = useState("");
  const [email, setEmail] = useState("");
  const [userInput, setUserInput] = useState(""); // For confirmation input
  const [loading, setLoading] = useState(false);
  const [feedbackMessage, setFeedbackMessage] = useState("");
  const [feedbackType, setFeedbackType] = useState("");

  const router = useRouter();

  useEffect(() => {
    if (!userId) return;

    const fetchMonitorData = async () => {
      try {
        const response = await fetch(`/users/${userId}/api-get-user`);
        if (response.ok) {
          const json = await response.json();
          setUser(json.data);
          setDisplayName(json.data.user_display_name);
          setEmail(json.data.user_email);
        } else {
          setFeedbackMessage("Failed to fetch user details!");
          setFeedbackType("error");
        }
      } catch (error) {
        console.error(error);
        setFeedbackMessage("An error occurred while fetching user data.");
        setFeedbackType("error");
      }
    };

    fetchMonitorData();
  }, [userId]);

  const handleDelete = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setFeedbackMessage("");
    setFeedbackType("");

    try {
      const response = await fetch(`/users/${userId}/delete-user/api-delete-user`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("Failed to delete user");
      }

      setFeedbackMessage("User deleted successfully.");
      setFeedbackType("success");

      // Redirect user after successful deletion
      setTimeout(() => {
        router.push("/users");
      }, 2000);
    } catch (error) {
      console.error(error);
      setFeedbackMessage("An error occurred while deleting the user.");
      setFeedbackType("error");
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="main_box">
      <h1>Delete User {displayName}</h1>

      {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

      <p>Are you sure you want to delete this user?</p>
      <p>To confirm deletion, type <b>{email}</b> below:</p>

      <form onSubmit={handleDelete}>
        <label htmlFor="confirmEmail">Confirm Users Email</label><br />
        <input
          type="text"
          id="confirmEmail"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          required
          style={{ width: "99%" }}
          autoFocus
        />
        <p>
          <button type="submit" disabled={loading || userInput !== email}>
            {loading ? "Deleting..." : "Delete User"}
          </button>
        </p>
      </form>
    </div>
  );
}
