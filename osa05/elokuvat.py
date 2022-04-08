'''
Tässä esimerkissä käytetään namedtuple-tyyppiä, joka yhdistää kokoelmien
ja "olioiden" hyviä puolia.

https://docs.python.org/3/library/collections.html#collections.namedtuple
'''

from collections import namedtuple

Elokuva = namedtuple('Elokuva', 'nimi ohjaaja vuosi pituus')

leffa = Elokuva('Pythonin viemää', 'Pekka Python', 2017, 116)
print(leffa.nimi)
print(leffa.vuosi)


def tulosta_elokuva(elokuva: Elokuva):
    print(f'{elokuva.nimi}, {elokuva.ohjaaja}')


tulosta_elokuva(leffa)
