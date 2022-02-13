'''
Tämä esimerkkitiedosto näyttää, miten voit selvittää toisen tiedoston
sijainnin suhteessa suoritettavaan Python-skriptiin pathlib:in avulla.

Käsiteltävien tiedostojen todellisen polun käyttäminen on kannattavaa, koska 
tällöin ohjelmasi toiminta ei ole riippuvaista siitä, mistä hakemistosta käsin
ohjelma on käynnistetty.
'''
import pathlib

# Luodaan polku 'tiedosto.txt'-tiedostoon hyödyntämällä tämän skritin sijaintia:
p = pathlib.Path(__file__).resolve().parent / 'tiedosto.txt'

# Luetaan tiedosto, ja tulostaa sen sisältö:
print(p.read_text())
