import sqlite3

db = sqlite3.connect('MyDataBase.db')
c = db.cursor()

title = 'Hello!'
big_title = 'World!'
views = 50000
author = f'FADE'
#c.execute("INSERT INTO testing VALUES (?, ?, ?, ?)", (title, big_title, views, author))
c.execute("SELECT * FROM testing")
print(c.fetchall())

db.commit()

db.close()

