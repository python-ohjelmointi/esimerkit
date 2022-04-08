'''
Kurssin materiaaleissa sudoku-ruudukko mallinnetaan kaksiulotteisilla
listoilla, joissa 0 tarkoittaa ruutua, jonka arvo ei ole vielä tiedossa.
Riippuen pelistä tai muusta mallinnettavasta ongelmasta "pelikenttä"
voi olla erittäin laaja, ja siellä voi olla hyvin vähän arvoja. Tällöin
kaikkien "tyhjien" ruutujen tallentaminen ei välttämättä ole mahdollista
saatika tehokasta.

Alla oleva esimerkki näyttää miten sudoku-ruudukko voitaisiin mallintaa
sanakirjan avulla. Sanakirjan avaimina käytetään tupleja (monikko), jossa
olevat kokonaisluvut määräävät x- ja y-koordinaatit. Arvoina ovat
vain tiedossa olevat pelin numerot.
'''

sudoku = {}

sudoku[0, 0] = 9
sudoku[4, 0] = 8
sudoku[6, 0] = 3
sudoku[3, 7] = 6
sudoku[8, 6] = 5

# Tulostetaan ruudukko (0, jos arvo ei ole tiedossa):
for y in range(9):
    for x in range(9):
        if (x, y) in sudoku:
            print(sudoku[x, y], end=' ')
        else:
            print(0, end=' ')
    print()
