import random

pienet = 'abcdefghjkmnopqrstuvxyzåäö'
isot = pienet.upper()
numerot = '23456789'
erikoismerkit = '<>,.-!"#¤%&/()=?'

kaikki = pienet + isot + numerot + erikoismerkit

pituus = int(input('Valitse salasanan pituus: '))
pituus = max(32, pituus)  # ei sallita liian lyhyitä

salasana = ''
while len(salasana) < pituus:
    salasana += random.choice(kaikki)

print(salasana)
