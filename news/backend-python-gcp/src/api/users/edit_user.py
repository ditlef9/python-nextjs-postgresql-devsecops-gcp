# src/api/users/edit_user.py
import html
import re

from flask import request

from src.dao.db_adapter import DBAdapter
import bcrypt

from src.utils.get_datetime import get_datetime
from src.utils.validate_token import validate_token


def edit_user(db: DBAdapter, jwt_secret_key: str, get_user_id: int):
    # Validate token
    validated_token_tuple: tuple = validate_token(db=db, jwt_secret_key=jwt_secret_key)
    token_validated =  validated_token_tuple[1]
    if token_validated != 200:
        # Invalid token
        return validated_token_tuple
    my_user_id = validated_token_tuple[0]['data']['my_user_id']
    my_user_email = validated_token_tuple[0]['data']['my_user_email']
    my_user_first_name = validated_token_tuple[0]['data']['my_user_first_name']
    my_user_middle_name = validated_token_tuple[0]['data']['my_user_middle_name']
    my_user_last_name = validated_token_tuple[0]['data']['my_user_last_name']
    my_user_display_name = validated_token_tuple[0]['data']['my_user_display_name']
    my_user_is_approved = validated_token_tuple[0]['data']['my_user_is_approved']
    my_user_rank = validated_token_tuple[0]['data']['my_user_rank']

    # Only admin and owner can get users list
    if my_user_rank != "admin" and my_user_rank != "owner":
        return {"message": f"Only admin and owner can get edit users", "data": None, "error": "Forbidden"}, 403


    # Get user
    query: str = """SELECT user_id, user_email, user_first_name, user_middle_name, user_last_name, user_display_name, user_is_approved, user_rank, user_type FROM n_users_index WHERE user_id=:user_id"""
    parameters: dict = {"user_id": get_user_id}
    rows = db.select_where(query=query, parameters=parameters)
    rows_count = db.count_rows(rows)
    if rows_count == 0:
        return {"message": f"User not found", "data": None, "error": "Not found"}, 404
    sql_user_id = rows[0][0]
    sql_user_email = rows[0][1]
    sql_user_first_name = rows[0][2]
    sql_user_middle_name = rows[0][3]
    sql_user_last_name = rows[0][4]
    sql_user_display_name = rows[0][5]
    sql_user_is_approved = rows[0][6]
    sql_user_rank = rows[0][7]
    sql_user_type = rows[0][8]

    # Datetime
    dt = get_datetime()

    # Post variables
    json_data = request.get_json()

    # user_email
    post_email = json_data.get('user_email')
    if post_email == "":
        return {"message": f"Email is blank", "data": None, "error": "Payment Required"}, 402
    post_email = html.escape(s=post_email, quote=True)
    post_email = post_email.strip().lower()

    # user_email :: Validate user_email format
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, post_email):
        return {"message": f"Invalid email format {post_email} :-(", "data": None, "error": "Bad Request"}, 400

    # user_email :: Check availability
    if post_email != sql_user_email:
        q: str = "SELECT user_id FROM n_users_index WHERE user_email=:email"
        p: dict = {"email": post_email}
        rows = db.select_where(query=q, parameters=p)
        rows_count = db.count_rows(rows)
        if rows_count > 0:
            return {"message": f"Email is taken", "data": None, "error": "Conflict"}, 409

    # user_first_name
    post_first_name = json_data.get('user_first_name')
    if post_first_name == "":
        return {"message": f"First name is blank", "data": None, "error": "Payment Required"}, 402
    post_first_name = html.escape(s=post_first_name, quote=True)
    post_first_name = post_first_name.strip()

    # user_middle_name
    post_middle_name = json_data.get('user_middle_name')
    post_middle_name = html.escape(s=post_middle_name, quote=True)
    post_middle_name = post_middle_name.strip()

    # user_last_name
    post_last_name = json_data.get('user_last_name')
    if post_last_name == "":
        return {"message": f"Last name is blank", "data": None, "error": "Payment Required"}, 402
    post_last_name = html.escape(s=post_last_name, quote=True)
    post_last_name = post_last_name.strip()

    # user_display_name
    post_display_name = json_data.get('user_display_name')
    if post_display_name == "":
        return {"message": f"Display name is blank", "data": None, "error": "Payment Required"}, 402
    post_display_name = html.escape(s=post_display_name, quote=True)
    post_display_name = post_display_name.strip()

    # user_rank
    post_rank = json_data.get('user_rank')
    if post_rank == "":
        return {"message": f"Rank name is blank", "data": None, "error": "Payment Required"}, 402
    post_rank = html.escape(s=post_rank, quote=True)
    post_rank = post_rank.strip()
    if post_rank != "user" and post_rank != "admin":
        return {"message": f"Unknown rank", "data": None, "error": "Payment Required"}, 402

    # user_department
    post_department = json_data.get('user_department')
    if post_department is None:
        post_department = ""
    post_department = html.escape(s=post_department, quote=True)
    post_department = post_department.strip()

    # user_is_approved
    post_is_approved = json_data.get('user_is_approved')
    post_is_approved_bool: bool = False
    if type(post_is_approved) is None:
        return {"message": "Is approved is blank", "data": None, "error": "Payment required"}, 402
    elif type(post_is_approved) is bool:
        post_is_approved_bool = post_is_approved
    else:
        if post_is_approved.lower() == "true":
            post_is_approved_bool = True


    # user_type
    post_type = json_data.get('user_type')
    if post_type == "":
        return {"message": f"Type is blank", "data": None, "error": "Payment Required"}, 402
    post_type = html.escape(s=post_type, quote=True)
    post_type = post_type.strip()
    if post_type != "user" and post_type != "service account":
        return {"message": f"Unknown type", "data": None, "error": "Payment Required"}, 402

    # Update user
    query: str = """UPDATE n_users_index SET
                user_email=:email, 
                user_first_name=:first_name, 
                user_middle_name=:middle_name, 
                user_last_name=:last_name, 
                user_display_name=:display_name,
                user_is_approved=:is_approved, 
                user_rank=:rank, 
                user_department=:department, 
                user_updated_timestamp=:updated_timestamp, 
                user_updated_by_user_id=:updated_by_user_id,
                user_type=:type
                WHERE user_id=:user_id
                """
    parameters: dict = {
        "email": post_email,
        "first_name": post_first_name,
        "middle_name": post_middle_name,
        "last_name": post_last_name,
        "display_name": post_display_name,
        "is_approved": post_is_approved_bool,
        "rank": post_rank,
        "department": post_department,
        "updated_timestamp": dt['ymdhms'],
        "updated_by_user_id": my_user_id,
        "type": post_type,
        "user_id": sql_user_id
    }
    db.update(query=query, parameters=parameters)

    # Give feedback
    return {"message": f"User updated {dt['ymdhms_saying']}", "data": {"user_id": sql_user_id}, "error": ""}, 200
