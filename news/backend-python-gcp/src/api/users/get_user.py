# src/api/users/get_user.py
import html
import re

from flask import request

from src.dao.db_adapter import DBAdapter
import bcrypt

from src.utils.get_datetime import get_datetime
from src.utils.validate_int import validate_int
from src.utils.validate_token import validate_token


def get_user(db: DBAdapter, jwt_secret_key: str, get_user_id: int):
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
        return {"message": f"Only admin and owner can get user", "data": None, "error": "Forbidden"}, 403

    # Get user
    query: str = """SELECT user_id, user_email, user_first_name, user_middle_name, user_last_name, user_display_name, user_is_approved, user_rank, user_department, user_type FROM n_users_index WHERE user_id=:user_id"""
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
    sql_user_department = rows[0][8]
    sql_user_type = rows[0][9]

    # Transform to dict
    return_dict = {
        "user_id": sql_user_id,
        "user_email": sql_user_email,
        "user_first_name": sql_user_first_name,
        "user_middle_name": sql_user_middle_name,
        "user_last_name": sql_user_last_name,
        "user_display_name": sql_user_display_name,
        "user_is_approved": sql_user_is_approved,
        "user_rank": sql_user_rank,
        "user_department": sql_user_department,
        "user_type": sql_user_type
    }

    # Give feedback
    return {"message": f"", "data": return_dict, "error": ""}, 200
