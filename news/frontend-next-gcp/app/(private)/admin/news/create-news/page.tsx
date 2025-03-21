// app/(private)/admin/news/create-news/page.tsx


'use client';

import { useSession } from 'next-auth/react';
import { useState, ChangeEvent, FormEvent } from 'react';

export default function CreateNews() {
    // Hooks should always be at the top level
    const { data: session } = useSession();

    // State hooks should always be defined before any return statements
    const [formData, setFormData] = useState({
        news_title: '',
        news_text: ''
    });
    const [feedbackMessage, setFeedbackMessage] = useState('');
    const [feedbackType, setFeedbackType] = useState('');

    // Handle input changes
    const handleChange = (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    // Handle form submission
    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setFeedbackMessage('');
        setFeedbackType('');

        try {
            const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/news/create-news`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${session?.user?.token}`
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            if (response.ok) {
                setFeedbackMessage(data.message || 'News created successfully!');
                setFeedbackType('success');
                setFormData({ news_title: '', news_text: '' }); // Reset form after success
            } else {
                setFeedbackMessage(data.message || 'Failed to create news.');
                setFeedbackType('error');
            }
        } catch (e) {
            console.error(`create-news · An error occurred:`, e);
            setFeedbackMessage('An error occurred. Please try again.');
            setFeedbackType('error');
        }
    };

    // Conditional rendering inside return instead of early return
    if (!session) {
        return <p>You must be logged in to view this page.</p>;
    }

    if (session?.user?.rank !== 'admin') {
        return <p>Admin only.</p>;
    }

    return (
        <>
            <h1>Create News</h1>
            {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

            <form onSubmit={handleSubmit}>
                <p>
                    <label>Title</label><br />
                    <input
                        name="news_title"
                        value={formData.news_title}
                        onChange={handleChange}
                        required
                        style={{ width: "98%" }}
                        autoFocus
                    />
                </p>
                <p>
                    <label>Text</label><br />
                    <textarea
                        name="news_text"
                        value={formData.news_text}
                        onChange={handleChange}
                        required
                        style={{ width: "98%" }}
                    />
                </p>
                <p>
                    <button type="submit" className="submit-button">Submit</button>
                </p>
            </form>
        </>
    );
}
