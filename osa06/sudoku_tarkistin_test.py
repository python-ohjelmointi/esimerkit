'''
Tämä tiedosto sisältää pytest-testejä.

Pytest voidaan asentaa komennolla `python -m pip install pytest`
Testit voidaan ajaa komennolla `python -m pytest sudoku_tarkistin_test.py`

'''

from sudoku_tarkistin import rivi_oikein, sarake_oikein, sudoku_oikein, sudoku_valmis, nelio_oikein


sudoku = [
    [2, 6, 7, 8, 3, 9, 5, 1, 4],  # täysi ja validi rivi
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 1, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 4, 1]  # rivillä 2 kpl numeroa 4
]  # _________^ tässä sarakkeessa on 2 kpl numeroa 1


def test_taysi_validi_rivi():
    tulos = rivi_oikein(sudoku, 0)

    assert tulos is True


def test_samalla_rivilla_monta_nelosta():
    tulos = rivi_oikein(sudoku, 8)

    assert tulos is False


def test_validi_sarake():
    tulos = sarake_oikein(sudoku, 0)

    assert tulos is True


def test_epavalidi_sarake():
    tulos = sarake_oikein(sudoku, 3)

    assert tulos is False


def test_validi_nelio():
    tulos = nelio_oikein(sudoku, 0, 0)

    assert tulos is True


def test_nelio_jossa_monta_ykkosta():
    tulos = nelio_oikein(sudoku, 3, 3)

    assert tulos is False


def test_sudoku_ei_ole_oikein():
    tulos = sudoku_oikein(sudoku)

    assert tulos is False


def test_sudoku_ei_valmis():
    tulos = sudoku_valmis(sudoku)

    assert tulos is False

# TODO: testaa täysi ruudukko ja `sudoku_valmis`
# TODO: testaa validi ruudukko ja `sudoku_oikein`
