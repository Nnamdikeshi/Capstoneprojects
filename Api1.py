#pip install --user requests

import requests

key = 9c863653

base_url = 'http://www.omdbapi.com/'
movie = input("What movie name?")
params = { 'apikey' key. 't' : movie }
data  = requests.get(base_url, params ). json()

print(data)

print("Rating for that movie: ")
print(data['Ratings'][0]['Value'])


http://www.omdbapi.com/?apikey=[9c863653]&