// app/lib/sendEmail.ts
import nodemailer from "nodemailer";

export async function sendEmail(to: string, subject: string, html: string, text?: string) {
  try {
    const transporter = nodemailer.createTransport({
      service: "gmail",
      auth: {
        user: process.env.GMAIL_USER, // Your Gmail address
        pass: process.env.GMAIL_APP_PASSWORD, // Your Gmail App Password
      },
    });

    const mailOptions = {
      from: process.env.GMAIL_USER,
      to,
      subject,
      text: text || "", // Fallback to empty string if no plain text
      html, // Ensure HTML email is included
    };

    await transporter.sendMail(mailOptions);
    console.log(`sendEmail · Email sent to ${to} successfully.`);
    return { success: true };
  } catch (error) {
    console.error("sendEmail · Error sending email:", error);
    return { success: false, error };
  }
}