'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

eka = input('Anna 1. sana: ')
toka = input('Anna 2. sana: ')

if eka.lower() < toka.lower():
    print(f'{toka} on viimeinen')
else:
    print(f'{eka} on viimeinen')
