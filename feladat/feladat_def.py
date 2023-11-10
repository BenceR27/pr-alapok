# feladat_015
"""
Kérjük be a vezeték és keresztnevünket
Írassuk ki függvény segítségével a nevünket.
pl:
Be: "Kérem a vezetékneved: Takács"
Be: "Kérem a keresztneved: István"
Ki: "A nevem: Takács István"
"""

vnev = (input("Kérem a vezetékneved: "))
knev = (input("Kérem a keresztneved: "))

def nevf(vnev,knev):
    nevem = vnev + ' ' +knev
    return nevem

print(f"A nevem: {nevf(vnev,knev)}")