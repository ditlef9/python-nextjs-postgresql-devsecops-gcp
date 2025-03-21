// app/(private)/admin/news/[newsId]/delete-news/page.tsx
'use client';

import { useSession } from 'next-auth/react';
import { useParams } from 'next/navigation';
import { useState, ChangeEvent, FormEvent, useEffect } from 'react';

export default function DeleteNews() {
    // Session hook should be called at the top level
    const { data: session } = useSession();
    const { newsId } = useParams();

    // State hooks should be declared at the top level
    const [formData, setFormData] = useState({ news_id: '' });
    const [feedbackMessage, setFeedbackMessage] = useState('');
    const [feedbackType, setFeedbackType] = useState('');
    const [news, setNews] = useState({
        news_title: '',
        news_title_slug: '',
        news_text: '',
    });

    // Fetch news data
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
                    setNews({
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
    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    // Handle form submission
    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setFeedbackMessage('');
        setFeedbackType('');

        try {
            const response = await fetch(
                `${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/news/delete-news/${newsId}`,
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
            console.error(`[newsId]/delete-news·An error occurred:`, e);
            setFeedbackMessage('An error occurred. Please try again.');
            setFeedbackType('error');
        }
    };

    // Conditional rendering instead of early return
    if (!session) {
        return <p>You must be logged in to view this page.</p>;
    }

    if (session?.user?.rank !== 'admin') {
        return <p>Admin only.</p>;
    }

    return (
        <>
            <h1>Delete News</h1>
            {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

            {news && (
                <p>
                    Are you sure you want to delete news <b>{news.news_title}</b>?
                    <br />
                    Confirm by entering the news&rsquo;s ID: <b>{newsId}</b>.
                </p>
            )}

            <form onSubmit={handleSubmit}>
                <p>
                    <label>ID</label><br />
                    <input
                        name="news_id"
                        type="text"
                        value={formData.news_id}
                        onChange={handleChange}
                        required
                        autoFocus
                    />
                </p>
                <p>
                    <button type="submit" className="submit-button">Delete</button>
                </p>
            </form>
        </>
    );
}
