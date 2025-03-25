// app/(private)/monitors/[monitorId]/edit-monitor/api-edit-monitor/route.ts

import { NextRequest, NextResponse } from "next/server";
import { sql } from "@/app/lib/db"; // Assuming you're using a database client
import { loginIsRequiredServer } from "@/app/lib/loginIsRequiredServer";
import { getServerSession } from "next-auth";
import { authConfig } from "@/app/lib/auth";

export async function PATCH(request: NextRequest, context: { params: Promise<{ monitorId: string }> }) {

  const monitorId = (await context.params).monitorId;

  // Ensure params exist
  if (!monitorId) {
    return NextResponse.json({ message: "Missing monitor ID" }, { status: 400 });
  }
  console.info(`api-edit-monitor · Edit Monitor: ${monitorId}`);

  
  // Session check
  await loginIsRequiredServer();
  const session = await getServerSession(authConfig);
  if (!session) {
    return NextResponse.json({ message: "Unauthorized" }, { status: 401 });
  }


  // JSON
  try {
    const data = await request.json();
    const {
      title,
      what_to_monitor,
      url_to_monitor,
      escalation_email_on,
      escalation_email_to,
    } = data;

    // Update the monitor in the database
    await sql(`
      UPDATE u_monitors_index
      SET
        title = $1,
        what_to_monitor = $2,
        url_to_monitor = $3,
        escalation_email_on = $4,
        escalation_email_to = $5
      WHERE monitor_id = $6`,
      [
        data.title,
        data.what_to_monitor,
        data.url_to_monitor,
        data.escalation_email_on,
        data.escalation_email_to,
        monitorId
      ]
    );



    return NextResponse.json({ message: "Monitor updated successfully" });
  } catch (error) {
    console.error("Error updating monitor:", error);
    return NextResponse.json({ message: "Error updating monitor" }, { status: 500 });
  }
}
