import sqlite3

db = sqlite3.connect('MyDataBase.db')

c = db.cursor() # Created cursor

c.execute("""CREATE TABLE if not EXISTS testing(
    title VARCHAR(15),
    full_text VARCHAR(50),
    views BIGINT,
    author VARCHAR(20)
)""")

#c.execute("INSERT INTO articles VALUES('Google', 'Google description!', 80, 'FadeDragon')") #adding new data
#c.execute("DELETE FROM articles WHERE rowid = 2 ") #DELETE FROM DATA BASE
#c.execute("DELETE FROM articles") DELETING ALL DATA BASE!!

c.execute("UPDATE articles SET author = 'Updated_author' WHERE title = 'Google'") #Updating author

c.execute("SELECT rowid, * FROM articles")
print(c.fetchall()) #all entry's


c.execute("SELECT rowid, * FROM articles")
print(c.fetchone()[1]) #one enty


c.execute("SELECT rowid, * FROM articles")
print(c.fetchmany(2)) #x entry's



#select with criteria
title = input('Choose a title: ')
c.execute("SELECT * FROM articles WHERE title = ?", (title,)) #SQL injection defence

# SQL - <> PYTHON - !=

print(c.fetchall())

c.execute("SELECT * FROM articles ORDER BY views DESC")
print(c.fetchall())


db.commit()

db.close()

