# Tätä ette voi käyttää kurssin tehtävissä :(
from getpass import getpass

salasana = getpass('Salasana: ')
uudelleen = getpass('Toista salasana: ')

if salasana == uudelleen:
    print('Käyttäjätunnus luotu!')
else:
    print('Ei ollut sama!')
