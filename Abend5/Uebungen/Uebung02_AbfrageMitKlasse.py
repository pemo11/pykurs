# Übung Nr. 2 - Eine Datenbankabfrage mit Objekten pro Datensatz
import os
import sqlite3
from sqlite3 import Error

# Verschiedene Alternativen für die absolute Angabe eines Pfades
dbPfad = "E:/2018/Pykiste/Datenbanken/PyMusik.db"
dbPfad = os.getcwd() +  "/Datenbanken/PyMusik.db"
dbPfad = os.path.dirname(__file__) + "/../Material/PyMusik.db"

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
    sqlCmd = "Select * From Titel"
    cursor.execute(sqlCmd)
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

