'''
Tässä esimerkissä käytetään namedtuple-tyyppiä, joka yhdistää kokoelmien
ja "olioiden" hyviä puolia.

https://docs.python.org/3/library/collections.html#collections.namedtuple
'''

from collections import namedtuple


Henkilo = namedtuple('Henkilo', 'nimi ika kenka')

henkilot = [Henkilo("Anu", 10, 26), Henkilo("Petteri", 7, 22),
            Henkilo("Emilia", 32, 37), Henkilo("Antti", 39, 44)]

for henkilo in henkilot:
    print(f"{henkilo.nimi}: ikä {henkilo.ika} vuotta, kengännumero {henkilo.kenka}")
