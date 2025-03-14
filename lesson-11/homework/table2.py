import sqlite3
connection = sqlite3.connect("library.db")
cursor = connection.cursor()

cursor.execute("""
        CREATE TABLE Books(
            title TEXT,
            author TEXT,
            year_published INTEGER,
            genre TEXT,  
        ) 
""")
data = [("To Kill a Mockingbird","Harper Lee",1960,"Fiction"),("1984","George Orwell",1949,"Dystopian"),("The Great Gatsby","F. Scott Fitzgerald",1925,"Classic")]
cursor.executemany("INSERT INTO Books(title,author,year_published,genre) VALUES(?,?,?,?)",data)
cursor.execute("UPDATE Books SET year_published =? WHERE year_published=?",(1984,1950))
cursor.execute("DELETE FROM Books WHERE year_published<?",(1950))
cursor.execute("ALTER TABLE Books ADD COLUMN rating FLOAT")
ratings = [(4.8),(4.7),(4.5)]
cursor.executemany("UPDATE Books SET rating=?",ratings)
cursor.execute("SELECT * FROM Books ORDER BY year_published")
cursor.fetchall()
connection.commit()
connection.close()