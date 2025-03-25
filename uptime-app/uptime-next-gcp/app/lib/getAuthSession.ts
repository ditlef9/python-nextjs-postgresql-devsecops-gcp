// @/app/lib/getAuthSession.ts
import { getServerSession } from "next-auth";
import { authConfig } from "@/app/lib/auth";

// Function to get the session on the server-side
export async function getAuthSession() {
  return await getServerSession(authConfig);
}
