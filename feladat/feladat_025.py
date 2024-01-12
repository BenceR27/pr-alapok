# feladat_025

tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']
szamlalo = 0
index = 0
for tantargy in tantargyak:
    print(f"A tantargyak lista {index}. indexű eleme: {tantargyak}")
    szamlalo = szamlalo + 1
    index = index + 1
print(f"{szamlalo} eleme van a tantargyak listának")