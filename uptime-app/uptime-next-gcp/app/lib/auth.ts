// app/lib/auth.ts
import { NextAuthOptions } from "next-auth";
import GitHubProvider from "next-auth/providers/github"; // Import GitHubProvider

// SQL query and database connection setup - assuming you're using `pg` or another SQL client
import { sql } from "@/app/lib/db";  // Import your SQL database client setup

export const authConfig: NextAuthOptions = {
  providers: [
    GitHubProvider({
      clientId: process.env.GITHUB_CLIENT_ID!,
      clientSecret: process.env.GITHUB_CLIENT_SECRET!,
    }),
  ],
  callbacks: {
    // SignIn callback to check if the user exists in the database
    async signIn({ user }) {
      if (user?.email) {
        try {
          // SQL query to check if the email exists in the database
          const res = await sql(
            "SELECT user_id, user_first_name, user_middle_name, user_last_name, user_display_name FROM u_users_index WHERE user_email=$1",
            [user.email]
          );

          if (res.rowCount === 0) {
            // User does not exist in the database
            console.log(`User not found with email: ${user.email}`);
            return false; // Reject sign-in if user not found
          }

          // User exists, log their details
          const sqlMyUser = res.rows[0];
          console.log("User found in DB: ", sqlMyUser);
          
          // Optionally, you could add user details to the session or token here
          // Example: Add user_id to the token for later use
          user.id = sqlMyUser.user_id;  // Add user_id from DB to the session token

        } catch (error) {
          console.error("Error checking user email in database: ", error);
          return false; // Reject sign-in in case of an error
        }
      }
      return true; // Allow sign-in if user email exists in the database
    },

    // Session callback to attach user ID to the session
    async session({ session, token }) {
      if (session.user) {
        // Adding user ID to the session object
        session.user.id = token.sub!; // `sub` is the user ID from the token
      }
      return session;
    },
  },
  secret: process.env.NEXTAUTH_SECRET, // Ensure this secret is securely set in .env.local
};
