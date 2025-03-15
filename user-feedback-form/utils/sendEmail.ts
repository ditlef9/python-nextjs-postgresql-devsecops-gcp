// app/utils/sendEmail.ts
// app/utils/sendEmail.ts

import nodemailer from 'nodemailer';
import dotenv from 'dotenv';

// Load environment variables
dotenv.config();

// Create a transport
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.SMTP_USER, // Your Gmail address (e.g., your-email@gmail.com)
    pass: process.env.SMTP_PASS, // Your generated App Password
  },
});

export async function sendEmail(formData: any) {
  // Get current date in YYYY-MM-DD format
  const currentDate = new Date().toISOString().split('T')[0]; // Format as "YYYY-MM-DD"

  const mailOptions = {
    from: process.env.SMTP_USER,  // Your Gmail address
    to: process.env.RECEIVER_EMAIL,  // The email address to receive the feedback
    subject: `User Feedback Form: ${formData.name} (${currentDate})`, // Adding the date to the subject
    html: `
      <html>
        <body style="font-family: Arial, sans-serif; color: #333;">
          <h2 style="color: #4CAF50;">New User Feedback Form Submission</h2>
          
          <p><strong>Name:</strong> ${formData.name}</p>
          <p><strong>Email:</strong> ${formData.email}</p>
          <p><strong>Satisfaction:</strong> ${'★'.repeat(formData.satisfaction)}${'☆'.repeat(5 - formData.satisfaction)}</p>
          
          <h3>Message:</h3>
          <p>${formData.message || 'No message provided.'}</p>
          
          <hr style="border: 1px solid #ddd;">
          <p style="color: #888;">This feedback was submitted on ${new Date().toLocaleString()}.</p>
        </body>
      </html>
    `,  // Send the form data in a styled HTML email body
  };

  try {
    await transporter.sendMail(mailOptions);
    console.log('Email sent successfully');
  } catch (error) {
    console.error('Error sending email:', error);
  }
}
