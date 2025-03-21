// app/(private)/admin/news/page.tsx

'use client';

import { useSession } from 'next-auth/react';
import Link from 'next/link';
import { useState, useEffect } from 'react';

interface NewsItem {
    news_id: string;
    news_title: string;
    news_text: string;
    news_created_timestamp: string;
    news_created_by_user_id: string;
    news_created_by_display_name: string;
}

export default function AdminNews() {
    // Hooks should always be at the top
    const { data: session } = useSession();
    
    // State hooks (must be before any conditional returns)
    const [news, setNews] = useState<NewsItem[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [feedbackMessage, setFeedbackMessage] = useState('');
    const [feedbackType, setFeedbackType] = useState('');

    // Fetch news from the backend
    useEffect(() => {
        const fetchNews = async () => {
            try {
                const response = await fetch(
                    `${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/news/get-all-news`
                );

                const data = await response.json();

                if (response.ok) {
                    setNews(data.data);
                } else {
                    setFeedbackMessage(data.message || "Failed to fetch news.");
                    setFeedbackType("error");
                }
            } catch (err) {
                console.error("Error fetching news:", err);
                setFeedbackMessage("An error occurred while fetching news.");
                setFeedbackType("error");
            } finally {
                setLoading(false);
            }
        };

        fetchNews();
    }, []);

    // Conditional rendering instead of early return
    if (!session) {
        return <p>You must be logged in to view this page.</p>;
    }

    if (session?.user?.rank !== 'admin') {
        return <p>Admin only.</p>;
    }

    return (
        <>
            <h1>Admin News</h1>
            
            {/* Feedback */}
            {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

            {/* Show loading state */}
            {loading ? (
                <p>Loading news...</p>
            ) : news.length > 0 ? (
                news.map((newsData) => (
                    <div key={newsData.news_id}>
                        <p style={{ float: "right" }}>
                            <Link href={`/admin/news/${newsData.news_id}/edit-news`}>Edit</Link>
                            &nbsp;&middot;&nbsp;
                            <Link href={`/admin/news/${newsData.news_id}/delete-news`}>Delete</Link>
                        </p>

                        <h2>{newsData.news_title}</h2>

                        <p style={{ fontSize: "90%", color: "grey" }}>
                            Created {newsData.news_created_timestamp} by &nbsp;
                            <Link href={`/admin/users/${newsData.news_created_by_user_id}/edit`} style={{ color: "grey" }}>
                                {newsData.news_created_by_display_name}
                            </Link>
                        </p>

                        <p>{newsData.news_text}</p>

                        <p><hr /></p>
                    </div>
                ))
            ) : (
                <p>No news found.</p>
            )}
        </>
    );
}
