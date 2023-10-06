#feladat_009

"""
Kérjuk be két egész számot, szam1 és szam2.
Hasonlítsuk össze a két számot, és irassuk ki, hogy 
a szam1 kisebb mint a szam2,
vagy a szam2 kisebb mint a szam1,
vagy a szam1 egyenlő szam2-vel
"""

szam1 = input("Írj be egy számot:")
szam2 = input("írj be mégegy számot:")
szam1 = int(szam1)
szam2 = int(szam2)

if szam1 > szam2:
    print(f"Az első szám a nagyobb")
elif szam1 < szam2:
    print(f"A második szám a nagyobb")
elif szam1 == szam2:
    print(f"A két szám egyenlő")

"""
if szam1 == szam2:
    print(f'A két szám egyenlő')
if szam1 < szam2:
    print(f'A második szám a nagyobb')
if szam1 > szam2:
    print(f'Az első szám a nagyobb')
"""
"""
if szam1 == szam2:
    print(f'A két szám egyenlő')
elif szam1 < szam2:
    print(f'A második szám a nagyobb')
else szam1 > szam2:
    print(f'Az első szám a nagyobb')
"""