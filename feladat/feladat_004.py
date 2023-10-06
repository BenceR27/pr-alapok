# dk9 104-oldal
from xml.dom.minidom import Identified


IDEI_EV = 2023
felhasznalo_kora = input('hány éves vagy')
print(f"The most {felhasznalo_kora} éves vagy")
felhasznalo_kora = int(felhasznalo_kora)
szuletesi_ev = IDEI_EV - felhasznalo_kora
print(f'Te ekkor születtél: {szuletesi_ev}')