'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.

Voit ajaa tämän "doctest"-testin komennolla: python -m doctest -v naapureita_listassa.py

>>> lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
>>> print(pisin_naapurijono(lista))
4
>>> on_naapurit(2, 3)
True
>>> on_naapurit(5, 3)
False
'''


def on_naapurit(a: int, b: int) -> bool:
    '''
    "Määritellään, että listan alkiot ovat naapureita, jos niiden erotus on 1.
    Naapureita olisivat siis esim alkiot 1 ja 2 tai alkiot 56 ja 55."
    '''
    return a == b-1 or a == b+1


def pisin_naapurijono(numerot: list) -> int:
    pisin = 1
    jonon_pituus = 1

    for i in range(1, len(numerot)):
        edellinen = numerot[i-1]
        nykyinen = numerot[i]

        if on_naapurit(edellinen, nykyinen):
            jonon_pituus += 1
        else:
            jonon_pituus = 1

        if jonon_pituus > pisin:
            pisin = jonon_pituus

    return pisin


if __name__ == '__main__':
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))
