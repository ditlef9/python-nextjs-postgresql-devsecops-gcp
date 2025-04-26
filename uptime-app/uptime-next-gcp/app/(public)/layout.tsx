
// app/(public)/layout.tsx
 
"use client";
import "./public.css";

import { SessionProvider } from "next-auth/react";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      <InnerLayout>{children}</InnerLayout>
    </SessionProvider>
  );
}

function InnerLayout({ children }: { children: React.ReactNode }) {

  return (
    <html lang="en">
      <body>
        {/* Wrap children in SessionProvider (client-side component) */}
        <SessionProvider>{children}</SessionProvider>
      </body>
    </html>
  );
}
