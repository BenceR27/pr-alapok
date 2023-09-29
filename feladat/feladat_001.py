#feladat_001
"""
Kérjük be a billentyűzetről a nevünket, és irassuk ki a képernyőre!
A billentyűzetről mindik szöveget (string-et) olvasunk be!
type(változó) --- visszaadja a változó tipusát    
"""

nev=input("Kérek egy nevet: ")
print(f"A megadott név a következő: {nev}")

vnev = input("Kérek egy vezetéknevet: ")
knev = input("Kérek egy keresztnevet: ")
print(f"A megadott név a következő: {vnev} {knev}")

print(f"A vnev változó típusa : {type(vnev)}")
print(f"A knev véltozó típusa : {type(knev)}")