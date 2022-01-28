'''
Tämä esimerkkiohjelma demonstroi merkkijonojen ja kokonaislukujen vertailua.
Oikea koodi on ilmaistu kokonaislukuna, ja käyttäjän syöte luetaan aina sisään
ohjelmaan merkkijonona. Vertailu ei toimi, vaan oikea_koodi tulisi muuttaa
merkkijonoksi ennen vertailua. Myös syötetyn koodin muuttaminen numeroksi
auttaa, mutta tällöin kadotetaan mahdolliset pin-koodissa olevat etunollat.
'''

oikea_koodi = 6661

koodi = input('Syötä pin-koodi: ')

if koodi == oikea_koodi:
    print('Oikea koodi!')
else:
    print('Väärä koodi!')
