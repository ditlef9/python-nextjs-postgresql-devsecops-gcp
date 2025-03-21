// app/(private)/admin/news/[newsId]/edit-news/page.tsx
'use client';

import { useSession } from 'next-auth/react';
import { useParams } from 'next/navigation';
import { useState, ChangeEvent, FormEvent, useEffect } from 'react';

export default function EditNews() {
    // Hooks should always be called at the top level
    const { data: session } = useSession();
    const { newsId } = useParams();

    // State hooks should be declared at the top level
    const [formData, setFormData] = useState({
        news_title: '',
        news_title_slug: '',
        news_text: ''
    });
    const [feedbackMessage, setFeedbackMessage] = useState('');
    const [feedbackType, setFeedbackType] = useState('');

    // Fetch user data when the component mounts
    useEffect(() => {
        if (!session) return; // Ensure session is available before making a request

        const fetchNewsData = async () => {
            try {
                const response = await fetch(
                    `${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/news/get-single-news/${newsId}`,
                    {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                            Authorization: `Bearer ${session.user.token}`,
                        },
                    }
                );

                const data = await response.json();
                if (response.ok) {
                    setFormData({
                        news_title: data.data.news_title,
                        news_title_slug: data.data.news_title_slug,
                        news_text: data.data.news_text,
                    });
                } else {
                    setFeedbackMessage(data.message || 'Failed to fetch data.');
                    setFeedbackType('error');
                }
            } catch (error) {
                console.error('Error fetching data:', error);
                setFeedbackMessage('Failed to load data. Please try again later.');
                setFeedbackType('error');
            }
        };

        fetchNewsData();
    }, [newsId, session]);

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
            const response = await fetch(
                `${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/news/edit-news/${newsId}`,
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Bearer ${session?.user?.token}`,
                    },
                    body: JSON.stringify(formData),
                }
            );

            const data = await response.json();
            if (response.ok) {
                setFeedbackMessage(data.message || 'Successful!');
                setFeedbackType('success');
            } else {
                setFeedbackMessage(data.message || 'Failed.');
                setFeedbackType('error');
            }
        } catch (e) {
            console.error(`[newsId]/edit-news·An error occurred:`, e);
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
            <h1>Edit News</h1>
            {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

            <form onSubmit={handleSubmit}>
                <p>
                    <label>Title</label><br />
                    <input
                        name="news_title"
                        type="text"
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
                    <button type="submit" className="submit-button">Update</button>
                </p>
            </form>
        </>
    );
}
