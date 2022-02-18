i = 0
korkeus = 10
leveys = korkeus * 2

while i < korkeus:
    tahdet = '*' * (1 + i*2)
    print(tahdet.center(leveys))

    i += 1
