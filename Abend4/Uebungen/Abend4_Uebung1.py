# Wort-Umdreher-Function

def WortUmdreher1(Wort):
    NeuesWort = ""
    for i in range(len(Wort)-1, -1,-1):
        NeuesWort += Wort[i]
    return NeuesWort


print(WortUmdreher1("Sonne"))

def WortUmdreher2(Wort):
    l = list(Wort)
    l.reverse()
    return "".join(l)

print(WortUmdreher2("Sonne"))
