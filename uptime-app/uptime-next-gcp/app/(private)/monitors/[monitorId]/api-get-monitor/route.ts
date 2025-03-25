// app/(private)/monitors/[monitorId]/api-get-monitor/route.ts
// Next 15.2.3
// Reference to the docs: https://nextjs.org/docs/app/api-reference/file-conventions/route#context-optional

import { NextRequest, NextResponse } from "next/server";
import { sql } from "@/app/lib/db";
import { loginIsRequiredServer } from "@/app/lib/loginIsRequiredServer";
import { getServerSession } from "next-auth";
import { authConfig } from "@/app/lib/auth";
export async function GET(request: NextRequest, context: { params: Promise<{ monitorId: string }> }) {

  const monitorId = (await context.params).monitorId;

  // Ensure params exist
  if (!monitorId) {
    return NextResponse.json({ message: "Missing monitor ID" }, { status: 400 });
  }

  // Session check
  await loginIsRequiredServer();
  const session = await getServerSession(authConfig);
  if (!session) {
    return NextResponse.json({ message: "Unauthorized" }, { status: 401 });
  }

  try {
    // Query the database for monitor details using the monitorId
    const res = await sql(
      `SELECT monitor_id, title, what_to_monitor, url_to_monitor, escalation_email_on, 
      escalation_email_to, last_checked_datetime, is_offline, offline_datetime, is_escalated,
      escalated_datetime
      FROM u_monitors_index WHERE monitor_id = $1`,
      [monitorId]
    );

    if (res.rows.length === 0) {
      return NextResponse.json({ message: "Monitor not found" }, { status: 404 });
    }

    return NextResponse.json({ data: res.rows[0] });
  } catch (error) {
    console.error("get-monitor · Error getting:", error);
    return NextResponse.json({ message: "Error getting monitor" }, { status: 500 });
  }
}