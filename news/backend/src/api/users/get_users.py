# src/api/users/users_list.py
import html
import re

from flask import request

from src.dao.db_adapter import DBAdapter
import bcrypt

from src.utils.get_datetime import get_datetime
from src.utils.validate_token import validate_token


def get_users(db: DBAdapter, jwt_secret_key: str):
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
        return {"message": f"Only admin and owner can get users list", "data": None, "error": "Forbidden"}, 403

    # Get users
    return_list: list = []
    query = """SELECT user_id, user_email, user_first_name, user_middle_name, user_last_name, user_display_name, user_is_approved, user_rank, user_type FROM n_users_index ORDER BY user_first_name ASC"""
    rows = db.select(query=query)
    for row in rows:
        sql_user_id = row[0]
        sql_user_email = row[1]
        sql_user_first_name = row[2]
        sql_user_middle_name = row[3]
        sql_user_last_name = row[4]
        sql_user_display_name = row[5]
        sql_user_is_approved = row[6]
        sql_user_rank = row[7]
        sql_user_type = row[8]

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
            "user_type": sql_user_type
        }
        return_list.append(return_dict)

    # Give feedback
    return {"message": f"", "data": return_list, "error": ""}, 200
