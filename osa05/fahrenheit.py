'''
Tämä tiedosto sisältää "doctest"-testejä, jotka voit ajaa komennolla:

$ python3 -m doctest -v fahrenheit.py

Kirjoita funktio muunna_fahrenheitiksi, joka muuntaa sille annetun lämpötilan
Celsius-asteikosta Fahrenheit-asteikkoon, ja palauttaa tuloksen.

Muunnoskaava Celsius-asteikosta Fahrenheiteiksi on seuraava:

°F = (°C) * 1,8 + 32

Annettu lämpötila tulee siis kertoa luvulla 1,8 ja tulokseen tulee lisätä 32.

>>> muunna_fahrenheitiksi(55)
131.0
'''


def muunna_fahrenheitiksi(celsius: int) -> float:
    return celsius * 1.8 + 32
