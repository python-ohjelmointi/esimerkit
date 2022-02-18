'''
> "900-sarjan henkilötunnukset on tarkoitettu testauskäyttöön, ja ne täyttävät
> henkilötunnuksen muotovaatimukset, mutta ne eivät ole virallisia henkilötunnuksia."

https://www.kanta.fi/jarjestelmakehittajat/testiketti
'''
tunnus = '180202A9092'

paiva = int(tunnus[:2])
kk = int(tunnus[2:4])
vuosi = int(tunnus[4:6])
vuosisata = tunnus[6]
yksilonumero = int(tunnus[7:-1])

if vuosisata == '+':
    vuosi += 1800
elif vuosisata == '-':
    vuosi += 1900
elif vuosisata == 'A':
    vuosi += 2000

print(f'{paiva}.{kk}.{vuosi}')

if yksilonumero % 2 == 0:
    print('nainen')
else:
    print('mies')
