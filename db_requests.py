import sqlite3
from datetime import date, timedelta

def adapt_date_iso(val):
    """Adapt datetime.date to ISO 8601 date."""
    return val.isoformat()

def hackernews_today(n=15):
    connection = sqlite3.connect('news_articles.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title, link from hacker_news WHERE date = ? ORDER BY votes desc LIMIT ?',(adapt_date_iso(date.today()), n))
    data = cursor.fetchall()
    return data

def hackernews_yesterday(n=15):
    connection = sqlite3.connect('news_articles.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title, link from hacker_news WHERE date = ? ORDER BY votes desc LIMIT ?',(adapt_date_iso(date.today() - timedelta(days = 1)), n))
    data = cursor.fetchall()
    return data

if __name__ == "__main__":
    print(hackernews_today())