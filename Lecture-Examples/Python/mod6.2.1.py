### Update
my_family = {
  "father": "Dan",
  "mother": "Mel",
  "child1": "Dalton"
}

my_family.update({"child2": "Cade"})

print(my_family)



### Update value
my_family = {
  "father": "Dan",
  "mother": "Melody",
  "child1": "Dalton"
}

# Add key and value (key value pair)
my_family.update({"child2": "Cade"})
print(my_family)

my_family["cousin"] = "April"
print(my_family)


# Update existing value
my_family["father"] = "Jimmy"
print(my_family)



### Methods
my_family = {
  "father": "Dan",
  "mother": "Melody",
  "child1": "Dalton"
}

# Remove all key/values
my_family.clear()
print(my_family)

# Remove a single key/value
del my_family["father"]
print(my_family)

popped_value = my_family.pop("mother")
print(my_family)
print(popped_value)
