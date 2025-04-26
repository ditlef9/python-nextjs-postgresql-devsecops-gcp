// app/(public)/sign-in/components/AuthButton.tsx
"use client";

import { signIn, signOut, useSession } from "next-auth/react";
import { useEffect } from "react";
import { useRouter } from "next/navigation";
import Image from "next/image";

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
    <div className="button-wrapper">
      <button onClick={() => signIn("github", { callbackUrl: "/dashboard" })} className="github-button">
        <Image src="/icons/20x20/github-icon-20x20.svg" alt="GitHub Logo" width={20} height={20} />
        Sign In with GitHub
      </button>
    </div>
  );
}
