// app/types/monitorsI.ts
export interface MonitorsI {
    monitor_id: string;
    title: string;
    what_to_monitor: string;
    url_to_monitor: string;
    escalation_email_on: boolean;
    escalation_email_to: string;
    last_checked_datetime: string;
    is_offline: boolean;
    offline_datetime: string | null; // Assuming nullable timestamps
    is_escalated: boolean;
    escalated_datetime: string | null; // Assuming nullable timestamps
  }
  