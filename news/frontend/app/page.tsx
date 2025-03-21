
// app/page.tsx

'use client';

import Link from "next/link";
import { useEffect, useState } from "react";

export default function Home() {
  // State to store news
  const [news, setNews] = useState<{ 
    news_id: string; 
    news_title: string; 
    news_created_timestamp: string; 
    news_created_by_display_name: string;
    news_text: string;
  }[]>([]);
  
  const [loading, setLoading] = useState<boolean>(true);
  const [feedbackMessage, setFeedbackMessage] = useState('');
  const [feedbackType, setFeedbackType] = useState('');

  // Fetch news from the backend
  useEffect(() => {
    const fetchNews = async () => {
      const apiUrl = `${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/news/get-all-news`;
      console.log("Fetching news from:", apiUrl);
      try {
        const response = await fetch(apiUrl);

        const data = await response.json();

        if (response.ok) {
          setNews(data.data);
        } else {
          setFeedbackMessage(data.message || "Failed to fetch news.");
          setFeedbackType("error");
        }
      } catch (error) {
        console.error("app/page · Error fetching news:", error);
        setFeedbackMessage(`An error occurred while fetching news from ${process.env.NEXT_PUBLIC_BACKEND_API_URL}: ${error}`);
        setFeedbackType("error");
      } finally {
        setLoading(false);
      }
    };

    fetchNews();
  }, []);

  // Display loading state while fetching data
  if (loading) {
    return <p>Loading news...</p>;
  }



  return (
    <>
      <main>
        <p>
          <Link href="/register">Register</Link>
          &nbsp; &middot; &nbsp;
          <Link href="/log-in">Log in</Link>
        </p>

        {/* Feedback */}
        {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}
        
        {/* News */}
        {news.length > 0 ? (
          news.map((newsData) => (
            <div key={newsData.news_id}>
              <h2>{newsData.news_title}</h2>
              
              <p style={{fontSize: "90%", color: "grey"}}>
              Created {newsData.news_created_timestamp} by {newsData.news_created_by_display_name}
              </p>

              <p>{newsData.news_text}</p>

              <p><hr /></p>
            </div>
          ))
        ) : (
          <p>No news found.</p>
        )}


      </main>
    </>
  );
}
