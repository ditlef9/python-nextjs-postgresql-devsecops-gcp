// app/lib/auth.ts
import { NextAuthOptions, User } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import jwt, { JwtPayload } from "jsonwebtoken"; // Import the jsonwebtoken package

interface DecodedToken extends JwtPayload {
  userId: string;
  userEmail: string;
  userFirstName: string;
  userMiddleName: string;
  userLastName: string;
  userDisplayName: string;
  userIsApproved: boolean;
  userRank: string;
}

export const authConfig: NextAuthOptions = {
  providers: [
    CredentialsProvider({
      name: "Sign in",
      credentials: {
        email: {
          label: "Email",
          type: "email",
          placeholder: "example@example.com",
        },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        // Null check for credentials
        if (!credentials || !credentials.email || !credentials.password) return null;
      
        const payload = {
          email: credentials.email,
          password: credentials.password,
        };
      
        try {
          const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/users/log-in`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
          });
      
          if (!res.ok) {
            
            try {
              const errorResponse = await res.json();
              console.log(`auth.authorize() · Error response: ${errorResponse.message}`);
            } catch (e) {
              console.log(`auth.authorize() · Error while parsing error response: ${e}`);
            }
            return null; // Return null if the response is not ok
          }
      
          const data = await res.json(); // Assuming the response contains the token
          const token = data?.data?.token; // Adjust this to match your API's response structure


          // user_id, user_email, user_first_name, user_middle_name, user_last_name and user_display_name is part of the payload of the token
          const decodedToken = jwt.decode(token) as DecodedToken | null;

          if (!decodedToken) {
            console.error("auth.authorize() · Failed to decode JWT token");
            return null;
          }

          const userId = decodedToken.user_id ?? null; // Access the userId from the decoded token
          const userEmail = decodedToken.user_email; 
          const userFirstName = decodedToken.user_first_name; 
          const userMiddleName = decodedToken.user_middle_name; 
          const userLastName = decodedToken.user_last_name; 
          const userDisplayName = decodedToken.user_display_name; 
          const userIsApproved = decodedToken.user_is_approved; 
          const userRank = decodedToken.user_rank; 
          if (!userId) {
            console.error("auth.authorize() · Decoded token is missing required properties", decodedToken);
            return null;
          }
          // console.log("auth.authorize() · Decoded Token:", decodedToken); // Debug the decoded token

          // Type assertion here
          return {
            id: userId,  // Ensure you have a user id
            email: userEmail,
            token, // Include the token
            name: userDisplayName,
            firstName: userFirstName,
            middleName: userMiddleName,
            lastName: userLastName,
            displayName: userDisplayName,
            isApproved: userIsApproved,
            rank: userRank
          } as unknown as User; // Cast it as unknown first, then to User
      
        } catch (error) {
          console.error("auth.authorize() · Error occurred during login:", error);
          return null;
        }
      },
    }),
  ],
  callbacks: {
    async session({ session, token }) {
      // Attach token to session if available
      if (session?.user && token) {
        session.user.email = token.email; // Assign email from token to session
        session.user.token = token.token; // Save token in session
        session.user.firstName = token.firstName as string; // Save first name
        session.user.middleName = token.middleName as string; // Save middle name
        session.user.lastName = token.lastName as string; // Save last name
        session.user.displayName = token.displayName as string; // Save display name
        session.user.isApproved = token.isApproved as boolean; // Save approval status
        session.user.rank = token.rank as string; // Save rank
      }
      return session;
    },
    async jwt({ token, user }) {
      // Persist user data and token in the JWT
      if (user) {
        token.email = user.email;
        token.token = user.token; // Save token in JWT
        token.userId = user.id;
        token.firstName = user.firstName;
        token.middleName = user.middleName;
        token.lastName = user.lastName;
        token.displayName = user.displayName;
        token.isApproved = user.isApproved;
        token.rank = user.rank;
      }
      return token;
    },
  },
};
