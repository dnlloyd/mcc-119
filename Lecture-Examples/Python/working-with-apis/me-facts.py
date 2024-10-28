import requests

agify_url = 'https://api.agify.io'
numbers_url = 'http://numbersapi.com'
dogs_url = 'https://dog.ceo/api'

name = input('Enter your name: ')
name_response = requests.get(f'{agify_url}?name={name}')
name_data = name_response.json()
name_age = name_data['age']

birthday = input('Enter your birthday (04/1)): ')
birthday_response = requests.get(f"{numbers_url}/{birthday}/date")
birthday_data = birthday_response.text

dog_owner = input('Do you own a dog? (Y/N) ')
if dog_owner == 'Y':
  breed_known = input('Do you know its breed? (Y/N) ')
  if breed_known == 'Y':
    breed = input('Breed? ')
  else:
    print('Select from one of these breeds:')
    all_breeds_response = requests.get(f'{dogs_url}/breeds/list/all')
    breeds = all_breeds_response.json()['message']
    for dog in breeds:
      print(dog)
    
    breed = input('Enter breed: ')

  image_response = requests.get(f'{dogs_url}/breed/{breed}/images/random')
  image_url = image_response.json()['message']

  print(f'Your dog is {breed}: {image_url}')
    

print(f'Your estimated age is {name_age} years old')
print(f'An interesting fact about your birthday:\n{birthday_data}')
