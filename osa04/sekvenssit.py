def operaatiot(teksti) -> None:
    print('Alkuperäinen:', teksti)

    # Yhdistäminen plussalla ja kertolaskuna
    print('Yhdistetty:  ', teksti + teksti)
    print('Kerrottu:    ', teksti * 3)

    # Indeksointi hakasuluilla ja kokonaisluvuilla
    print('Eka:         ', teksti[0])
    print('Toka:        ', teksti[1])
    print('Vika:        ', teksti[-1])

    # Pituus len-funktiolla
    print('Pituus:      ', len(teksti))

    # Osajonot hakasuluilla ja rajoilla
    print('Kaksi ekaa:  ', teksti[:2])
    print('Kaksi vikaa: ', teksti[-2:])

    # 'in' -operaatio etsii sisällöstä
    print('Löytyykö "ti"?', 'ti' in teksti)

    # max- ja min-operaatiot
    print('Minimi:      ', min(teksti))
    print('Maksimi:     ', max(teksti))

    # "iterointi" yksi pala kerrallaan
    print('Yksi kerrallaan: ')
    for i in range(len(teksti)):
        print(i, teksti[i])


operaatiot('Python-ohjelmointi')

print('-' * 80)

paivat = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su']
operaatiot(paivat)
