// app/(private)/users/[userId]/edit-user/api-edit-user/route.ts

import { NextRequest, NextResponse } from "next/server";
import { sql } from "@/app/lib/db"; // Assuming you're using a database client
import { loginIsRequiredServer } from "@/app/lib/loginIsRequiredServer";
import { getServerSession } from "next-auth";
import { authConfig } from "@/app/lib/auth";

export async function PATCH(request: NextRequest, context: { params: Promise<{ userId: string }> }) {

  const userId = (await context.params).userId;

  // Ensure params exist
  if (!userId) {
    return NextResponse.json({ message: "Missing user ID" }, { status: 400 });
  }
  console.info(`api-edit-user · Edit user: ${userId}`);

  
  // Session check
  await loginIsRequiredServer();
  const session = await getServerSession(authConfig);
  if (!session) {
    return NextResponse.json({ message: "Unauthorized" }, { status: 401 });
  }
  // Find my User ID
  const res = await sql(
    `SELECT user_id
    FROM u_users_index WHERE user_email = $1`,
    [session.user.email]
  );
  const sqlMyUser = res.rows[0];
  const myUserID = sqlMyUser.user_id;

  // Get today's date formatted as 'YYYY-MM-DD HH:MM:SS'
  const date = new Date();
  const dateYmdhms = date.toISOString().slice(0, 19).replace("T", " ");

  // JSON
  try {
    const data = await request.json();
    const {
      email,
      display_name,
    } = data;

    // Update the monitor in the database
    await sql(`
      UPDATE u_users_index
      SET
        user_email = $1,
        user_display_name = $2,
        user_updated_timestamp = $3,
        user_updated_by_id = $4
      WHERE user_id = $5`,
      [
        data.email,
        data.display_name,
        dateYmdhms,
        myUserID,
        userId
      ]
    );



    return NextResponse.json({ message: "User updated successfully" });
  } catch (error) {
    console.error("api-edit-user · Error updating user:", error);
    return NextResponse.json({ message: "Error updating user" }, { status: 500 });
  }
}
