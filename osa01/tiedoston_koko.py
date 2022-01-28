tavut = 500_000_000_000

kilo = 1_024
mega = 1_024**2
giga = 1_024**3
tera = 1_024**4

if tavut < kilo:
    print(f'{tavut} B')

elif tavut < mega:
    kilot = round(tavut / kilo, 2)
    print(f'{kilot} KB')

elif tavut < giga:
    megat = round(tavut / mega, 2)
    print(f'{megat} MB')

elif tavut < tera:
    gigat = round(tavut / giga, 2)
    print(f'{gigat} GB')

elif tera < tavut:
    terat = round(tavut / tera, 2)
    print(f'{terat} TB')