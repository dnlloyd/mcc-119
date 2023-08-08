families_list_of_dicts = [
  {
    "name": "Lloyds",
    "father": "Dan",
    "children": [
      {
        "name": "Dalton",
        "age": "25"
      },
      {
        "name": "Cade",
        "age": "23"
      },
      {
        "name": "Cruz",
        "age": "15"
      },
      {
        "name": "Mari",
        "age": "14"
      },
    ],
    "home": {
      "address": "123 Lovers Ln",
      "type": "house"
    }
  },
  {
    "name": "Collums",
    "father": "Shaun",
    "children": [
      {
        "name": "Haley",
        "age": "28"
      },
      {
        "name": "Tate",
        "age": "24"
      },
      {
        "name": "Jace",
        "age": "21"
      },
      {
        "name": "Liv",
        "age": "18"
      },
    ],
    "home": {
      "address": "456 Easy rd"
    }
  }
]

print('---- Family: List of dictionaries ----')
for family in families_list_of_dicts:
  print(family["name"])

  for child in family["children"]:
    print(f'{child["name"]}: {child["age"]}')


# families_dict = {
#   "Lloyds": {
#     "father": "Dan",
#     "children": ["Dalton", "Cade", "Cruz", "Cade"],
#     "home": {
#       "address": "123 Lovers Ln",
#       "type": "house"
#     }
#   },
#   "Collums": {
#     "father": "Shaun",
#     "children": ["Haley", "Tate", "Jace", "Liv"],
#     "home": {
#       "address": "456 Easy rd"
#     }
#   }
# }


# print('\n---- Family: dictionary ----')
# for family_name, family_info in families_dict.items():
#   print(family_info["children"])
