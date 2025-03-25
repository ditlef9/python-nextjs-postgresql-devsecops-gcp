"use client";
import { useState, useEffect } from "react";

export default function PublicMigrations() {
  // State variables
  const [feedbackMessage, setFeedbackMessage] = useState('');
  const [feedbackType, setFeedbackType] = useState('');

  // Function to trigger migration
  const runMigrations = async () => {
    setFeedbackMessage('');
    setFeedbackType('');

    try {
      const response = await fetch(`/public-migrations/api-run-migrations`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      const data = await response.json();
      if (response.ok) {
        setFeedbackMessage(data.message || 'Successful!');
        setFeedbackType('success');
      } else {
        setFeedbackMessage(data.message || 'Failed.');
        setFeedbackType('error');
      }
    } catch (e) {
      console.log(`public-migrations · An error occurred: ${e}`);
      setFeedbackMessage('An error occurred. Please try again.');
      setFeedbackType('error');
    }
  };

  // Run migrations on load
  useEffect(() => {
    runMigrations();
  }, []);

  return (
    <>
      <h1>DB Migrations (Public)</h1>

      <div className="main_box">
        {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}
        <p>This runs public migrations</p>
      </div>
    </>
  );
}
