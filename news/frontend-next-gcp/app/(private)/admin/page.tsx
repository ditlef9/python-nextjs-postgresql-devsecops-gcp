// app/(public)/admin/page.tsx

'use client';

import Link from 'next/link';
import { useSession } from "next-auth/react"; // Import useSession

export default function Users() {
    // Session
    const { data: session } = useSession();
    if (!session) {
        return <p>You must be logged in to view this page.</p>;
    }
    // Check admin
    if(session?.user?.rank !== 'admin'){
      return <p>Admin only.</p>;
    }

  return (
    <>
    <h1>Admin</h1>

    <p>
    {session?.user?.name || "Unknown name"}
    {session?.user?.email || "Unknown email"}
    </p>

    <ul>
        <li><Link href="admin/users">Users</Link></li>
        <li><Link href="admin/news/">News</Link></li>
        <li><Link href="admin/news/create-news">Create news</Link></li>
        <li><Link href="../">Homepage</Link></li>
    </ul>
    </>
  );
}
