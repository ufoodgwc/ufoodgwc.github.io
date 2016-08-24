from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import csv

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

c = "yelp.csv"
writer = csv.writer(open(c,'w'),dialect='excel')
writer.writerow(('Name','Rate','Link'))


response = client.search('New York City', **params)
for i in range(len(response.businesses)):
	print(response.businesses[i].name + " - Rating: "  + str(response.businesses[i].rating) + str(response.businesses[i].url))
	Name = response.businesses[i].name
	Rate = response.businesses[i].rating
	Link = response.businesses[i].url
	data=[Name, Rate, Link]
	writer.writerow(data) 


