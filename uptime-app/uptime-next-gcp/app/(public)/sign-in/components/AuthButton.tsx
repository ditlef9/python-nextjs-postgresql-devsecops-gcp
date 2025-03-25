// app/(public)/sign-in/components/AuthButton.tsx
"use client";

import { signIn, signOut, useSession } from "next-auth/react";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function AuthButton() {
  const { data: session, status } = useSession();
  const router = useRouter();

  // Redirect to /dashboard if authenticated
  useEffect(() => {
    if (session) {
      router.push("/monitors");
    }
  }, [session, router]);

  if (status === "loading") {
    return <p>Loading...</p>;
  }

  if (session) {
    return (
      <div>
        <p>Welcome, {session.user?.name}!</p>
        <button onClick={() => signOut()}>Sign Out</button>
      </div>
    );
  }

  return (
    <button onClick={() => signIn("github", { callbackUrl: "/dashboard" })}>Sign In with GitHub</button>
  );
}
