'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

sana = 'banaani'
merkki = 'n'

i = 0
while i < len(sana) - 2:
    osajono = sana[i:i+3]
    if osajono[0] == merkki:
        print(osajono)

    i += 1
