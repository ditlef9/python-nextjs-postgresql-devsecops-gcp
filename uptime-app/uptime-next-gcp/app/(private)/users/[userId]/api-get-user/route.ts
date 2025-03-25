// app/(private)/users/[userId]/api-get-user/route.ts
// Next 15.2.3
// Reference to the docs: https://nextjs.org/docs/app/api-reference/file-conventions/route#context-optional

import { NextRequest, NextResponse } from "next/server";
import { sql } from "@/app/lib/db";
import { loginIsRequiredServer } from "@/app/lib/loginIsRequiredServer";
import { getServerSession } from "next-auth";
import { authConfig } from "@/app/lib/auth";
export async function GET(request: NextRequest, context: { params: Promise<{ userId: string }> }) {

  const userId = (await context.params).userId;

  // Ensure params exist
  if (!userId) {
    return NextResponse.json({ message: "Missing user ID" }, { status: 400 });
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
      `SELECT user_id,
        user_email,
        user_display_name,
        user_created_timestamp,
        user_created_by_user_id,
        user_updated_timestamp,
        user_updated_by_id,
        user_last_ip,
        user_last_user_agent
      FROM u_users_index WHERE user_id = $1`,
      [userId]
    );

    if (res.rows.length === 0) {
      console.error("api-get-user · User not found");
      return NextResponse.json({ message: "User not found" }, { status: 404 });
    }

    console.log("api-get-user · Returning user:", res.rows[0]);
    return NextResponse.json({ data: res.rows[0] });
  } catch (error) {
    console.error("api-get-user · Error getting:", error);
    return NextResponse.json({ message: "Error getting monitor" }, { status: 500 });
  }
}