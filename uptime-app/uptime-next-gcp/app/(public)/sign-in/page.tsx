// app\(public)\sign-in\page.tsx


import AuthButton from "@/app/(public)/sign-in/components/AuthButton";
import { getAuthSession } from "@/app/lib/getAuthSession";
import Link from "next/link";

export default async function SignIn() {
  const session = await getAuthSession();

  return (
    <div className="main_box">
      <h1>Sign In</h1>
      <AuthButton />
      {session && <p>Signed in as {session.user?.email}</p>}

      <p><Link href="public-migrations">Public migrations</Link></p>
    </div>
  );
}
