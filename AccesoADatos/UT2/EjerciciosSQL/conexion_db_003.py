import sqlite3

with sqlite3.connect("chinook.sqlite") as conn:
    cursor = conn.cursor()
    cursor.execute(''' SELECT name FROM sqlite_master WHERE type='table' ''')
    resultado = cursor.fetchall()

    print(resultado)