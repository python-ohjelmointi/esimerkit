'''
Tämä tiedosto sisältää "doctest"-testejä, jotka voit ajaa komennolla:

$ python3 -m doctest -v paivamaara.py
'''

from datetime import datetime

PAIVAT = 'Maanantai Tiistai Keskiviikko Torstai Perjantai Lauantai Sunnuntai'.split()
KUUKAUDET = 'tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu'.split()


def muodosta_paivays(pvm: datetime) -> str:
    '''
    Muodostaa ja palauttaa suomenkielisen päivämäärätekstin
    annetulle datetime-oliolle.

    >>> muodosta_paivays(datetime(2022, 3, 18))
    'Perjantai 18. maaliskuuta 2022'

    >>> muodosta_paivays(datetime(2022, 1, 19))
    'Keskiviikko 19. tammikuuta 2022'
    '''
    kuukausi = pvm.month            # tammi = 1
    viikonpaiva = pvm.isoweekday()  # ma = 1

    return f'{PAIVAT[viikonpaiva-1]} {pvm.day}. {KUUKAUDET[kuukausi-1]}kuuta {pvm.year}'


if __name__ == '__main__':
    nyt = datetime.now()
    print(muodosta_paivays(nyt))
