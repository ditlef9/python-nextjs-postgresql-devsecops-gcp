# src/api/news/get_all_news.py

from src.dao.db_adapter import DBAdapter

from src.utils.get_datetime import get_datetime


def get_all_news(db: DBAdapter):

    # Datetime
    dt = get_datetime()

    # Get news
    return_list: list = []
    query = """SELECT news_id, news_title, news_title_slug, news_text, news_created_timestamp, 
               news_created_by_user_id, news_created_by_display_name, news_updated_timestamp, news_updated_by_user_id, news_updated_by_display_name 
               FROM n_news_index ORDER BY news_id DESC"""
    rows = db.select(query=query)
    for row in rows:
        sql_news_id = row[0]
        sql_news_title = row[1]
        sql_news_title_slug = row[2]
        sql_news_text = row[3]
        sql_news_created_timestamp = row[4]
        sql_news_created_by_user_id = row[5]
        sql_news_created_by_display_name = row[6]
        sql_news_updated_timestamp = row[7]
        sql_news_updated_by_user_id = row[8]

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
        return_list.append(return_dict)

    # Give feedback
    return {"message": f"", "data": return_list, "error": ""}, 200
