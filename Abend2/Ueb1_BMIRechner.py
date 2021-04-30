# Übung 1: Ein BMI-Rechner
# Das klassische EVA-Prinzip  Eingabe = Gewicht, Größe, Geschlecht - Verarbeitung - Ausgabe = BMI-Wert
import math

gewicht = input("Gewicht in kg?")
groesse = input("Groesse in cm?")
geschlecht = input("Geschlecht? (m/w/x)?")

# Zuerst die ganz einfache Variante
bmi = float(gewicht) / math.pow(int(groesse) / 100, 2)

if geschlecht == "m":
    if bmi < 20:
        gewichtsKategorie = "Untergewicht"
    elif bmi < 25:
        gewichtsKategorie = "Normalgewicht"
    elif bmi < 30:
        gewichtsKategorie = "übergewicht"
    elif bmi < 40:
        gewichtsKategorie = "Adipositas"
    else:
        gewichtsKategorie = "Massive Adipositas"
elif geschlecht == "w":
    if bmi < 19:
        gewichtsKategorie = "Untergewicht"
    elif bmi < 24:
        gewichtsKategorie = "Normalgewicht"
    elif bmi < 30:
        gewichtsKategorie = "übergewicht"
    elif bmi < 40:
        gewichtsKategorie = "Adipositas"
    else:
        gewichtsKategorie = "Massive Adipositas"
else:
    pass

print("Mit einem BMI von " + str(bmi)  + " hast Du " + gewichtsKategorie)

