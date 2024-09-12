import sqlite3
from HN_scraper import create_custom_hn, get_data
from datetime import date


def adapt_date_iso(val):
    """Adapt datetime.date to ISO 8601 date."""
    return val.isoformat()

connection = sqlite3.connect('news_articles.db')
cursor = connection.cursor()

cursor.execute('pragma journal_mode=wal')

cursor.execute('''CREATE TABLE IF NOT EXISTS hacker_news(id integer primary key not null,
               title varchar not null unique,
               date varchar, 
               link varchar,
               votes integer)
               ''')
links, subtext = get_data()
news_list = create_custom_hn(links,subtext)
for article in news_list:
    cursor.execute('INSERT OR IGNORE INTO hacker_news (title, date, link, votes) VALUES (?, ?, ?, ?)', 
                   (article['title'], adapt_date_iso(date.today()), article['link'],article['votes']))


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()