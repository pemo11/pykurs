# Übung Nr. 4: Zusammenstellen einer Playlist
import os
import sqlite3
from sqlite3 import Error

# Der Pfad der Datei PyMusik.db wird zusammengesetzt
dbPfad = os.path.dirname(__file__) + "/Material/PyMusik.db"

jahr = input("Jahr? (z.B. 1985)")
kategorie = input("Musikrichtung? (z.B. Rock oder Pop)")

playList = []

class Titel:

    def __init__(self, titel, interpret, jahr, kategorie, laenge):
        self.Titel = titel
        self.Interpret = interpret
        self.Kategorie = kategorie
        self.Laenge = laenge
        self.Jahr = jahr
    
    def __eq__(self, other):
        return self.Titel == other.Titel

    def toString(self):
        return f"Titel: {self.Titel} Interpret: {self.Interpret} Jahr: {self.Jahr}"

try:
    # Verbindung herstellen
    conn = sqlite3.connect(dbPfad)
    # Cursor anlegen
    cursor = conn.cursor()
    # Ausführen des Cursors mit einer SQL-Anweisung
    sqlCmd = "Select * From Titel Where Jahr=? and Kategorie=?"
    cursor.execute(sqlCmd, [jahr,kategorie])
    # Alle Datensätze holen
    rows = cursor.fetchall()
    # Alle zurückgegebenenen Zeilen mit allen Feldern Zeile für Zeile ausgeben
    for row in rows:
        neuerTitel = Titel(row[1],row[2],row[3],row[4],row[6])
        playList.append(neuerTitel)
except Error as e:
    print(e)
finally:
    conn.close()

for titel in playList:
    print(titel.toString())

