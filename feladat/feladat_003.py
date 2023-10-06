# feladat_003
# dk9 95-oldal
print(f'Üdv néked!')
évek_száma = input('Hány éves vagy? ')
évek_száma = int(évek_száma)
if évek_száma == 0:
    print(f"Még nem születttél meg")
elif évek_száma < 6:
    print(f"Még csak{évek_száma} éves vagy, még nem jársz általános iskolába!")
elif évek_száma >= 6 and évek_száma <= 14:
    print(f"Már {évek_száma} éves vagy, Általános iskolába jársz!")
elif évek_száma > 14 and évek_száma < 65:
    print(f"{évek_száma} Éves vagy, vagy tanulsz vagy dolgozol!")
else:
    print(f"{évek_száma} Éves vagy, nyugdíjas")
