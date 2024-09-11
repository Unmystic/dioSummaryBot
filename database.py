import sqlite3
from HN_scraper import create_custom_hn, get_data
from datetime import date

connection = sqlite3.connect('news_articles.db')
cursor = connection.cursor()

cursor.execute('pragma journal_mode=wal')

cursor.execute('''CREATE TABLE IF NOT EXISTS hackernews(id integer primary key not null,
               title varchar not null,
               date varchar, 
               link varchar,
               votes integer)
               ''')
links, subtext = get_data()
news_list = create_custom_hn(links,subtext)
for article in news_list:
    cursor.execute('INSERT OR IGNORE INTO hackernews (title, date, link, votes) VALUES (?, ?, ?, ?)', 
                   (article['title'], date.today(), article['link'],article['votes']))


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()