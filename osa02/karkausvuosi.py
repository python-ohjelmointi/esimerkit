'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

vuosi = 2004
seuraava = vuosi + 1

while True:
    if seuraava % 4 == 0 and (seuraava % 100 != 0 or seuraava % 400 == 0):
        print(f'{seuraava} on karkausvuosi')
        break

    seuraava += 1
