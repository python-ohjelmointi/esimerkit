'''
Tämä tiedosto sisältää "doctest"-testejä, jotka voit ajaa komennolla:

$ python3 -m doctest -v arvosanat.py

Toteuta funktio arvosanojen_keskiarvo, joka saa parametrinaan listan kokonaislukuja,
ja palauttaa niiden keskiarvon. Erikoisuutena arvosanojen keskiarvoja laskettaessa
nollat tulee jättää huomioimatta.

>>> arvosanojen_keskiarvo([1, 2, 3])
2.0

>>> arvosanojen_keskiarvo([0, 1, 0, 2, 0, 3])
2.0
'''


from statistics import mean


def arvosanojen_keskiarvo(arvosanat: list) -> float:
    # tehdään kopio listasta, jotta nollien poistaminen
    # ei aiheuta bugeja muualle:
    ilman_nollia = list(arvosanat)
    while 0 in ilman_nollia:
        ilman_nollia.remove(0)

    # "Mean" eli keskiarvo.
    # Kerrotaan 1.0:lla, jotta saadaan aina liukuluku:
    return mean(ilman_nollia) * 1.0


if __name__ == '__main__':
    numerot = [0, 1, 5, 5, 0, 2, 0, 3, 4, 5, 5, 5, 4, 4, 3, 2, 5, 5]

    print(f'Arvosanat: {numerot}')
    print(f'Keskiarvo: {arvosanojen_keskiarvo(numerot):.2f}')
    print('Jakauma:')

    for i in range(6):
        print(f' {i}: {"*" * numerot.count(i)}')
