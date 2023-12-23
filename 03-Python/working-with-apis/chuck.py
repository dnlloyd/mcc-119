import requests

base_url = 'https://api.chucknorris.io/jokes'
response = requests.get(f'{base_url}/random')
joke = response.json()

print(joke['value'])
