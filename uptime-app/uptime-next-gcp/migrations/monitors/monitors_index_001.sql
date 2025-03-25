-- Watch Index ------------------------------------------------
DROP TABLE IF EXISTS u_monitors_index;
CREATE TABLE IF NOT EXISTS public.u_monitors_index (
  monitor_id SERIAL PRIMARY KEY,
  title VARCHAR(200),
  what_to_monitor VARCHAR(255) NOT NULL, -- URL becomes unavailable
  url_to_monitor VARCHAR(200),
  escalation_email_on BOOLEAN,
  escalation_email_to TEXT,
  last_checked_datetime TIMESTAMP,
  is_offline BOOLEAN,
  offline_datetime TIMESTAMP,
  is_escalated BOOLEAN,
  escalated_datetime TIMESTAMP
);

-- Insert
INSERT INTO public.u_monitors_index
VALUES
(1, 'Uptime', 'URL becomes unavailable', 'https://uptime-644994207224.europe-north1.run.app',
False, 'admin@example.com', NOW(), False, NULL, False, NULL),
(2, 'API Health Check', 'URL becomes unavailable', 'https://api.example.com/health',
False, 'admin@example.com', NOW(), False, NULL, False, NULL),
(3, 'Company Website', 'URL becomes unavailable', 'https://www.company.com',
False, 'webmaster@company.com', NOW(), False, NULL, False, NULL),
(4, 'Database Status', 'URL becomes unavailable', 'https://db-monitor.example.com',
False, 'dba@example.com', NOW(), False, NULL, False, NULL);

-- Sequence
SELECT setval(pg_get_serial_sequence('u_monitors_index', 'monitor_id'), coalesce(max(monitor_id)+1, 1), false) FROM u_monitors_index;
