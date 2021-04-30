# Die formatierte Ausgabe von Zahlen

# Die klassische Formatierung wie bei der Programmiersprache C

wert = 22 / 7

print("Das Ergebnis ist %.2f" % wert)

# Die etwas modernere Formatierung ueber das format()-Attribut eines Strings (str)

print("Das Ergebnis ist {:.3f}".format(wert))

# Die moderne Formatierung seit Python 3.6 mit dem f-Praefix

print(f"Das Ergebnis ist {wert:.4f}")
