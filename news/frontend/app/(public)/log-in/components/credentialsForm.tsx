// app/(public)/log-in/components/credentialsForm.tsx

"use client";
import { signIn } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useState } from "react";

export function CredentialsForm() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);

  // Submit form
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const data = new FormData(e.currentTarget);
  
    const signInResponse = await signIn("credentials", {
      email: data.get("email"),
      password: data.get("password"),
      redirect: false,
    });
  
    if (signInResponse && !signInResponse.error) {
      router.push("/admin");
    } else {
      if (signInResponse?.error) {
        if (signInResponse.error === "User not authenticated") {
          setError("Your account is locked or not authenticated.");
        } else if (signInResponse.error === "User not found") {
          setError("No account found with that email.");
        } else if (signInResponse.error === "MFA verification failed") {
          setError("MFA verification failed. Please try again.");
        } else {
          setError(`Please check your email and password. If the error consists then please contact us by following the link below, and we will help you.`);
        }
      } else {
        setError("An unknown error occurred. Please try again.");
      }
    }
  };
  
  // HTML
  return (
    <form onSubmit={handleSubmit}>
      {error && (
        <div className="error">
          <span>{error}</span>
        </div>
      )}

      <p><input type="email" name="email" placeholder="Email" required /></p>
      <p><input type="password" name="password" placeholder="Password" required /></p>
      <p><button type="submit">Sign In</button></p>

    </form>
  );
}
