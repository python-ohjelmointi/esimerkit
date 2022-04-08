'''
Tuple eli monikko
'''

# Tuple voidaan yksinkertaisimmillaan
# määritellä pilkuilla eroteltuina arvoina:
luvut = 1, 2, 3, 8, 9, 10, 4, 5, 6, 7
print(type(luvut))

# Tuplen tuloste muistuttaa paljolti listaa:
print(luvut)

# Tuplea voidaan käyttää hyvin
# samankaltaisesti kuin muita sekvenssejä:
print(luvut[2:])

for num in luvut:
    print(num)
