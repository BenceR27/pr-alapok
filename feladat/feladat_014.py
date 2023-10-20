# feladat_014
"""
Kérjük be a vezeték és keresztnevünket
Írassuk ki eljárás segítségével a nevünket.
pl:
Be: "Kérem a vezetékneved: Takács"
Be: "Kérem a keresztneved: István"
Ki: "A nevem: Takács István"
"""

vnev = (input("Kérem a vezetékneved "))
knev = (input("Kérem a keresztneved "))

def neved(vnev,knev):
    print(f"A neved {vnev} {knev}")

neved(vnev,knev)