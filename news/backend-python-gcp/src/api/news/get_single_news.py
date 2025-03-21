# src/api/news/get_single_news.py

from src.dao.db_adapter import DBAdapter

from src.utils.get_datetime import get_datetime


def get_single_news(db: DBAdapter, jwt_secret_key: str, get_news_id: int):

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

    # Transform to dict
    return_dict = {
        "news_id": sql_news_id,
        "news_title": sql_news_title,
        "news_title_slug": sql_news_title_slug,
        "news_text": sql_news_text,
        "news_created_timestamp": sql_news_created_timestamp,
        "news_created_by_user_id": sql_news_created_by_user_id,
        "news_created_by_display_name": sql_news_created_by_display_name,
        "news_updated_timestamp": sql_news_updated_timestamp,
        "news_updated_by_user_id": sql_news_updated_by_user_id
    }

    # Give feedback
    return {"message": f"", "data": return_dict, "error": ""}, 200
