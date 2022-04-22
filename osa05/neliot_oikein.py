'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.

Voit ajaa tämän "doctest"-testin komennolla: python -m doctest -v neliot_oikein.py

>>> sudoku = [
...     [9, 0, 0, 0, 8, 0, 3, 0, 0],
...     [2, 0, 0, 2, 5, 0, 7, 0, 0],
...     [0, 2, 0, 3, 0, 0, 0, 0, 4],
...     [2, 9, 4, 0, 0, 0, 0, 0, 0],
...     [0, 0, 0, 7, 3, 0, 5, 6, 0],
...     [7, 0, 5, 0, 6, 0, 4, 0, 0],
...     [0, 0, 7, 8, 0, 3, 9, 0, 0],
...     [0, 0, 1, 0, 0, 0, 0, 0, 3],
...     [3, 0, 0, 0, 0, 0, 0, 0, 2]
... ]
>>> nelion_numerot(sudoku, 0, 0)
[9, 2, 2]
>>> nelion_numerot(sudoku, 3, 3)
[7, 3, 6]
>>> nelio_oikein(sudoku, 0, 0)
False
>>> nelio_oikein(sudoku, 1, 3)
True
'''


def nelio_oikein(sudoku: list, rivi: int, sarake: int) -> bool:
    '''
    Tarkastaa ettei annetun sudokun 3x3 -kokoisessa osassa ole mitään numeroa 1-9
    yli yhtä kertaa.
    '''
    numerot = nelion_numerot(sudoku, rivi, sarake)

    for i in range(1, 10):
        if numerot.count(i) > 1:
            return False
    return True


def nelion_numerot(sudoku: list, rivi: int, sarake: int) -> list:
    '''
    Palauttaa annetusta sudoku-ruudukosta numerot, jotka kuuluvat 3x3-neliöön,
    jonka yläkulma määräytyy annetun rivin ja sarakkeen mukaan. Nollia ei palauteta.
    '''
    numerot = []
    for y in range(rivi, rivi + 3):
        for x in range(sarake, sarake + 3):
            numero = sudoku[y][x]
            if numero > 0:
                numerot.append(numero)
    return numerot
