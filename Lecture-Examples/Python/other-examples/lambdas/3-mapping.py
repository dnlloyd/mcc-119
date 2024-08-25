first_names = ['melody', 'dan', 'dalton', 'cade', 'cruz', 'mari']

first_names_capitalized = list(map(lambda name: name.capitalize(), first_names))
print(f'Names capitalized: {first_names_capitalized}')

####### 1
my_name = "dan"
name_cap = (lambda name: name.capitalize())(my_name)
print(name_cap)

####### 2
my_map = map(lambda name: name.capitalize(), first_names)
print(my_map)

for name in my_map:
  print(name)

####### 3
first_names_capitalized = list(map(lambda name: name.capitalize(), first_names))
print(f'Names capitalized: {first_names_capitalized}')