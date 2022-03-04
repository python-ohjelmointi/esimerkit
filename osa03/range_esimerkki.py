# range(10) toistaa nollasta yläraja - 1:een
for i in range(10):
    print(i)

print('-' * 80)

# range(100, 200) toistaa 100:sta 200-1:een:
for x in range(100, 200):
    print(x)

# kolmas parametri määrittää valinnaisen "askeleen":
for y in range(999, 900, -1):
    print(y)

# Huuda kolme kertaa eläköön!
for _ in range(3):
    print('Eläköön!')
