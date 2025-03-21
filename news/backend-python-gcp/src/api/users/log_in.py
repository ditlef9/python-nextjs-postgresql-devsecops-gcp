# src/api/users/register.py
from datetime import datetime, timedelta

import html
import re

import jwt
from flask import request

from src.dao.db_adapter import DBAdapter
import bcrypt

from src.utils.get_datetime import get_datetime


def log_in(db: DBAdapter, jwt_secret_key: str):
    print(f"log_in() · Init")
    # Datetime
    dt_info = get_datetime()

    # Post variables
    json_data = request.get_json()


    # Client
    my_user_agent = request.headers.get('User-Agent')
    my_user_agent = html.escape(s=my_user_agent, quote=True)
    my_ip = ""
    try:
        my_ip = request.access_route[0]
    except Exception as e:
        pass
    my_ip = my_ip
    my_ip = html.escape(s=my_ip, quote=True)

    # user_email
    post_email = json_data.get('email')
    if post_email == "":
        return {"message": f"Email is blank", "data": None, "error": "Payment Required"}, 402
    post_email = html.escape(s=post_email, quote=True)
    post_email = post_email.strip().lower()

    # user_email :: Validate user_email format
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, post_email):
        return {"message": f"Invalid email format {post_email} :-(", "data": None, "error": "Bad Request"}, 400

    # Find user
    q: str = "SELECT user_id, user_email, user_first_name, user_middle_name, user_last_name, user_display_name, user_password, user_is_approved, user_rank, user_login_tries_count, user_login_tries_timestamp FROM n_users_index WHERE user_email=:email"
    p: dict = {"email": post_email}
    rows = db.select_where(query=q, parameters=p)
    rows_count = db.count_rows(rows)
    if rows_count == 0:
        return {"message": f"Email not found", "data": None, "error": "Conflict"}, 409
    sql_user_id = rows[0][0]
    sql_user_email = rows[0][1]
    sql_user_first_name = rows[0][2]
    sql_user_middle_name = rows[0][3]
    sql_user_last_name = rows[0][4]
    sql_user_display_name = rows[0][5]
    sql_user_password = rows[0][6]
    sql_user_is_approved = rows[0][7]
    sql_user_rank = rows[0][8]
    sql_user_login_tries_count = rows[0][9]
    sql_user_login_tries_timestamp = rows[0][10]

    # Check login tries
    if sql_user_login_tries_count is None:
        sql_user_login_tries_count = 0
    if sql_user_login_tries_count > 10:
        lockout_time = datetime.strptime(sql_user_login_tries_timestamp, "%Y-%m-%d %H:%M:%S") + timedelta(hours=24)
        if dt_info['now'] < lockout_time:
            return {"message": "Too many login attempts. Account locked for 24 hours.", "data": None, "error": "Too Many Requests"}, 429

    # user_password
    post_password = json_data.get('password')
    if not post_password:
        return {"message": "Password is blank", "data": None, "error": "Payment Required"}, 402
    if not bcrypt.checkpw(post_password.encode("utf-8"), sql_user_password.encode("utf-8")):
        # Increment login attempts
        new_login_attempts = sql_user_login_tries_count + 1
        db.update(
            "UPDATE n_users_index SET user_login_tries_count=:count, user_login_tries_timestamp=:timestamp WHERE user_id=:user_id",
            {"count": new_login_attempts, "timestamp": dt_info["ymdhms"], "user_id": sql_user_id}
        )

        print(f"log_in() · Wrong password entered")
        return {"message": "Wrong password entered.", "data": None, "error": "Unauthorized"}, 401

    # Update last IP
    db.update(
        "UPDATE n_users_index SET user_login_timestamp=:login_timestamp, user_last_online_timestamp=:last_online_timestamp, user_last_ip=:last_ip, user_last_user_agent=:last_user_agent WHERE user_id=:user_id",
        {
            "login_timestamp": dt_info["ymdhms"],
            "last_online_timestamp": dt_info["ymdhms"],
            "last_ip": my_ip,
            "last_user_agent": my_user_agent,
            "user_id": sql_user_id
        }
    )

    # Successful login - generate JWT token
    payload = {
        "user_id": sql_user_id,  # Include the user ID in the token payload
        "user_email": sql_user_email,
        "user_first_name": sql_user_first_name,
        "user_middle_name": sql_user_middle_name,
        "user_last_name": sql_user_last_name,
        "user_display_name": sql_user_display_name,
        "user_is_approved": sql_user_is_approved,
        "user_rank": sql_user_rank,
        "exp": dt_info['now'] + timedelta(hours=24)  # Expiry time (24 hours)
    }

    # Encode the JWT with the payload and secret key
    token = jwt.encode(payload, jwt_secret_key, algorithm="HS256")

    # Return the token along with a success message
    print(f"login()·Successful login for {sql_user_id}")
    return {
        "message": "Login successful",
        "data": {
            "user_id": sql_user_id,
            "token": token
        },
        "error": None
    }, 200




