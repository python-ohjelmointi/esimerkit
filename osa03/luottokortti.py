def tulosta_sensuroitu(teksti):
    pituus = len(teksti)
    print(teksti[:4] + '*' * (pituus - 8) + teksti[-4:])


if __name__ == '__main__':
    kortti = input('Syötä kortin numero: ')

    if kortti[0] == '4':
        print('Visa!')
    elif 51 <= int(kortti[0:2]) <= 55 or 2221 <= int(kortti[0:4]) <= 2720:
        print('MasterCard!')
    else:
        print('Tuntematon kortti')

    tulosta_sensuroitu(kortti)
