### Accessing

my_family = {
  # key   : value
  "father": "Dan",
  "mother": "Mel",
  "child1": "Cruz"
}

print(my_family["dad"])

father = my_family.get('dad')
print(father)



### Iterating

# for member in my_family:
#   print(member)

# for member, name in my_family.items():
#   print(f'{member}: {name}')

# for name in my_family.values():
#   print(name)



### checking if key exists

if "father" in my_family:
  print("key 'father' exists in dictionary")



### Complex

my_family_complex = {
  # key: value
  "name": "Lloyds",
  "father": "Dan",
  "children": [
    {
      "name": "Bob",
      "age": 25
    },
    {
      "name": "Jed",
      "age": 23
    },
    {
      "name": "Albert",
      "age": 15
    },
    {
      "name": "Martha",
      "age": 14
    },
  ],
  "home": {
    "address": "123 Right Way",
    "type": "house"
  }
}
