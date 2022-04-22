'''
Muodostetaan polku, joka on:
* suhteessa nykyisen Python-tiedoston sijaintiin
    * eli toimii työhakemistosta riippumatta
* toimii sekä Linuxissa, MacOS:ssä että Windowsissa
'''

from pathlib import Path

tiedosto = Path(__file__).parent / 'tiedostot' / 'nimet.csv'

# tiedostosta luettu sisältö on "aivan tavallinen" merkkijono
sisalto = tiedosto.read_text(encoding='utf-8')

kokonaismaara = 0
for rivi in sisalto.splitlines():
    nimi, maara, sukupuoli = rivi.split(';')
    print(nimi)
    kokonaismaara += int(maara.replace(' ', ''))

print(f'Aineistossa on {kokonaismaara} nimeä')
