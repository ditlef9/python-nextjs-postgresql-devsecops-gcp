// app/types/next-auth.d.ts

import { DefaultSession, DefaultUser } from "next-auth";

declare module "next-auth" {
  interface User extends DefaultUser {
    token?: string;
    name?: string;
    firstName?: string;
    middleName?: string;
    lastName?: string;
    displayName?: string;
    isApproved?: boolean;
    rank?: string;
  }

  interface Session {
    user: {
      token?: string;
      name?: string;
      firstName?: string;
      middleName?: string;
      lastName?: string;
      displayName?: string;
      isApproved?: boolean;
      rank?: string;
    } & DefaultSession["user"];
  }
}

declare module "next-auth/jwt" {
  interface JWT {
    token?: string;
    name?: string;
  }
}
