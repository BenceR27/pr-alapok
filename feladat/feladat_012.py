# feladat_012
# be: pozitív egész 
# ki: a szám páros vagy páratlan
szam = int(input("Kérek egy egész számot: "))
"""
if szam % 2 == 0:
    print(f"A számod {szam} páros!")
else:
    print(f"A számod {szam} páratlan!")
"""
"""
if szam % 2 == 0:
    print(f"A számod {szam} páros!")
elif szam % 2 == 1:
    print(f"A számod {szam} páratlan!")
"""
"""
if szam % 2 == 0:
    print(f"A számod {szam} páros!")
elif szam % 2 != 0:
    print(f"A számod {szam} páratlan!")
"""
if szam % 2 == 0:
    print(f"A számod {szam} páros!")
if szam % 2 == 1:
    print(f"A számod {szam} páratlan!")