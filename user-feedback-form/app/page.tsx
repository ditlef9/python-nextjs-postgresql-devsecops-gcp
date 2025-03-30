// app/page.tsx
 
'use client';

import { useState, useEffect } from 'react';

export default function Home() {
  // State to manage the form inputs
  const [form, setForm] = useState({
    antispam: '',
    name: '',
    email: '',
    satisfaction: 0,
    message: ''
  });

  // State to track feedback message, type and submitted
  const [feedbackMessage, setFeedbackMessage] = useState('');
  const [feedbackType, setFeedbackType] = useState(''); // success or error  
  const [submitted, setSubmitted] = useState(false); // State to track submission status

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Handle star rating selection
  const handleStarClick = (value: number) => {
    setForm({ ...form, satisfaction: value });
  };  
  // Handle star selection using keyboard (Enter or Space)
  const handleStarKeyPress = (value: number, e: React.KeyboardEvent<HTMLSpanElement>) => {
    if (e.key === 'Enter' || e.key === ' ') {
      setForm({ ...form, satisfaction: value });
    }
  };

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setFeedbackMessage('');
    setFeedbackType('');
    if (submitted) return;
    
    // Validate anti-spam question
    if (form.antispam.trim().toLowerCase() !== 'oslo') {
      setFeedbackMessage('Incorrect answer for anti-spam question.');
      setFeedbackType('error');
      return;
    }
    // Validate required fields
    if (!form.name || !form.email || form.satisfaction === 0) {
      setFeedbackMessage('All required fields must be filled.');
      setFeedbackType('error');
      return;
    }
    
    try {
      // Send form data to backend API
      const response = await fetch('/api/api-submit-form', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      });
      
      const result = await response.json();
      if (response.ok) {
        localStorage.setItem('lastSubmit', Date.now().toString()); // Store submission time
        setSubmitted(true);
        setFeedbackMessage(result.message);
        setFeedbackType('success');
      } else {
        setFeedbackMessage(result.error || 'Submission failed. Try again later.');
        setFeedbackType('error');
      }
    } catch (err) {
      setFeedbackMessage('Error submitting the form.');
      setFeedbackType('error');
    }
  };

  return (
    <>
      <h1>User Feedback Form</h1>

      {/* Feedback */}
      {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

      {submitted ? (
        <p className="success-message">Thank you!</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <p>
          <label>What is the capital of Norway?</label><br />
          <input name="antispam" onChange={handleChange} required style={{ width: "98%" }} autoFocus />
          </p>

          <p>
          <label>Name</label><br />
          <input name="name" onChange={handleChange} required style={{ width: "98%" }} />
          </p>

          <p>
          <label>Email</label><br />
          <input name="email" type="email" onChange={handleChange} required style={{ width: "98%" }} />
          </p>

          <p style={{paddingBottom: 0, marginBottom: 0}}>
          <label>Satisfaction</label><br />
          </p>
          <div>
            {[1, 2, 3, 4, 5].map((num) => (
              <span
                key={num}
                className={`star ${form.satisfaction >= num ? 'filled' : ''}`}
                onClick={() => handleStarClick(num)}
                onKeyDown={(e) => handleStarKeyPress(num, e)} // Add keydown event
                tabIndex={0} // Make the stars focusable
                role="button" // Ensures it's announced as a button for screen readers
                aria-label={`Rating ${num}`}
              >★</span>
            ))}
          </div>
          
          <p>
          <label>Message (optional)</label><br />
          <textarea name="message" onChange={handleChange} rows={5} style={{ width: "98%" }} />
          </p>

          <p>
          <button type="submit" className="submit-button">Send</button>
          </p>
        </form>
      )}

    </>
  );
}
