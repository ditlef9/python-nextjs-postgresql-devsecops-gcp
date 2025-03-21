# src/api/news/delete_news.py
import html
import re


from flask import request

from src.dao.db_adapter import DBAdapter
import bcrypt

from src.utils.get_datetime import get_datetime
from src.utils.validate_token import validate_token


def delete_news(db: DBAdapter, jwt_secret_key: str, get_news_id: int):
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
        return {"message": f"Only admin and owner can delete news", "data": None, "error": "Forbidden"}, 403


    # Get news
    query: str = """SELECT news_id, news_title, news_title_slug, news_text, news_created_timestamp, 
               news_created_by_user_id, news_created_by_display_name, news_updated_timestamp, news_updated_by_user_id, news_updated_by_display_name 
               FROM n_news_index 
               WHERE news_id=:news_id"""
    parameters: dict = {"news_id": get_news_id}
    rows = db.select_where(query=query, parameters=parameters)
    rows_count = db.count_rows(rows)
    if rows_count == 0:
        return {"message": f"News not found", "data": None, "error": "Not found"}, 404
    sql_news_id = rows[0][0]
    sql_news_title = rows[0][1]
    sql_news_title_slug = rows[0][2]
    sql_news_text = rows[0][3]
    sql_news_created_timestamp = rows[0][4]
    sql_news_created_by_user_id = rows[0][5]
    sql_news_created_by_display_name = rows[0][6]
    sql_news_updated_timestamp = rows[0][7]
    sql_news_updated_by_user_id = rows[0][8]

    # Check that we have written the ID
    json_data = request.get_json()
    post_news_id = json_data.get('news_id')
    if post_news_id == "":
        return {"message": f"ID is blank", "data": None, "error": "Payment Required"}, 402
    if int(post_news_id) != sql_news_id:
        return {"message": f"ID is wrong", "data": None, "error": "Payment Required"}, 402

    # Delete news
    query: str = """DELETE FROM n_news_index 
                WHERE news_id=:news_id"""
    parameters: dict = {
        "news_id": sql_news_id
    }
    db.update(query=query, parameters=parameters)

    # Give feedback
    return {"message": f"Deleted", "data": None, "error": ""}, 200
