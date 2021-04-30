# Function mit benannten Argumenten

# Ein Beispiel für eine Function mit Default-Parameter

def Kennwort(Anzahl=8,Alpa=False):
    import random
    Kennwort = ""
    # Geniale Syntax
    min, max = (48,91) if Alpa else (33,97)
    for i in range(Anzahl):
        Kennwort += chr(random.randint(min, max))
    return Kennwort


# Es gibt "jede Menge" Aufrufvarianten für eine Function
print(Kennwort(Anzahl=4))

print(Kennwort(6))

print(Kennwort(2,True))

print(Kennwort(Anzahl=24, Alpa=True))

# Die Reihenfolge der Parameter kann natürlich auch vertauscht werden
print(Kennwort(Alpa=True, Anzahl=10))

print(Kennwort())
