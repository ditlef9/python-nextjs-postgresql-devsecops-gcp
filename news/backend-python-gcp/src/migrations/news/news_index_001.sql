-- News Index ------------------------------------------------
DROP TABLE IF EXISTS n_news_index;
CREATE TABLE IF NOT EXISTS public.n_news_index (
  news_id SERIAL PRIMARY KEY,
  news_title VARCHAR(255) NOT NULL,
  news_title_slug VARCHAR(255) NOT NULL,
  news_text TEXT,
  news_created_timestamp TIMESTAMP NOT NULL,
  news_created_by_user_id INT,
  news_created_by_display_name VARCHAR(255),
  news_updated_timestamp TIMESTAMP,
  news_updated_by_user_id INT,
  news_updated_by_display_name VARCHAR(255)
);

-- Example News Entry 1
INSERT INTO public.n_news_index (
  news_title,
  news_title_slug,
  news_text,
  news_created_timestamp,
  news_created_by_user_id,
  news_created_by_display_name,
  news_updated_timestamp,
  news_updated_by_user_id,
  news_updated_by_display_name
)
VALUES (
  'Breaking News: Major Event Happens',
  'breaking-news-major-event-happens',
  'This is a detailed news article about a major event that has just happened. More information is coming soon.',
  '2025-03-17 09:00:00',
  1,
  'John Doe',
  '2025-03-17 10:00:00',
  2,
  'Jane Smith'
);

-- Example News Entry 2
INSERT INTO public.n_news_index (
  news_title,
  news_title_slug,
  news_text,
  news_created_timestamp,
  news_created_by_user_id,
  news_created_by_display_name,
  news_updated_timestamp,
  news_updated_by_user_id,
  news_updated_by_display_name
)
VALUES (
  'Technology Advancements in 2025',
  'technology-advancements-in-2025',
  'The year 2025 has seen remarkable advancements in technology, with new gadgets, innovations, and breakthroughs.',
  '2025-03-16 14:30:00',
  3,
  'Alice Green',
  NULL, -- No updates yet
  NULL, -- No updates yet
  NULL
);