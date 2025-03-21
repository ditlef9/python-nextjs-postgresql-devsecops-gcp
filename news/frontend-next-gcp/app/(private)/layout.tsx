// app/(private)/layout.tsx
// This is the layout for the private / logged in pages.
//

"use client"; 

import { SessionProvider, useSession } from "next-auth/react";
import { useRouter } from "next/navigation"; 
import { useEffect } from "react";

export default function PrivateLayout({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      <InnerLayout>{children}</InnerLayout>
    </SessionProvider>
  );
}

function InnerLayout({ children }: { children: React.ReactNode }) {
  console.log("InnerLayout()::Init");
  const { status } = useSession(); // We don't need session here anymore
  const router = useRouter();

  useEffect(() => {
    // Authentication
    if (status === "unauthenticated") {
      console.log("InnerLayout() · unauthenticated!");
      router.push("/"); // Redirect to sign-in page if not authenticated
    }
    

    
  }, [status, router]);

  if (status === "loading") {
    console.log("InnerLayout() · Loading layout!");
    return <div><span style={{color: "black"}}>Loading - Please wait while InnerLayout is loading!</span></div>;
  }

  return (
    <>
      <main>{children}</main>
    </>
  );
}
