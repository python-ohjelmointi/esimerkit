'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.


Voit ajaa alla olevat doctest-testit komennolla:
$ python3 -m doctest -v poista_isot.py

>>> lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
>>> karsittu_lista = poista_isot(lista)
>>> print(karsittu_lista)
['def', 'pieni', 'toinen pieni', 'Osittain Iso']
'''


def poista_isot(sanat: list) -> list:
    ilman_isoja = []

    for sana in sanat:
        if not sana.isupper():
            ilman_isoja.append(sana)

    return ilman_isoja
