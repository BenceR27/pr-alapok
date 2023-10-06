#feladat_004
#jegyek beolvasása

jegy = input("Kérem a jegyed")
jegy = int(jegy)

if jegy == 1:
    print(f"Elégtelen")
elif jegy == 2:
    print(f"Elégséges")
elif jegy == 3:
    print(f"közepes")
elif jegy == 4:
    print(f"jó")
elif jegy == 5:
    print(f"Kitűnő")
else:
    print(f"A jegyet nem ismerte fel a program")