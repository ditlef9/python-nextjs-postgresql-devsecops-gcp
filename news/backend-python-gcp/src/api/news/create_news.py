# src/api/news/create_news.py
import html
import re

from flask import request

from src.dao.db_adapter import DBAdapter
import bcrypt

from src.utils.get_datetime import get_datetime
from src.utils.validate_token import validate_token


def create_news(db: DBAdapter, jwt_secret_key: str):
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
        return {"message": f"Only admin and owner can create news", "data": None, "error": "Forbidden"}, 403

    # Datetime
    dt = get_datetime()

    # Post variables
    json_data = request.get_json()

    # news_title
    post_title = json_data.get('news_title')
    if post_title == "":
        return {"message": f"title is blank", "data": None, "error": "Payment Required"}, 402
    post_title = html.escape(s=post_title, quote=True)
    post_title = post_title.strip()

    # Slug
    post_title_slug = re.sub(r'[^a-z0-9]+', '-', post_title).strip('-').lower()

    # news_text
    post_text = json_data.get('news_text')
    if post_text == "":
        return {"message": f"Text is blank", "data": None, "error": "Payment Required"}, 402
    post_text = html.escape(s=post_text, quote=True)
    post_text = post_text.strip()

    # Insert news
    query: str = """INSERT INTO n_news_index (
                news_title, news_title_slug, news_text, news_created_timestamp, news_created_by_user_id,
                news_created_by_display_name) 
                VALUES (
                :title, :title_slug, :text, :created_timestamp, :created_by_user_id,
                :created_by_display_name
                )"""
    parameters: dict = {
        "title": post_title,
        "title_slug": post_title_slug,
        "text": post_text,
        "created_timestamp": dt['ymdhms'],
        "created_by_user_id": my_user_id,
        "created_by_display_name": my_user_display_name
    }
    db.insert(query=query, parameters=parameters)

    # get ID
    query = """SELECT news_id FROM n_news_index WHERE news_created_timestamp=:news_created_timestamp"""
    parameters: dict = {"news_created_timestamp": dt['ymdhms']}
    rows = db.select_where(query=query, parameters=parameters)
    if len(rows) == 0:
        return {"message": f"New news not found - Programming error", "data": None, "error": "Not Found"}, 404
    sql_news_id = rows[0][0]

    print(f"create_news()·New news registered with new id: {sql_news_id}")

    # Give feedback
    return {"message": f"Created {dt['ymdhms_saying']}", "data": {"news_id": sql_news_id}, "error": ""}, 200
