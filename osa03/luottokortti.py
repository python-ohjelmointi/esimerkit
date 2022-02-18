kortti = input('Syötä kortin numero: ')

if kortti[0] == '4':
    print('Visa!')
elif 51 <= int(kortti[0:2]) <= 55 or 2221 <= int(kortti[0:4]) <= 2720:
    print('MasterCard!')
else:
    print('Tuntematon kortti')

pituus = len(kortti)
print('*' * (pituus - 4) + kortti[-4:])
