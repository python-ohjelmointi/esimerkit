from math import sqrt

a = int(input('Anna a: '))
b = int(input('Anna b: '))
c = int(input('Anna c: '))

x0 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
x1 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)

# Kolme eri tapaa tulostaa numeroita osana lausetta.
# Kaikki seuraavat rivit tulostavat täsmälleen saman tuloksen.
print('Juuret ovat', x0, 'ja', x1)
print('Juuret ovat ' + str(x0) + ' ja ' + str(x1))
print(f'Juuret ovat {x0} ja {x1}')
