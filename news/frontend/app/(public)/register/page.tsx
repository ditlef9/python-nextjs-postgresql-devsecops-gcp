'use client';

import { useState, ChangeEvent, FormEvent } from 'react';

export default function Register() {
    const [formData, setFormData] = useState({
        email: '',
        first_name: '',
        middle_name: '',
        last_name: '',
        password: '',
        antispam: ''
    });
    const [submitted, setSubmitted] = useState(false);
    const [feedbackMessage, setFeedbackMessage] = useState('');
    const [feedbackType, setFeedbackType] = useState('');
    
    const API_URL = process.env.NEXT_PUBLIC_BACKEND_API_URL;

    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setFeedbackMessage('');
        setFeedbackType('');
        
        try {
            const response = await fetch(`${API_URL}/api/users/register`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            if (response.ok) {
                setSubmitted(true);
                setFeedbackMessage(data.message || 'Registration successful!');
                setFeedbackType('success');
            } else {
                setFeedbackMessage(data.message || 'Registration failed.');
                setFeedbackType('error');
            }
        } catch (e) {
            console.log(`register·An error occurred: ${e}`)
            setFeedbackMessage('An error occurred. Please try again.');
            setFeedbackType('error');
        }
    };

    return (
        <>
            <h1>User Registration</h1>
            {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}
            {submitted ? (
                <p>You are now registered!</p>
            ) : (
                <form onSubmit={handleSubmit}>
                    <p>
                        <label>Email</label><br />
                        <input name="email" type="email" onChange={handleChange} required style={{ width: "98%" }} autoFocus />
                    </p>
                    <p>
                        <label>First Name</label><br />
                        <input name="first_name" onChange={handleChange} required style={{ width: "98%" }} />
                    </p>
                    <p>
                        <label>Middle Name</label><br />
                        <input name="middle_name" onChange={handleChange} style={{ width: "98%" }} />
                    </p>
                    <p>
                        <label>Last Name</label><br />
                        <input name="last_name" onChange={handleChange} required style={{ width: "98%" }} />
                    </p>
                    <p>
                        <label>Password</label><br />
                        <input type="password" name="password" onChange={handleChange} required style={{ width: "98%" }} />
                    </p>
                    <p>
                        <label>What is the capital of Norway?</label><br />
                        <input name="antispam" onChange={handleChange} required style={{ width: "98%" }} />
                    </p>
                    <p>
                        <button type="submit" className="submit-button">Register</button>
                    </p>
                </form>
            )}
        </>
    );
}