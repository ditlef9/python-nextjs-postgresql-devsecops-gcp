// app/(private)/users/add-user/page.tsx

"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function AddUser() {
  const [email, setEmail] = useState("");
  const [displayName, setDisplayName] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError(null);

    const monitorData = {
      email: email,
      display_name: displayName
    };

    try {
      const response = await fetch("/users/add-user/api-add-user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(monitorData),
      });

      if (!response.ok) {
        throw new Error("Failed to add user");
      }

      router.push("/users"); // Redirect to the dashboard page on success
    } catch (error) {
      console.error(error);
      setError("An error occurred while adding the users.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="main_box">
      <h1>Add Users</h1>
      {error && <p className="error">{error}</p>}

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
          {loading ? "Adding User..." : "Add User"}
        </button>
        </p>
      </form>
    </div>
  );
}
