#feladat_021
# egymásba ágyazott ciklusok II.

szam = int(input(f"Kérek egy PÁROS számot: "))
szam_fele = int(szam/2)

darab_karakter = 6
sor = 1
while sor <= szam_fele:
    oszlop = 1
    while oszlop <= szam_fele:
        print('I', end="")
        oszlop = oszlop + 1
    print("")
    darab_karakter = darab_karakter + 1
    sor = sor + 1

darab_karakter = 6
sor = 1
while sor <= szam_fele:
    oszlop = 1
    while oszlop <= szam_fele:
        print('I', end="")
        oszlop = oszlop + 1
    print("")
    darab_karakter = darab_karakter - 1
    sor = sor + 1 