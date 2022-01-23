# megatavua  (mega = 1024**2)
tiedosto_megabyte = int(input('Syötä tiedoston koko (Mt): '))

# megabittiä (mega = 1000**2)
liittyma_mbps = int(input('Syötä liittymän nopeus (Mbps): '))

koko_bit = tiedosto_megabyte * 1_024**2 * 8
liittyma_bits = liittyma_mbps * 1_000_000

sekunnit = koko_bit / liittyma_bits

print(str(tiedosto_megabyte) + ' Mt tiedoston lataus vie noin ' +
      str(round(sekunnit)) + ' sekuntia.')
