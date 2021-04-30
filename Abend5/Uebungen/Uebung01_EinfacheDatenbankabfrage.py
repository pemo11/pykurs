# Übung Nr. 1 - Eine einfache Datenbankabfrage
import os
import sqlite3
from sqlite3 import Error

# Verschiedene Alternativen für die absolute Angabe eines Pfades
# dbPfad = "E:/2018/Pykiste/Datenbanken/PyMusik.db"
dbPfad = os.getcwd() +  "../Material/PyMusik.db"
dbPfad = os.path.dirname(__file__) + "/../Material/PyMusik.db"

try:
    # Verbindung herstellen
    conn = sqlite3.connect(dbPfad)
    # Cursor anlegen
    cursor = conn.cursor()
    # Ausführen des Cursors mit einer SQL-Anweisung
    sqlCmd = "Select * From Titel"
    cursor.execute(sqlCmd)
    # Alle Datensätze holen
    rows = cursor.fetchall()
    # Alle zurückgegebenenen Zeilen mit allen Feldern Zeile für Zeile ausgeben
    for row in rows:
        print(row[1])
except Error as e:
    print(e)
finally:
    conn.close()

