'''
Tämä tiedosto sisältää "doctest"-testejä, jotka voit ajaa komennolla:

$ python3 -m doctest -v lotto.py
'''


def poimi_numerot(teksti: str) -> list:
    '''
    Tämä metodi poimii annetusta merkkijonosta numerot,
    ja palauttaa ne uutena listana:

    >>> poimi_numerot('-3 2 5 7 9 11 123')
    [-3, 2, 5, 7, 9, 11, 123]
    '''
    osat = teksti.split(' ')
    numerot = []
    for x in osat:
        numerona = int(x)
        numerot.append(numerona)
    return numerot


def poimi_yhteiset(lista1: list, lista2: list) -> list:
    '''
    Poimii annetuista listoista arvot, jotka löytyvät molemmista
    listoista. Palauttaa yhteiset arvot uutena listana.

    >>> poimi_yhteiset([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9])
    [4, 5, 6]
    '''
    yhteiset = []
    for arvo1 in lista1:
        if arvo1 in lista2:
            yhteiset.append(arvo1)
    return yhteiset


def main():
    '''
    Pääohjelma on tässä toteutettu omaksi funktioksi,
    jotta siinä esitettävät muuttujat eivät olisi ns.
    "globaaleja".

    Katso: https://ohjelmointi-22.mooc.fi/osa-4/6-lisaa-rakenteista
    '''
    # 9 15 17 18 19 22 30 (lisänumero 11 ja plusnumero 29)
    oikea_rivi = input('Syötä oikea lottorivi: ')
    oikeat_numerot = poimi_numerot(oikea_rivi)

    lisanumero = int(input('Syötä lisänumero: '))
    plusnumero = int(input('Syötä plusnumero: '))

    while True:
        print()  # tyhjä rivi

        # 3 4 11 15 22 25 29
        oma_rivi = input('Syötä seuraava oma lottorivi: ')

        if oma_rivi == '':
            break

        omat_numerot = poimi_numerot(oma_rivi)

        yhteiset = poimi_yhteiset(oikeat_numerot, omat_numerot)
        print(f'{len(yhteiset)} oikeaa numeroa!')

        if lisanumero in omat_numerot:
            print('Lisänumero löytyy!')

        if plusnumero in omat_numerot:
            print('Plusnumero löytyy!')


if __name__ == '__main__':
    main()
    print('Loppu')
