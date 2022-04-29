'''
>>> dict_pieneksi({'ETUNIMI': 'VAPPU', 'SUKUNIMI': 'MUNKKI'})
{'etunimi': 'Vappu', 'sukunimi': 'Munkki'}
'''


def dict_pieneksi(sanakirja):

    new_dict = {}
    for k, v in sanakirja.items():
        new_dict[k.lower()] = v.title()
    return new_dict


d = {'ETUNIMI': 'VAPPU', 'SUKUNIMI': 'MUNKKI'}
pieni = dict_pieneksi(d)
print(pieni)
