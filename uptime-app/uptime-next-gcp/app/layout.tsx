import type { Metadata } from "next";
import "./globals.css";


export const metadata: Metadata = {
  title: "Uptime",
  description: "A modern uptime monitoring solution",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
