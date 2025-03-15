// app/utils/uploadToGoogleBucket.ts
import { Storage } from '@google-cloud/storage';

const storage = new Storage();
const bucketName = 'user-feedback-form-bucket'; // Replace with your actual bucket name

export async function uploadToGoogleBucket(formData: any) {
  return new Promise((resolve, reject) => {
    const bucket = storage.bucket(bucketName);
    const timestamp = Date.now();
    const fileName = `form-submission-${timestamp}.json`;

    const file = bucket.file(fileName);
    const fileStream = file.createWriteStream({
      resumable: false,
      gzip: true,
      contentType: 'application/json',
    });

    fileStream.on('error', (err) => {
      console.error('❌ Error uploading to Google Cloud Storage:', err);
      reject(err); // Reject the promise with the error
    });

    fileStream.on('finish', () => {
      console.log(`✅ File ${fileName} uploaded to Google Cloud Storage.`);
      resolve(true); // Resolve the promise when finished
    });

    // Write the form data as JSON to the file
    fileStream.end(JSON.stringify(formData));
  });
}
