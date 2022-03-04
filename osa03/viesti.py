def viesti():
    print("Tämä on oma funktio!")


def huuda(teksti):
    print(teksti.upper().replace('.', '!') + '!!!1!!')


def kuiskaa(lause):
    print(lause.lower().replace('!', '.'))


viesti()
huuda('Hyvää huomenta.')
kuiskaa('Syömään!!!')
