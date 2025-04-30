
// app\(private)\layout.tsx

"use client";

import "./private.css";
import { SessionProvider } from "next-auth/react";
import Header from "./header";
import Footer from "./footer";


export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      <InnerLayout>{children}</InnerLayout>
    </SessionProvider>
  );
}

function InnerLayout({ children }: { children: React.ReactNode }) {

  return (
    <SessionProvider>
    <html lang="en">
    <body>
        
        <div className="container">
            <Header />
            <div style={{width: "100%"}}>
                <main>
                    {children}
                </main>
                <Footer />
            </div>
        </div>
    </body>
    </html>
    </SessionProvider>
  );
}
