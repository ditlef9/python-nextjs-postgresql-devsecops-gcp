// app/(public)/log-in/page.tsx
"use client";

import { CredentialsForm } from "./components/credentialsForm";

export default function LoginPage() {

  return (
    <>
        <h1>Log in</h1>
        
        {/* Sign-In Form */}
        <CredentialsForm />
    </>
  );
}