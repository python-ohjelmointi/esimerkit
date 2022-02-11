'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

tarina = ''
vanha_sana = ''

while True:
    sana = input('Sana: ')

    if sana == 'loppu' or vanha_sana == sana:
        break

    tarina += sana + ' '
    vanha_sana = sana

# tulostetaan lopussa kaikki
print(tarina)
