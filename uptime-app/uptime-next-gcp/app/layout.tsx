
"use client"; // Mark this as a Client Component

import type { Metadata } from "next";
import "./globals.css";
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
