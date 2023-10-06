#feladat_005

"""
Amikor karakterlánccá  alakítunk, az str utasításra van szükség.
"""
felhasznalo_kora = 16
print(f'A felhasznalo_kora változó típusa: {type(felhasznalo_kora)}')
felhasznalo_kora = str(felhasznalo_kora)
print(f'A felhasznalo_kora változó típúsa: {type(felhasznalo_kora)}')
ilyen = input('És milyen ' + felhasznalo_kora + 'évesnek lenni?')
olyan = input(f'És milyen {felhasznalo_kora} évesnek lenni?')