'''
Tuple eli monikko
'''

luvut = 1, 2, 3, 8, 9, 10, 4, 5, 6, 7

print(luvut)
print(type(luvut))

# tuplea voidaan käyttää hyvin
# samankaltaisesti kuin muita sekvenssejä:
print(luvut[2:])

for num in luvut:
    print(num)
