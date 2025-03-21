# src/api/users/register.py
import html
import re

from flask import request

from src.dao.db_adapter import DBAdapter
import bcrypt

from src.utils.get_datetime import get_datetime


def register(db: DBAdapter):
    # Datetime
    dt = get_datetime()

    # Post variables
    json_data = request.get_json()

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

    # user_email :: Check availability
    q: str = "SELECT user_id FROM n_users_index WHERE user_email=:email"
    p: dict = {"email": post_email}
    rows = db.select_where(query=q, parameters=p)
    rows_count = db.count_rows(rows)
    if rows_count > 0:
        return {"message": f"Email is taken", "data": None, "error": "Conflict"}, 409

    # user_first_name
    post_first_name = json_data.get('first_name')
    if post_first_name == "":
        return {"message": f"First name is blank", "data": None, "error": "Payment Required"}, 402
    post_first_name = html.escape(s=post_first_name, quote=True)
    post_first_name = post_first_name.strip()

    # user_middle_name
    post_middle_name = json_data.get('middle_name')
    post_middle_name = html.escape(s=post_middle_name, quote=True)
    post_middle_name = post_middle_name.strip()

    # user_last_name
    post_last_name = json_data.get('last_name')
    if post_last_name == "":
        return {"message": f"Last name is blank", "data": None, "error": "Payment Required"}, 402
    post_last_name = html.escape(s=post_last_name, quote=True)
    post_last_name = post_last_name.strip()

    # user_display_name - Construct user_display_name: "FirstName L."
    post_display_name = post_first_name
    if post_display_name:
        post_display_name += f" {post_last_name[0]}."

    # user_password
    post_password = json_data.get('password')
    if not post_password:
        return {"message": "Password is blank", "data": None, "error": "Payment Required"}, 402
    post_password_encrypted = bcrypt.hashpw(post_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # antispam
    post_antispam = json_data.get('antispam').lower()
    if not post_antispam:
        return {"message": "Antispam is blank", "data": None, "error": "Payment Required"}, 402
    if post_antispam != "oslo":
        return {"message": "Wrong antispam", "data": None, "error": "Bad Request"}, 400

    # Insert to users_index
    query: str = """INSERT INTO n_users_index (
                user_email, user_first_name, user_middle_name, user_last_name, user_display_name,
                user_password, user_is_approved, user_rank, user_created_timestamp, user_type) 
                VALUES (
                :email, :first_name, :middle_name, :last_name, :display_name,
                :password, :is_approved, :rank, :created_timestamp, :type
                )"""
    parameters: dict = {
        "email": post_email,
        "first_name": post_first_name,
        "middle_name": post_middle_name,
        "last_name": post_last_name,
        "display_name": post_display_name,
        "password": post_password_encrypted,
        "is_approved": False,
        "rank": "user",
        "created_timestamp": dt['ymdhms'],
        "type": "user"
    }
    db.insert(query=query, parameters=parameters)

    # Find user ID
    query = """SELECT user_id FROM n_users_index WHERE user_email=:email"""
    parameters: dict = {"email": post_email}
    rows = db.select_where(query=query, parameters=parameters)
    if len(rows) == 0:
        return {"message": f"New user not found - Programming error", "data": None, "error": "Not Found"}, 404
    sql_user_id = rows[0][0]

    print(f"register()·New user registered with new user id: {sql_user_id}")

    # If user ID is 1, then set as admin
    if sql_user_id == 1:
        query: str = "UPDATE n_users_index SET user_is_approved=:is_approved, user_rank=:rank WHERE user_id=:user_id"
        parameters: dict = {"is_approved": True, "rank": "admin", "user_id": sql_user_id}
        db.update(query=query, parameters=parameters)

    # Give feedback
    return {"message": f"User registered", "data": {"user_id": sql_user_id}, "error": ""}, 201
