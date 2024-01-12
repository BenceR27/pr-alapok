# feladat_027
# Lista bejárása index-szel I.

honapok = ['január', 'február','március', 'április', 'május', 'június']

index = 0
for honap in honapok:
    print(index, honap)
    index = index + 1

# ---------------------------------------

print("2. futás")
index = 0
for honap in honapok:
    print(f"A honapok lista indexe: {index}, eleme: {honap}")
    index = index + 1