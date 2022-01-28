'''
Tämä skripti on vaihtoehtoinen ratkaisu tiedoston_koko.py-skriptille.
Vertailujen sijaan tässä ratkaisussa selvitetään ensin tiedoston kokoluokka
luvun 1024 kertoimina logaritmin avulla, jossa X = log(tavut, 1_024).

Tämän jälkeen koko jaetaan löydetyllä kokoluokalla 1024**X. Koon pääte (B, KB, MB..)
valitaan listalta, jossa kunkin päätteen indeksi on sen suuruutta vastaava luvun
1024 potenssi.
'''

from math import log

kertoimet = ['B', 'KB', 'MB', 'GB', 'TB']

tavut = int(input('Syötä tiedoston koko tavuina: '))

# kuinka monta kertaa 1024 pitää kertoa itsellään, jotta saadaan annetut tavut?
potenssi = int(log(tavut, 1_024))
koko = tavut / (1_024 ** potenssi)

print(f'Tiedoston koko on {koko:.2f} {kertoimet[potenssi]}')
