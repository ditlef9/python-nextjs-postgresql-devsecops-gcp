// app/(private)/users/[userId]/edit-user/page.tsx

"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useParams } from "next/navigation"; // Import the `useParams` hook

export default function EditUser() {
  const { userId } = useParams(); // Get the monitorId from the route params
  const [user, setUser] = useState<any | null>(null);
  const [email, setEmail] = useState("");
  const [displayName, setDisplayName] = useState("");
  const [loading, setLoading] = useState(false);
  
  const [feedbackMessage, setFeedbackMessage] = useState('');
  const [feedbackType, setFeedbackType] = useState('');
  
  const router = useRouter(); // ???

  useEffect(() => {
    if (!userId) return; // If userId is not available, don't attempt to fetch data

    console.log(`edit-user · Fetchng user from /users/${userId}/api-get-user`);
    const fetchUserData = async () => {
      try {
        const response = await fetch(`/users/${userId}/api-get-user`);
        if (response.ok) {
          const json = await response.json();
          setUser(json.data);
          setEmail(json.data.user_email);
          setDisplayName(json.data.user_display_name);
          console.log(`edit-user · json: ${JSON.stringify(json)}`);
          console.log(`edit-user · data: ${JSON.stringify(json.data)}`);
          console.log(`edit-user · Email: ${json.data.user_email}`);
          console.log(`edit-user · Display Name: ${json.data.user_display_name}`);
        } else {
          setFeedbackMessage('Failed to fetch details!');
          setFeedbackType('error');
        }
      } catch (error) {
        console.error(`edit-user · ${error}`);
        setFeedbackMessage(`An error occurred while fetching user data: ${error}`);
        setFeedbackType('error');
      }
    };

    fetchUserData();
  }, [userId]); // Fetch when userId changes

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);

    setFeedbackMessage(``);
    setFeedbackType('');

    const userData = {
      user_id: userId, // Include the user_id for the update
      email,
      display_name: displayName,
    };

    try {
      const response = await fetch(`/users/${userId}/edit-user/api-edit-user`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });

      if (!response.ok) {
        throw new Error("Failed to edit user");
      }
      else{
        setFeedbackMessage(`Changes saved.`);
        setFeedbackType('success');
      }

    } catch (error) {
      console.error(error);
      
      setFeedbackMessage(`An error occurred while editing the user.`);
      setFeedbackType('error');
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="main_box">
      <h1>Edit User {displayName}</h1>

      {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

      <form onSubmit={handleSubmit}>
        
      <p>
          <label htmlFor="email">Email</label><br />
          <input
            type="text"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            autoFocus
            style={{ width: "99%" }}
          />
        </p>

        <p>
          <label htmlFor="displayName">Display Name</label><br />
          <input
            type="text"
            id="displayName"
            value={displayName}
            onChange={(e) => setDisplayName(e.target.value)}
            required
            style={{ width: "99%" }}
          />
        </p>


        <p>
          <button type="submit" disabled={loading}>
            {loading ? "Editing User..." : "Save Changes to User"}
          </button>
        </p>
      </form>
    </div>
  );
}
