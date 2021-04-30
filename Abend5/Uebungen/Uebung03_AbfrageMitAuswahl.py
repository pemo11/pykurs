# Übung Nr. 3: Eine Datenbankabfrage mit Filter
import os
import sqlite3
from sqlite3 import Error

# Wichtig: Die Pfadangabe muss noch geändert werden
dbPfad = os.path.dirname(__file__) + "/../Material/PyMusik.db"

jahr = input("Jahr? (z.B. 1985)")

titelListe = []

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
    sqlCmd = "Select * From Titel Where Jahr=?"
    # Wichtig: Alle Parameter, auch wenn es nur einer ist, müssen als Liste übergeben werden
    # daher []
    cursor.execute(sqlCmd, [jahr])
    # Alle Datensätze holen
    rows = cursor.fetchall()
    # Alle zurückgegebenenen Zeilen mit allen Feldern Zeile für Zeile ausgeben
    for row in rows:
        neuerTitel = Titel(row[1],row[2],row[3],row[4],row[6])
        titelListe.append(neuerTitel)
except Error as e:
    print(e)
finally:
    conn.close()

for titel in titelListe:
    print(titel.toString())

