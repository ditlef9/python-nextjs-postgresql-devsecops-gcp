-- Users Index ------------------------------------------------
DROP TABLE IF EXISTS n_users_index;
CREATE TABLE IF NOT EXISTS public.n_users_index (
  user_id SERIAL PRIMARY KEY,
  user_email VARCHAR(255) NOT NULL,
  user_first_name VARCHAR(200),
  user_middle_name VARCHAR(200),
  user_last_name VARCHAR(200),
  user_display_name VARCHAR(200),
  user_password VARCHAR(255),
  user_mfa_type VARCHAR(255),
  user_mfa_code VARCHAR(255),
  user_login_code_value VARCHAR(255),
  user_login_code_valid_to_timestamp TIMESTAMP,
  user_is_approved BOOLEAN,
  user_rank VARCHAR(255), -- user, admin
  user_department VARCHAR(255),
  user_created_timestamp TIMESTAMP NOT NULL,
  user_created_by_user_id INT,
  user_updated_timestamp TIMESTAMP,
  user_updated_by_user_id INT,
  user_login_tries_count INT,
  user_login_tries_timestamp TIMESTAMP,
  user_login_timestamp TIMESTAMP,
  user_last_online_timestamp TIMESTAMP,
  user_last_ip VARCHAR(255),
  user_last_user_agent VARCHAR(255),
  user_type VARCHAR(50) -- user, service
);