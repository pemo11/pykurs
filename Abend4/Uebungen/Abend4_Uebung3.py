# Anzeigen einer Liste als Balkendiagramm
import matplotlib.pyplot as plt

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

# Die Namen der Städte und die Einwohner müssen zwei Listen sein
namen = [s.Name for s in staedte]
einwohner = [s.Einwohner for s in staedte]

plt.bar(namen, einwohner)
plt.show()