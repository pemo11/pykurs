# Übung 3: Zahlenraten
# "Der Computer denkt sich" eine Zahl von 1 bis 1024 - diese soll mit möglichst wenig Versuchen erraten werden
# Zufallszahlen werden mit der randint()-Function aus dem random-Modul erzeugt
import random

geheimZahl = random.randint(1,1025)

while True:
    zahl = int(input("Gibt eine Zahl zwischen 1 und 1024 ein: "))

    if zahl < geheimZahl:
        print("Diese Zahl ist zu klein")
    elif zahl > geheimZahl:
        print("Diese Zahl ist zu groß")
    else:
        print("Diese Zahl ist richtig")
        

# Erweiterungen:
# 1) Nach dem Erraten der Zahl, soll die Eingabe abgebrochen werden
# 2) Es soll die Anzahl der Versuche ausgegeben werden
# 3) Nach 20 Versuchen wird das Spiel beendet und die Zahl wird ausgegeben
