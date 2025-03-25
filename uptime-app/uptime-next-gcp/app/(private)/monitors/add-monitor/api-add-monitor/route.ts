// app/(private)/monitors/add-monitor/api-add-monitor/route.ts

import { NextResponse } from "next/server";
import { sql } from "@/app/lib/db"; // Assuming you're using a database client
import { loginIsRequiredServer } from "@/app/lib/loginIsRequiredServer";
import { getServerSession } from "next-auth";
import { authConfig } from "@/app/lib/auth";

export async function POST(request: Request) {
  // Session check
  await loginIsRequiredServer();
  const session = await getServerSession(authConfig);

  if (!session) {
    return NextResponse.json({ message: "Unauthorized" }, { status: 401 });
  }

  // Get today's date formatted as 'YYYY-MM-DD HH:MM:SS'
  const date = new Date();
  const dateYmdhms = date.toISOString().slice(0, 19).replace("T", " ");


  try {
    const data = await request.json();

    const {
      title,
      what_to_monitor,
      url_to_monitor,
      escalation_email_on,
      escalation_email_to,
    } = data;

    // Insert new monitor into the database
    await sql(`
        INSERT INTO u_monitors_index  
        (
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
        ) VALUES (
        $1, $2, $3, $4, $5,
        $6, $7, $8, $9, $10
        )`,
        [
            title,
            what_to_monitor,
            url_to_monitor,
            escalation_email_on,
            escalation_email_to,

            dateYmdhms, 
            false,
            '1900-01-01 00:00:00',
            false,
            '1900-01-01 00:00:00'
        ]
    );

    // Find ID
    const engRes = await sql(`
        SELECT monitor_id
        FROM u_monitors_index 
        WHERE title = $1`, [title]);
    const sqlMonitor = engRes.rows[0];
    const monitor_id = sqlMonitor.monitor_id;

  

    return NextResponse.json({ message: "Monitor added successfully", monitor_id: monitor_id });
  } catch (error) {
    console.error("api-add-monitor · Error adding monitor:", error);
    return NextResponse.json({ message: "Error adding monitor" }, { status: 500 });
  }
}
