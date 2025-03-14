import sqlite3
connection = sqlite3.connect("roster.db")
cursor = connection.cursor()

cursor.execute("""
        CREATE TABLE Roster(
            name TEXT,
            species TEXT,
            age INTEGER,
        )
""")

data = [("Benjamin Sisko","Human",40),("Jadzia Dax","Trill",300),("Kira Nerys","Bajoran",29)]
cursor.executemany("INSERT INTO Roster(name,species,age) VALUES(?,?,?)",data)
cursor.execute("UPDATE Roster SET name=? WHERE name=?",("Jadzia Dax","Ezri Dax"))
cursor.execute("SELECT name,age FROM Roster WHERE species=?",("Bajoran"))
cursor.execute("DELETE FORM Roster WHERE age>100")
rank_data = [("Captain"),("Lieutenant"),("Major")]
cursor.execute("ALTER TABLE Roster ADD COLUMN rank TEXT")
cursor.execute("UPDATE Roster SET rank = ?", (rank_data,))
cursor.execute("SELECT * FROM Roster ORDER BY age DESC")
cursor.fetchall()
connection.commit()
connection.close()