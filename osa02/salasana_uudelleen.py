'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

# getpass ei toimi kurssin tehtävissä, käyttäkää siellä input-funktiota
from getpass import getpass

salasana = getpass('Salasana: ')
uudelleen = getpass('Toista salasana: ')

if salasana == uudelleen:
    print('Käyttäjätunnus luotu!')
else:
    print('Ei ollut sama!')
