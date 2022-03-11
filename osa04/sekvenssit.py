# pylint: disable=consider-using-enumerate

def operaatiot(data):
    print('Alkuperäinen:', data)

    # Yhdisteleminen ja "kertominen"
    print('Yhdistely:   ', data + data)
    print('Kertominen:  ', data * 3)

    # Indeksit (kokonaislukuja) ja hakasulut
    print('Eka:         ', data[0])
    print('Toka:        ', data[1])
    print('Vika:        ', data[-1])

    # Osat saadaan hakasuluilla ja rajoilla
    print('Kaksi ekaa:  ', data[:2])
    print('Kaksi vikaa: ', data[-2:])

    # pituuden selvittäminen
    print('Pituus:      ', len(data))

    # in-operaatio etsii sisällöstä
    print('Löytyykö ti? ', 'ti' in data)

    # maksimi ja minimi
    print('Minimi:      ', min(data))
    print('Maksimi:     ', max(data))

    # läpikäynti yksi kerrallaan indeksin avulla
    for i in range(len(data)):
        print(i, data[i])
        i += 1


# merkkijonoilla
operaatiot('Python-ohjelmointi')

print('-' * 80)

# listoilla
viikonpaivat = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su']
operaatiot(viikonpaivat)

print('~' * 80)

numerot = [4, 18, 30, 6, 1, 9]
operaatiot(numerot)
