# Einlesen einer Textdatei als Objekte

class Stadt:

    def __init__(self, Name, Einwohner):
        self.Name = Name
        self.Einwohner = Einwohner

staedte = []

with open("Städte.txt") as fh:
    for zeile in fh:
        name = zeile.split(",")[0]
        einwohner = int(zeile.split(",")[1])
        s = Stadt(name, einwohner)
        staedte.append(s)

print(staedte)
