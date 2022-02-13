'''
Tämä esimerkkitiedosto näyttää, miten voit selvittää toisen tiedoston
sijainnin suhteessa suoritettavaan Python-skriptiin pathlib:in avulla.

Käsiteltävien tiedostojen todellisen polun käyttäminen on kannattavaa, koska
tällöin ohjelmasi toiminta ei ole riippuvaista siitä, mistä hakemistosta käsin
ohjelma on käynnistetty.
'''
from pathlib import Path

# Luodaan polku 'tiedosto.txt'-tiedostoon hyödyntämällä tämän skritin sijaintia:
tiedosto = Path(__file__).resolve().parent / 'tiedosto.txt'

# Luetaan tiedosto ja tulostetaan sen sisältö:
print(tiedosto.read_text())
