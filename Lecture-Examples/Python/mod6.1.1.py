"""Dictionary examples"""

### Example comparing list of list to dictionary
my_company_staff = [
    ["Martha Martin", "Bob, Roberts", "Maggie Moo"],
    ["Jon Johnson", "Angie Angel", "Edward Scissors"],
    ["Heather Jobs", "Bradley Thomas"]
]

my_company_staff = {
    "Executives": ["Martha Martin", "Bob, Roberts", "Maggie Moo"],
    "Sales": ["Jon Johnson", "Angie Angel", "Edward Scissors"],
    "Engineers": ["Heather Jobs", "Bradley Thomas"]
}

my_company = {
    "staff": {
        "Executives": ["Martha Martin", "Bob, Roberts", "Maggie Moo"],
        "Sales": ["Jon Johnson", "Angie Angel", "Edward Scissors"],
        "Engineers": ["Heather Jobs", "Bradley Thomas"],
    },
    "name": "Danco Inc",
    "address": "123 Computer Drive",
    "sales": {
        "2021": 650099,
        "2022": 786770,
        "2023": 1023350,
        "2024": 1500356,
    }
}



### Accessing
my_family = {
    # key   : value
    "father": "Dan",
    "mother": "Mel",
    "child1": "Cruz"
}

print(my_family["father"])
# vs.
dad = my_family.get('father')
print(dad)



### Iterating
for member in my_family:
    print(member)


for member, name in my_family.items():
    print(f'{member}: {name}')


for name in my_family.values():
    print(name)



### checking if key exists
if "father" in my_family:
    print("key 'father' exists in dictionary")



### More complex examples
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

my_children = [
        {
            "name" : "Dan",
            "age" : 25
        },
        {
            "name" : "Jim",
            "age" : 20
        },
        {
            "name" : "Sam",
            "age" : 30
        }
    ]

print(my_children)

my_children.sort(key=lambda child: child["age"])

print(my_children)
