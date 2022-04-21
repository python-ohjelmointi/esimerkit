'''
Tämä esimerkkitiedosto näyttää, miten voit selvittää haluamasi tiedoston
sijainnin suhteessa suoritettavaan Python-skriptiin pathlib:in avulla.

Käsiteltävien tiedostojen todellisen polun käyttäminen on kannattavaa, koska
tällöin ohjelmasi toiminta ei ole riippuvaista siitä, mistä hakemistosta käsin
ohjelma on käynnistetty.
'''
from pathlib import Path

# Luodaan polku 'nimet.csv'-tiedostoon hyödyntämällä tämän skritin sijaintia:
tiedosto = Path(__file__).resolve().parent / 'tiedostot' / 'nimet.csv'

# Luetaan tiedosto ja tulostetaan sen sisältö. Huom! Merkistöksi on määritetty utf-8:
print(tiedosto.read_text(encoding='UTF-8'))
