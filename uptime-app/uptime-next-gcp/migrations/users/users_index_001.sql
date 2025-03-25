-- Users Index ------------------------------------------------
DROP TABLE IF EXISTS u_users_index;
CREATE TABLE IF NOT EXISTS public.u_users_index (
  user_id SERIAL PRIMARY KEY,
  user_email VARCHAR(255) NOT NULL,
  user_display_name VARCHAR(200),
  user_created_timestamp TIMESTAMP NOT NULL,
  user_created_by_user_id INT NOT NULL,
  user_updated_timestamp TIMESTAMP,
  user_updated_by_id INT,
  user_last_online_timestamp TIMESTAMP,
  user_last_ip VARCHAR(255),
  user_last_user_agent VARCHAR(255)
);
-- Insert admin 1
INSERT INTO public.u_users_index (
  user_email,
  user_display_name,
  user_created_timestamp,
  user_created_by_user_id,
  user_updated_timestamp,
  user_updated_by_id,
  user_last_online_timestamp,
  user_last_ip,
  user_last_user_agent
) 
VALUES (
  'YOUR-GMAIL-USER@gmail.com',                  -- user_email
  'John',                                -- user_display_name
  NOW(),                                 -- user_created_timestamp (current timestamp)
  1,                                     -- user_created_by_user_id (replace with actual user ID)
  NULL,                                  -- user_updated_timestamp (if not updated yet)
  1,                                     -- user_updated_by_id (replace with actual user ID, if applicable)
  NOW(),                                 -- user_last_online_timestamp (current timestamp)
  '192.168.1.1',                        -- user_last_ip (replace with actual IP)
  'Mozilla/5.0'                          -- user_last_user_agent (replace with actual user agent)
);


-- Sequence
SELECT setval(pg_get_serial_sequence('u_users_index', 'user_id'), coalesce(max(user_id)+1, 1), false) FROM u_users_index;