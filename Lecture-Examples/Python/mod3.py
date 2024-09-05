########################## 3.2

guess = input("guess my name: ")

if guess == "Dan" or guess == "dan":
  print("Correct")
elif guess == "Dave":
  print("Nope, thats my dad")
else:
  print("Wrong")


########################## 3.3
# 1

incorrect_guess = True

while incorrect_guess:
  guess = input("Guess my name: ")

  if guess == "Dan" or guess == "dan":
    incorrect_guess = False
  else:
    print("  Incorrect, try again")
else:
  print("Correct")

#2
students = ["bob", "martha", "ed", "mary"]
class_size = len(students)
count = 0

while count < class_size:
  print(students[count])
  count += 1


########################## 3.6
students = ["bob", "martha", "ed", "mary"]

for student in  students:
  print(student)


########################## 3.7

for number in range(-5, 10):
  print(number)

for number in range(2, 20, 5):
  print(number)


########################## 3.8

families = [
  {
    "name": "Lloyd",
    "children": [ "Dalton", "Cade", "Cruz", "Mari"]
  },
  {
    "name": "Smith",
    "children": ["Haley", "Tate", "Jace", "Liv"]
  }
]

for family in families:
  print(family["name"])
  # for child in family["children"]:
  #   print(f" - {child}")

  print("")


########################## 3.9.1

playlist = ["Smells Like Teen Spirit", "Imagine", "Bohemian Rhapsody", "Hey Jude"]

for song in playlist:
  print(song)
  if song == "Imagine":
    print(song)
    break
