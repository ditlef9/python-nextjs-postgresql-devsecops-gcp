// app/(private)/dashboard/api-get-monitors/route.ts

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
        monitor_id, 
        title, 
        what_to_monitor, 
        url_to_monitor,
        escalation_email_on,
        escalation_email_to,
        last_checked_datetime,
        is_offline,
        offline_datetime,
        is_escalated,
        escalated_datetime
      FROM u_monitors_index
      ORDER BY title ASC;
    `);

    return NextResponse.json({ data: res.rows });
  } catch (error) {
    console.error("api-get-monitors · Error fetching monitors:", error);
    return NextResponse.json({ error: "Database query failed" }, { status: 500 });
  }
}
