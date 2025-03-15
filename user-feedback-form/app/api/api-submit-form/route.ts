// app/api/api-submit-form/route.ts

import { NextResponse } from 'next/server';
import { uploadToGoogleBucket } from '@/utils/uploadToGoogleBucket';
import { sendEmail } from '@/utils/sendEmail';

export async function POST(request: Request) {
  try {
    const formData = await request.json();

    // Wait for the upload to complete
    await uploadToGoogleBucket(formData);

    // Second, send an email with the form data
    await sendEmail(formData);
    
    // Response on success
    return NextResponse.json(
      { message: 'Form submitted and stored successfully!' },
      { status: 200 }
    );
  } catch (error) {
    console.error('🚨 Error processing form:', error);
    return NextResponse.json(
      { message: 'Error submitting the form. Please try again later.' },
      { status: 500 }
    );
  }
}
