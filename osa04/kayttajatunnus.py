'''
Tässä tiedostossa esitetään return-komennon käyttöä sekä tyyppivihjeitä.
'''


def muodosta_tunnus(etunimi: str, sukunimi: str) -> str:
    tunnus = etunimi[:3].lower() + sukunimi[:3].lower()
    return tunnus


user1 = muodosta_tunnus('Matti', 'Meikäläinen')
user2 = muodosta_tunnus('John', 'Smith')

# luodaan tietokantaan rivi, jossa esiintyy luotu tunnus
# älä ota tästä mallia ;)
print(f'INSERT INTO users (username) VALUES ("{user1}"), ("{user2}")')
