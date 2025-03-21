// app/lib/useLoginRequiredClient.ts
"use client";

import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";

// Custom hook to check if login is required
export function useLoginRequiredClient() {
  const { data: session, status } = useSession();
  const router = useRouter();

  if (typeof window !== "undefined" && status === "unauthenticated") {
    router.push("/");
  }

  return { session, status };
}

