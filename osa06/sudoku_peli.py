'''
Tämä tiedosto sisältää Sudoku-pelin käyttöliittymän, mutta se ei sisällä lainkaan
pelin logiikkaa. Logiikka on toteutettu aikaisemmissa viikkoharjoituksissa, ja
lisäksi pelin tueksi on toteutettu uudet sudoku_valmis-, ja tulotsa-funktiot.
'''
from sudoku_tarkistin import tulosta, sudoku_oikein, sudoku_valmis

# Sudoku-logo on luotu https://patorjk.com/software/taag/ -palvelussa.
logo = r'''
   _____             __        __
  / ___/ __  __ ____/ /____   / /__ __  __
  \__ \ / / / // __  // __ \ / //_// / / /
 ___/ // /_/ // /_/ // /_/ // ,<  / /_/ /
/____/ \__,_/ \__,_/ \____//_/|_| \__,_/

'''

# pelin alkutila on lainattu mooc.fi:n esimerkistä
sudoku = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
]


def kysy_numero(teksti: str) -> int:
    '''
    Pyytää käyttäjää syöttämään kokonaisluvun käyttäen
    annettua tekstiä. Toistaa kysymyksen kunnes saa
    kelvollisen kokonaisluvun, joka palautetaan.
    '''
    while True:
        try:
            numero = int(input(teksti))
            return numero
        except ValueError as virhe:
            print('Virheellinen numero!')
            print(virhe)


def pelaa():
    print(logo)

    while not sudoku_valmis(sudoku):
        tulosta(sudoku)
        print()

        rivi = kysy_numero('Syötä rivi: ')
        sarake = kysy_numero('Syötä sarake: ')
        numero = kysy_numero('Syötä numero: ')

        try:
            alkuperainen = sudoku[rivi][sarake]
            sudoku[rivi][sarake] = numero

            if sudoku_oikein(sudoku):
                print('OK!')
            else:
                print('Ei sallittu numero!')
                sudoku[rivi][sarake] = alkuperainen

        except IndexError:
            print('Virheellinen rivi tai sarake!')

        print()


if __name__ == '__main__':
    try:
        pelaa()
        print('Sait sudokun valmiiksi!')

    except KeyboardInterrupt:
        print()
        print('Kiitos pelaamisesta!')
