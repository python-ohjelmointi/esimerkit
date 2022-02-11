tarina = ''
vanha_sana = ''

while True:
    sana = input('Anna sana: ')

    # jos sana on loppu, poistutaan silmukasta
    if sana == 'loppu' or vanha_sana == sana:
        break

    # ei tulosteta, vaan otetaan talteen
    tarina += sana + ' '

    vanha_sana = sana

# tulostetaan lopussa kaikki
print(tarina)
