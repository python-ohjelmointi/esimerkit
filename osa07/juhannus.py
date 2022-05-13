'''
"Nykyisin juhannusta juhlitaan Suomessa ja Ruotsissa
kesäkuun 20. ja 26. päivien välisenä lauantaina"
https://fi.wikipedia.org/wiki/Juhannus
'''
from datetime import date, timedelta


def on_juhannus(pvm: date) -> bool:
    return pvm.month == 6 and 20 <= pvm.day <= 26 and pvm.isoweekday() == 6


paivamaara = date.today()
laskuri = 0

while not on_juhannus(paivamaara):
    laskuri += 1
    # siirrytään seuraavaan päivään:
    paivamaara = paivamaara + timedelta(days=1)


print(f'{paivamaara} on juhannus: {on_juhannus(paivamaara)}')
print(f'{laskuri} päivää juhannukseen')


paivamaara = date(2010, 1, 1)

# käydään päivät väliltä 2010 - 2030
while paivamaara.year < 2030:
    if on_juhannus(paivamaara):
        # muotoillaan lähes wikipedian taulukkoformaattiin:
        print(f"'''{paivamaara.year}''' | {paivamaara.day}. kesäkuuta")

    # Siirrytään seuraavaan päivään:
    paivamaara = paivamaara + timedelta(days=1)
