// app/(private)/users/add-user/api-add-user/route.ts

import { NextResponse } from "next/server";
import { sql } from "@/app/lib/db"; 
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


  try {
    const data = await request.json();

    const {
      email,
      display_name,
    } = data;

    // Insert new monitor into the database
    await sql(`
        INSERT INTO u_users_index  
        (
            user_email,
            user_display_name,
            user_created_timestamp,
            user_created_by_user_id
        ) VALUES (
        $1, $2, $3, $4
        )`,
        [
            email,
            display_name,
            dateYmdhms, 
            myUserID
        ]
    );

    // Find ID
    const res = await sql(`
        SELECT user_id
        FROM u_users_index 
        WHERE user_email = $1`, [email]);
    const sqlUser = res.rows[0];
    const userId = sqlUser.user_id;

  

    return NextResponse.json({ message: "User added successfully", user_id: userId });
  } catch (error) {
    console.error("api-add-user · Error adding user:", error);
    return NextResponse.json({ message: "Error adding user" }, { status: 500 });
  }
}
