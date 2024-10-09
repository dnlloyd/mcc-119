### Declaring
my_family = set(["Dan", "Melody", "Dalton", "Cade"])
# or
my_family = {"Dan", "Melody", "Dalton"}



### Methods
my_family = set(["Dan", "Melody", "Dalton"])

# Add a single item
my_family.add("Cade")
print(my_family)


my_family.update(["Cruz", "Mari"])
print(my_family)




### How sets differ from lists
sentence = "Hello my name is dan, i will be teaching a class in python scripting. thanks for attending this class"
vowels_found = []
# vs.
# vowels_found = set([])

for letter in sentence:
  if letter in {"a", "e", "i", "o", "u"}:
    print(f"letter {letter} is a vowel")
    vowels_found.append(letter)
    # vs
    # vowels_found.add(letter)

print(vowels_found)
