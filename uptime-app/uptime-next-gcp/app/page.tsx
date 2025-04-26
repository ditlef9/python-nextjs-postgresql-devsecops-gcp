// app/page.tsx

import { getServerSession } from "next-auth";
import { authConfig } from "@/app/lib/auth";
import { redirect } from "next/navigation";

export default async function SignInPage() {
  const session = await getServerSession(authConfig);
  console.log("Session: ", session);
  if (session){ 
    return redirect("/monitors");
  }
  else{
    return redirect("/sign-in");
  }
}