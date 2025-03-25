// app/(private)/users/[userId]/delete-user/api-delete-user/route.ts

import { NextRequest, NextResponse } from "next/server";
import { sql } from "@/app/lib/db"; // Assuming you're using a database client
import { loginIsRequiredServer } from "@/app/lib/loginIsRequiredServer";
import { getServerSession } from "next-auth";
import { authConfig } from "@/app/lib/auth";

export async function DELETE(request: NextRequest, context: { params: Promise<{ userId: string }> }) {

  const userId = (await context.params).userId;

  // Ensure params exist
  if (!userId) {
    return NextResponse.json({ message: "Missing user ID" }, { status: 400 });
  }
  console.info(`api-delete-user · Delete user: ${userId}`);

  // Session check
  await loginIsRequiredServer();
  const session = await getServerSession(authConfig);
  if (!session) {
    return NextResponse.json({ message: "Unauthorized" }, { status: 401 });
  }

  try {

    // Delete the monitor from the database
    await sql(`DELETE FROM u_users_index WHERE user_id = $1`, [userId]);

    return NextResponse.json({ message: "User deleted successfully" });
  } catch (error) {
    console.error("api-delete-user · Error deleting user:", error);
    return NextResponse.json({ message: "Error deleting user" }, { status: 500 });
  }
}