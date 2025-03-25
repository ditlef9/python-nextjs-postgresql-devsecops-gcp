// app/(private)/monitors/[monitorId]/delete-monitor/api-delete-monitor/route.ts

import { NextRequest, NextResponse } from "next/server";
import { sql } from "@/app/lib/db"; // Assuming you're using a database client
import { loginIsRequiredServer } from "@/app/lib/loginIsRequiredServer";
import { getServerSession } from "next-auth";
import { authConfig } from "@/app/lib/auth";

export async function DELETE(request: NextRequest, context: { params: Promise<{ monitorId: string }> }) {

  const monitorId = (await context.params).monitorId;

  // Ensure params exist
  if (!monitorId) {
    return NextResponse.json({ message: "Missing monitor ID" }, { status: 400 });
  }
  console.info(`api-delete-monitor · Delete Monitor: ${monitorId}`);

  // Session check
  await loginIsRequiredServer();
  const session = await getServerSession(authConfig);
  if (!session) {
    return NextResponse.json({ message: "Unauthorized" }, { status: 401 });
  }

  try {

    // Delete the monitor from the database
    await sql(`DELETE FROM u_monitors_index WHERE monitor_id = $1`, [monitorId]);

    return NextResponse.json({ message: "Monitor deleted successfully" });
  } catch (error) {
    console.error("Error deleting monitor:", error);
    return NextResponse.json({ message: "Error deleting monitor" }, { status: 500 });
  }
}