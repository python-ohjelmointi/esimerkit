def huuda(teksti):
    print(teksti.upper() + '!!!!')


def kuiskaa(teksti):
    print(teksti.lower().replace('!', '.'))


def kayttajanimi(etunimi: str, sukunimi: str):
    print((sukunimi[:4] + etunimi[:2]).lower())
    print(f'{etunimi}.{sukunimi}@example.com'.lower())


def sensuroi(kortin_numero):
    print('*' * (len(kortin_numero) - 4) + kortin_numero[-4:])


def laske_lumikuorma(pinta_ala, lumen_korkeus, kiloja_per_litra):
    """
    https://www.meillakotona.fi/artikkelit/mittaa-katon-lumikuorma
    """
    litroja = pinta_ala * lumen_korkeus * 1_000
    paino = litroja * kiloja_per_litra
    paino_m2 = lumen_korkeus * 1_000 * kiloja_per_litra

    print(f'Lumi painaa yhteensä {paino} kg')
    print(f'Neliö lunta painaa {paino_m2} kg')

    if paino_m2 >= 180:
        print('Lumet täytyy pudottaa')
    elif paino_m2 >= 100:
        print('Harkitse lumien pudottamista')


huuda('Terve, mitä kuuluu?')
kuiskaa('PELKKÄÄ HYVÄÄ KIITOS!')
kayttajanimi('Teemu', 'Havulinna')

sensuroi('1234567891011')
