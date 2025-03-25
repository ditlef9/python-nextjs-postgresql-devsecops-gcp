// app/(public)/api/api-check-monitors/route.ts

import { sql } from "@/app/lib/db";
import { sendEmail } from "@/app/lib/sendEmail";
import { NextResponse } from "next/server";

export async function GET(request: Request) {
    // This route checks all monitors and sends an email if a monitor is offline
    // This route is meant to be called by a cron job every hour:
    // http://localhost:3000/api/api-check-monitors


    // Find all monitors
    const res = await sql(`
        SELECT 
          monitor_id, 
          title, 
          what_to_monitor, 
          url_to_monitor,
          escalation_email_on,
          escalation_email_to,
          last_checked_datetime,
          is_offline,
          offline_datetime,
          is_escalated,
          escalated_datetime
        FROM u_monitors_index
        ORDER BY last_checked_datetime ASC LIMIT 1;
      `);
    // Ensure monitors exist
    if (res.rows.length === 0) {
        return new Response(JSON.stringify({ message: "No monitors found" }), { status: 404 });
    }
    const sqlMonitor = res.rows[0];
    console.log(`api-check-monitors · Check Monitor: ${sqlMonitor.monitor_id} ${sqlMonitor.title} `);


    // Check if the monitor is offline by visiting the URL
    let isOffline = false;
    try {
      const response = await fetch(sqlMonitor.url_to_monitor);
      console.log(`api-check-monitors · Check Monitor: ${sqlMonitor.monitor_id} ${sqlMonitor.title} [response.status = ${response.status}]`);
      if (response.status === 200){
        isOffline = false;
      } else { 
        isOffline = true;
      }
    } catch (error) {
      isOffline = true;
    }
     
    // Get today's date formatted as 'YYYY-MM-DD HH:MM:SS'
    const date = new Date();
    const dateYmdhms = date.toISOString().slice(0, 19).replace("T", " ");

    // If the monitor was online but is now offline, update DB
    if (isOffline && !sqlMonitor.is_offline) {
      // Monitor was online but is now offline
      await sql(
          `UPDATE u_monitors_index SET 
          last_checked_datetime = $1, 
          is_offline = $2, 
          offline_datetime = $3, 
          is_escalated = $4, 
          escalated_datetime=$5 
          WHERE monitor_id = $6`,
          [dateYmdhms,
          true,
          dateYmdhms,
          false,
          '1900-01-01 00:00:00',  
          sqlMonitor.monitor_id]
      );
      console.log(`api-check-monitors · Check Monitor: ${sqlMonitor.monitor_id} ${sqlMonitor.title} [Offline]`);

      
      if (sqlMonitor.escalation_email_to) {
        const emailSubject = `🔴 Monitor Offline Alert: ${sqlMonitor.title}`;
        const emailBody = `
            <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                <h2 style="color: #d9534f;">🔴 Monitor Alert: ${sqlMonitor.title} is Offline</h2>
                <p><strong>Monitor Name:</strong> ${sqlMonitor.title}</p>
                <p><strong>URL:</strong> <a href="${sqlMonitor.url_to_monitor}" target="_blank">${sqlMonitor.url_to_monitor}</a></p>
                <p><strong>Checked at:</strong> ${dateYmdhms}</p>
                <p>The monitor has been detected as <span style="color: #d9534f; font-weight: bold;">OFFLINE</span>. Please take immediate action.</p>
                <a href="${sqlMonitor.url_to_monitor}" 
                   style="display: inline-block; padding: 10px 20px; background-color: #0275d8; color: #ffffff; text-decoration: none; border-radius: 5px; font-size: 16px; margin-top: 10px;">
                    Check Monitor
                </a>
                <p style="margin-top: 20px; font-size: 12px; color: #777;">This is an automated message from the monitoring system.</p>
                <p style="margin-top: 20px; font-size: 12px; color: #777;">To unsubscribe reply with 'unsubscribe' in the subject.</p>
            </div>
        `;
    
        await sendEmail(sqlMonitor.escalation_email_to, emailSubject, emailBody);
      } // Send email  
    }
    else if (!isOffline && sqlMonitor.is_offline) {
      // Monitor was offline but is now online
      await sql(
          `UPDATE u_monitors_index SET 
          last_checked_datetime = $1, 
          is_offline = $2, 
          offline_datetime = $3,
          is_escalated = $4, 
          escalated_datetime=$5
          WHERE monitor_id = $6`,
          [dateYmdhms,
          false,
          '1900-01-01 00:00:00',
          false,
          '1900-01-01 00:00:00',
          sqlMonitor.monitor_id]
      );
      console.log(`api-check-monitors · Check Monitor: ${sqlMonitor.monitor_id} ${sqlMonitor.title} [Online]`);
      if (sqlMonitor.escalation_email_to) {
        const emailSubject = `🟢 Monitor Back Online Alert: ${sqlMonitor.title}`;
        const emailBody = `
            <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                <h2 style="color: #228B22;">🟢 Monitor Alert: ${sqlMonitor.title} is back Online</h2>
                <p><strong>Monitor Name:</strong> ${sqlMonitor.title}</p>
                <p><strong>URL:</strong> <a href="${sqlMonitor.url_to_monitor}" target="_blank">${sqlMonitor.url_to_monitor}</a></p>
                <p><strong>Checked at:</strong> ${dateYmdhms}</p>
                <p>The monitor has been detected as <span style="color #228B22; font-weight: bold;">ONLINE</span>.</p>
                <a href="${sqlMonitor.url_to_monitor}" 
                   style="display: inline-block; padding: 10px 20px; background-color: #0275d8; color: #ffffff; text-decoration: none; border-radius: 5px; font-size: 16px; margin-top: 10px;">
                    Check Monitor
                </a>
                <p style="margin-top: 20px; font-size: 12px; color: #777;">This is an automated message from the monitoring system.</p>
                <p style="margin-top: 20px; font-size: 12px; color: #777;">To unsubscribe reply with 'unsubscribe' in the subject.</p>
            </div>
        `;
    
        await sendEmail(sqlMonitor.escalation_email_to, emailSubject, emailBody);
      } // Send email
    }
    else {
      // No changes
      await sql(
          `UPDATE u_monitors_index SET 
          last_checked_datetime = $1
          WHERE monitor_id = $2`,
          [dateYmdhms,
          sqlMonitor.monitor_id]
      );
      console.log(`api-check-monitors · Check Monitor: ${sqlMonitor.monitor_id} ${sqlMonitor.title} [No changes]`);
    }

    // Return
    var returnError = isOffline ? "Monitor is offline" : "Monitor is online";
    return NextResponse.json({
        "message": `Monitor check complete`,
        "data": `${sqlMonitor.monitor_id}`,
        "error": `${returnError}`,
    });
}
