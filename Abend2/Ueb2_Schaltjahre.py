# Übung 2: Ausgabe aller Schaltjahre von 1900 bis 2200

for j in range(1900, 2200 + 1):
    schaltjahr = False
    if j % 4 == 0:
        schaltjahr = True
    if j % 100 == 0:
        schaltjahr = False
    if j % 400 == 0:
        schaltjahr = True

    if schaltjahr == True:
        print("%d ist ein Schaltjahr" % j)
