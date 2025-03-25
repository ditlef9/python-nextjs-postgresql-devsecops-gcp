// app/types/usersI.ts
export interface UsersI {
  user_id: string;
  user_email: string;
  user_display_name: string;
  user_created_timestamp: string | null; // Assuming nullable timestamps
  user_created_by_user_id: number;
  user_updated_timestamp: string | null; // Assuming nullable timestamps
  user_updated_by_id: number;
  user_last_online_timestamp:  string | null; // Assuming nullable timestamps
  user_last_ip: string;
  user_last_user_agent: string;
}
  