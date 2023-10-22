# 

# mixed = [45, "string"]
# student = ["bob", "martha", "ed", "mary"]
# ages = [5, 9, 11]

# my_list = []
# my_list.append("bob")
# print(my_list)

# if 2 >= 2:
#   print("true")

# name = "dan"
# age = 49

# if not name == "dan":
#   print("you the student")


# students = ["bob", "martha", "ed", "mary"]

# if "bob" in students:
#   print("is a student")
# else:
#   print("sdsds")
# elif:
#   print("not a student")

################################################################################
################################### Module 3 ###################################

# guess = input("guess my name: ")

# if guess == "Dan" or guess == "dan":
#   print("Correct")
# elif guess == "Dave":
#   print("Nope, thats my dad")
# else:
#   print("Wrong")


# count = 0

# while count < 10 or count > -10:

#   print(count)
#   count += 1
# else:
#   print("we're done here")

# students = ["bob", "martha", "ed", "mary"]

# for student in  students:
#   print(student)

# class_size = len(students)

# count = 0

# while count < 4:
#   print(students[count])
#   count += 1


# for number in range(-5, 10):
#   print(number)

# families = [
#   {
#     "name": "Lloyds",
#     "father": "Dan",
#     "children": [
#       {
#         "name": "Bob",
#         "age": "25"
#       },
#       {
#         "name": "Jed",
#         "age": "23"
#       },
#       {
#         "name": "Albert",
#         "age": "15"
#       },
#       {
#         "name": "Martha",
#         "age": "14"
#       },
#     ],
#     "home": {
#       "address": "123 Right Way",
#       "type": "house"
#     }
#   },
#   {
#     "name": "Smiths",
#     "father": "Shaun",
#     "children": [
#       {
#         "name": "Haley",
#         "age": "28"
#       },
#       {
#         "name": "Tate",
#         "age": "24"
#       },
#       {
#         "name": "Jace",
#         "age": "21"
#       },
#       {
#         "name": "Liv",
#         "age": "18"
#       },
#     ],
#     "home": {
#       "address": "456 Easy Road"
#     }
#   }
# ]

# for family in families:
#   print(family["name"])
#   for child in family["children"]:
#     print(child["name"])
  
#   print("")

################################################################################
################################### Module 4 ###################################

# my_simple_list = ["Ford", "Toyota", "Chevrolet", "Chevrolet"]

# my_mixed_list = ["string", 9, "other string"]

# my_complex_list = [
#   {
#     "make": "Ford",
#     "model": "Focus",
#     "year": 2011
#   },
#   {
#     "make": "Toyota",
#     "model": "Prius",
#     "year": 2021
#   }
# ]





# my_list = ["Ford", "Toyota", "Chevrolet"]
# my_list.append("Honda")
# print(my_list)





# my_list = ["Ford", "Toyota", "Chevrolet"]
# my_list.extend(["Honda", "GM"])
# print(my_list)



# my_list = ["Ford", "Toyota", "Chevrolet"]
# my_list.insert(2, "GM")
# print(my_list)


# my_list = ["Ford", "Toyota", "Chevrolet"]
# my_list.pop(0)
# print(my_list)

# my_list = ["Ford", "Toyota", "Chevrolet"]
# my_list.index("Ford")
# print(my_list.index("Toyota"))


# my_list = ["Ford", "Toyota", "Chevrolet", "GM", "Audi"]
# my_list.sort(reverse=True)
# print(my_list)

# my_list = ["Ford", "Toyota", "Chevrolet", "GM", "Audi"]
# my_list.sort(reverse=True)
# print(my_list)



# def myFunc(e):
#   return e['year']

# cars = [
#   {
#     'car': 'Ford',
#     'year': 2005
#   },
#   {
#     'car': 'Mitsubishi',
#     'year': 2000
#   },
#   {
#     'car': 'BMW', 
#     'year': 2019
#   },
#   {
#     'car': 'VW',
#     'year': 2011
#   }
# ]

# cars.sort(key=myFunc)
# print(cars)



# my_kids = ["dalton", "cade", "cruz", "mari"]

# # for name in my_kids:
# #   print(name)

# names = [name[2:].capitalize() for name in my_kids]
# print(names)



# my_tuple = "hello",
# print(type(my_tuple))

# my_other_tuple = ("hello",)
# print(type(my_other_tuple))

# my_tuple = ("Ford", "Toyota", "Chevrolet", "GM", "Audi")
# my_new_tuple = my_tuple[2:4]
# print(my_new_tuple)


# my_tuple_1 = ["Ford", "Toyota", "Chevrolet"]
# my_tuple_2 = ["GM", "Audi"]
# my_tuple_3 = my_tuple_1 + my_tuple_2
# print(my_tuple_3)




