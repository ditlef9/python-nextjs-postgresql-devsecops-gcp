import base64
import html
import json

import jwt
from flask import request
from jwt import ExpiredSignatureError

from src.dao.db_adapter import DBAdapter


def validate_token(db: DBAdapter, jwt_secret_key: str):

    # Start token test
    token = None
    if "Authorization" not in request.headers.keys():
        print("validate_token()·No access token is set")
        return {
            "message": "No access token is set",
            "data": None,
            "error": "Unauthorized"
        }, 401

    # print(f"TokenFromGoogleWorkspace() :: validate_google_workspace_token() :: Split Authorization")
    if len(request.headers["Authorization"].split()) <= 1:
        print("validate_token()·No identity token provided")
        return {
            "message": "No identity token provided",
            "data": None,
            "error": "Unauthorized"
        }, 401
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        print("validate_token()·Authentication Token is missing")
        return {
            "message": "Authentication Token is missing!",
            "data": None,
            "error": "Unauthorized"
        }, 401

    # Check that token is base64 and can be decoded
    try:
        key_info = json.loads(base64.b64decode(token.split(".")[0] + "=========").decode("utf-8"))
        if key_info['alg'] != "HS256":
            print("validate_token()·Unknown alg") # noqa
            return {
                "message": "Something went wrong",
                "data": None,
                "error": ""
            }, 500
        if key_info['typ'] != "JWT":
            print("validate_token()·Unknown typ") # noqa
            return {
                "message": "Something went wrong",
                "data": None,
                "error": ""
            }, 500

    except Exception as e:
        print(f"validate_token()·Could not do json.loads(base64.b64decode(token.split(.)[0] + =========).decode(utf-8)) because: {e}") # noqa
        return {
            "message": "Something went wrong",
            "data": None,
            "error": str(e)
        }, 500

    # Decode
    jwt_decoded_dict: dict = {}
    try:
        # Decode and validate token
        jwt_decoded_dict = jwt.decode(token, jwt_secret_key, algorithms=["HS256"], options={"verify_at_hash": False})
    except ExpiredSignatureError:
        print("Token has expired")
        return {
            "message": "Token has expired",
            "data": None,
            "error": "Unauthorized"
        }, 401

    except Exception as e:
        print(f"validate_token()·Error: {e}")
        return {
            "message": "Something went wrong",
            "data": None,
            "error": str(e)
        }, 500

    # Find user in our database
    q: str = "SELECT user_id, user_email, user_first_name, user_middle_name, user_last_name, user_display_name, user_is_approved, user_rank FROM n_users_index WHERE user_id=:user_id AND user_email=:email"
    p: dict = {"user_id": jwt_decoded_dict['user_id'], "email": jwt_decoded_dict['user_email']}
    rows = db.select_where(query=q, parameters=p)
    rows_count = db.count_rows(rows)
    if rows_count == 0:
        print(f"validate_token() · Did not find user in database from the token") # noqa
        return {"message": f"User not found", "data": None, "error": "Conflict"}, 409
    sql_user_id = rows[0][0]
    sql_user_email = rows[0][1]
    sql_user_first_name = rows[0][2]
    sql_user_middle_name = rows[0][3]
    sql_user_last_name = rows[0][4]
    sql_user_display_name = rows[0][5]
    sql_user_is_approved = rows[0][6]
    sql_user_rank = rows[0][7]

    # Check that users is approved
    if not sql_user_is_approved:
        print(f"validate_token() · User {sql_user_id} is not approved") # noqa
        return {"message": f"User is not approved", "data": None, "error": "Unauthorized"}, 401

    # Everything OK
    print(f"validate_token() · Validated token to user {sql_user_id}")

    # Return OK
    return {"message": "",
            "data": {
                "my_user_id": sql_user_id,
                "my_user_email": sql_user_email,
                "my_user_first_name": sql_user_first_name,
                "my_user_middle_name": sql_user_middle_name,
                "my_user_last_name": sql_user_last_name,
                "my_user_display_name": sql_user_display_name,
                "my_user_is_approved": sql_user_is_approved,
                "my_user_rank": sql_user_rank
            },
            "error": "Success"}, 200
