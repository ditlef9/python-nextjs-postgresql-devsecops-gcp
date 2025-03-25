// app/(private)/header.tsx
"use client";

import Link from "next/link";
import { signOut } from "next-auth/react"; // Import signOut function
import { useLoginRequiredClient } from "../lib/useLoginRequiredClient";

export default function Header() {
  const { session, status } = useLoginRequiredClient();

  
  return (
    <nav className="sidebar">
      {/* Navigation Links */}
      <Link href="/monitors">Monitors</Link>
      <Link href="/users">Users</Link>
      <a href="/public-migrations">Public Migrations</a>
      <a href="/api/api-check-monitors">API Check Monitors</a>

      {/* Logout Button */}
      <p>{session?.user?.email}</p>
      <button  onClick={() => signOut()} className="logout-btn">Log Out</button>
    </nav>
  );
}
