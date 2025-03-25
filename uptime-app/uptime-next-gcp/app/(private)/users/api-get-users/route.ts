// app/(private)/users/api-get-users/route.ts

import { authConfig } from "@/app/lib/auth";
import { sql } from "@/app/lib/db";
import { loginIsRequiredServer } from "@/app/lib/loginIsRequiredServer";
import { getServerSession } from "next-auth";
import { NextResponse } from "next/server";

export async function GET() {
  await loginIsRequiredServer();
  const session = await getServerSession(authConfig);

  if (!session) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const res = await sql(`
      SELECT 
        user_id,
        user_email,
        user_display_name,
        user_created_timestamp,
        user_created_by_user_id,
        user_updated_timestamp,
        user_updated_by_id,
        user_last_ip,
        user_last_user_agent
      FROM u_users_index
      ORDER BY user_display_name ASC;
    `);

    return NextResponse.json({ data: res.rows });
  } catch (error) {
    console.error("api-get-users · Error fetching users:", error);
    return NextResponse.json({ error: "Database query failed" }, { status: 500 });
  }
}
