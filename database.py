import sqlite3

connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

cursor.execute('pragma journal_mode=wal')
cursor.execute('.mode box')