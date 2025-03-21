// app/(public)/layout.tsx

"use client";

export default function PublicLayout({ children }: { children: React.ReactNode }) {


  
  return (
    <>
      {/* Main */}
      <main>
        {children}
      </main>
    </>
  );
}
