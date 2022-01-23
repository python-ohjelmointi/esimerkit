'''
Tämä esimerkkiskripti kysyy tiedoston koon ja liittymän nopeuden, ja antaa
arvion tiedoston lataamiseen kuluvasta ajasta.

Arvion saamiseksi ohjelmassa huomioidaan tiedostojen koon ja liittymien
nopeuksien ilmoittamisessa olevat eroavaisuudet, eli kilo- ja mega-
yksiköiden eri merkitykset. Lisäksi lasketaan tiedoston koko tavujen
sijaan bitteinä.
'''

# megatavua  (mega = 1024**2)
tiedosto_mb = int(input('Syötä tiedoston koko (Mt): '))
koko_bitteina = tiedosto_mb * 1_024**2 * 8  # 1 tavu = 8 bittiä

# megabittiä (mega = 1000**2)
liittyma_mbps = int(input('Syötä liittymän nopeus (Mbps): '))
liittyma_bps = liittyma_mbps * 1_000_000

sekunnit = koko_bitteina / liittyma_bps

print(str(tiedosto_mb) + ' Mt tiedoston lataus vie noin ' +
      str(round(sekunnit)) + ' sekuntia.')
