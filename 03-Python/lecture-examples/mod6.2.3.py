# import pprint
# pp = pprint.PrettyPrinter(indent=2, compact=False, width=1)

### Copy (Shallow)
my_family = {
  "father": "Dan",
  "mother": "Mel",
  "son": "Dalton"
}

yo_family = my_family.copy()

my_family["father"] = "bob"
print(yo_family)
print(my_family)



### Copy (Deep)
my_family = yo_family

my_family["father"] = "bob"
print(yo_family)
print(my_family)
