from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key='qWd-LjYcZ6iL1eyyl5RkmQ',
    consumer_secret= 'vmiS63tELxmPYEvhJbEnG9VBCAo',
    token= 'bpK88ZEllW3yT3Qeygqitg1MolQm1TaT',
    token_secret= 'YgG729sDDlKiWTLk5APGkUcLAjw'
)

client = Client(auth)

params = {
    'term': 'food',
    'lang': 'fr'
}

response = client.search('New York City', **params)

for i in range(len(response.businesses)):
    print(response.businesses[i].name + " - Rating: "  + str(response.businesses[i].rating) + str(response.businesses[i].url))
