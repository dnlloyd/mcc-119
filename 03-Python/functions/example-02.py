import requests

agify_url = 'https://api.agify.io'
numbers_url = 'http://numbersapi.com'

def stuff_about_me(name, date = "04/01"):
  agify_response = requests.get(f'{agify_url}?name={name}')
  agify_data = agify_response.json()
  age = agify_data['age']

  numbers_api_response = requests.get(f"http://numbersapi.com/{date}/date")
  numbers_api_data = numbers_api_response.text

  return age, numbers_api_data


name = input('Enter your name: ')
birthday = input('Enter your date of birth (ex: 04/1): ')

age, interesting_fact = stuff_about_me(name, birthday)

print(f'Based on your name, your age is: {age}\n')
print(f'An interesting fact about your birthday:\n{interesting_fact}')
