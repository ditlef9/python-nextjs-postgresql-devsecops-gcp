// app/(public)/admin/users/page.tsx


'use client';

import { useState, useEffect } from 'react';
import { useSession } from 'next-auth/react';
import Link from 'next/link';

// Define the type for user object
interface User {
  user_id: string;
  user_email: string;
  user_display_name: string;
  user_rank: string;
  user_is_approved: boolean;
}

export default function Users() {
  // Always call hooks at the top level
  const { data: session } = useSession();
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch users only if session is available
  useEffect(() => {
    if (!session) return; // Avoid fetching if no session

    const fetchUsers = async () => {
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/users/get-users`, {
          headers: {
            Authorization: `Bearer ${session.user.token}`,
          },
        });

        const data = await response.json();

        if (response.ok) {
          setUsers(data.data);
        } else {
          setError(data.message || 'Failed to fetch users');
        }
      } catch (error) {
        setError(`An error occurred while fetching users: ${error}`);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, [session]);

  // Now we can safely use conditional rendering
  if (!session) return <p>You must be logged in to view this page.</p>;
  if (session?.user?.rank !== 'admin') return <p>Admin only.</p>;

  // Don't return before defining all hooks
  if (loading) return <p>Loading users...</p>;
  if (error) return <p>{error}</p>;

  return (
    <>
      <h1>Users</h1>
      {users.length > 0 ? (
        <table className='generic-table'>
          <thead>
            <tr>
              <th><span>Name</span></th>
              <th><span>Email</span></th>
              <th><span>Rank</span></th>
              <th><span>Approved</span></th>
              <th><span>Actions</span></th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.user_id}>
                <td><span>{user.user_display_name}</span></td>
                <td><span>{user.user_email}</span></td>
                <td>
                  <span>
                    {user.user_rank === 'user' 
                      ? 'User' 
                      : user.user_rank === 'admin' 
                        ? 'Admin' 
                        : user.user_rank === 'owner' 
                          ? 'Owner' 
                          : 'Unknown'}
                  </span>
                </td>
                <td><span>{user.user_is_approved ? 'Yes' : 'No'}</span></td>
                <td>
                  <span>
                    <Link href={`/admin/users/${user.user_id}/edit`}>Edit</Link>
                    &nbsp;&middot;&nbsp;
                    <Link href={`/admin/users/${user.user_id}/delete`}>Delete</Link>
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No users found.</p>
      )}
    </>
  );
}
