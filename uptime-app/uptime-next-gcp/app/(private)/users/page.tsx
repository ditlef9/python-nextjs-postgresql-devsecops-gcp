// app/(private)/users/page.tsx

"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { useLoginRequiredClient } from "@/app/lib/useLoginRequiredClient";
import { UsersI } from "@/app/types/usersI";

export default function Dashboard() {
  const { session, status } = useLoginRequiredClient();
  const [users, setUsers] = useState<UsersI[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {

      try {
        const apiUrl = `/users/api-get-users`;
        console.log("users · Fetching users from:", apiUrl);
        const response = await fetch(apiUrl);
        const data = await response.json();

        if (response.ok) {
          setUsers(data.data);
        } else {
          setError(data.message || "Failed to fetch users");
        }
      } catch (error) {
        console.error("users · Error fetching:", error);
        setError("An error occurred while fetching users.");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);


  return (
    <div className="main_box">
      <h1>Users</h1>

      <p>
      <Link href="/users/add-user">Add user</Link>
      </p>

      {users.length > 0 ? (
        <table className="generic-table">
          <thead>
            <tr>
              <th><span>Name</span></th>
              <th><span>Email</span></th>
              <th><span>Actions</span></th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.user_id}>
               <td>
                <span>
                  {user.user_display_name}
                  </span>
               </td>
                <td>
                  <span>{user.user_email}</span>
                </td>
                <td>
                  <span>
                  <Link href={`/users/${user.user_id}/edit-user`}>Edit</Link>
                  &nbsp;&middot;&nbsp;
                  <Link href={`/users/${user.user_id}/delete-user`}>Delete</Link>
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        loading ? <p>Loading...</p> : <p>No users found.</p>
      )}
    </div>
  );
}
