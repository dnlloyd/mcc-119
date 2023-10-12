import requests

agify_url = 'https://api.agify.io'
numbers_url = 'http://numbersapi.com'

def guess_my_age(name):
  response = requests.get(f'{agify_url}?name={name}')
  data = response.json()
  age = data['age']

  return age


def interesting_fact_about_a_date(date):
  response = requests.get(f"http://numbersapi.com/{date}/date")
  data = response.text

  return data


name = input('Enter your name: ')
age = guess_my_age(name)
print(f'Based on your name, your age is: {age}\n')

birthday = input('Enter your date of birth (ex: 04/1): ')
interesting_fact = interesting_fact_about_a_date(birthday)
print(f'An interesting fact about your birthday:\n{interesting_fact}')

anniv = input('Enter your anniversary (ex: 04/1): ')
interesting_fact = interesting_fact_about_a_date(anniv)
print(f'An interesting fact about your birthday:\n{interesting_fact}')