################### Lists
my_simple_list = ["Ford", "Toyota", "Chevrolet", "Chevrolet"]

my_mixed_list = ["string", 9, "other string", 7.2]

my_complex_list = [
  {
    "make": "Ford",
    "model": "Focus",
    "year": 2011
  },
  {
    "make": "Toyota",
    "model": "Prius",
    "year": 2021
  }
]


### methods


my_cars = ["Ford", "Toyota", "Chevrolet", "Honda"]
my_cars.append("Tesla")
print(my_cars[0])

my_cars = my_cars.append("Tesla")

my_cars = ["Ford", "Toyota", "Chevrolet"]
my_cars.extend(["Honda", "GM"])
print(my_cars)



my_cars = ["Ford", "Toyota", "Chevrolet"]
my_cars.insert(2, "GM")
print(my_cars)


my_cars = ["Ford", "Toyota", "Chevrolet"]
my_cars.remove("Ford")
print(my_cars)


my_cars = ["Ford", "Toyota", "Chevrolet"]
a_car = my_cars.pop(0)
print(my_cars)
print(a_car)


my_cars = ["Ford", "Toyota", "Chevrolet"]
a_car = my_cars.index("Ford")
print(a_car)


my_cars = ["Ford", "Toyota", "Chevrolet", "Tesla", "Toyota"]
print(my_cars.count("Toyota"))



### Sorting


my_cars = ["Ford", "Toyota", "Chevrolet", "GM", "Audi"]
my_cars.sort()
print(my_cars)

my_cars = ["Ford", "Toyota", "Chevrolet", "GM", "Audi"]
my_cars.sort(reverse=True)
print(my_cars)

my_cars = ["Ford", "Toyota", "Chevrolet", "GM", "Audi"]
my_cars.reverse
print(my_cars)



###

my_kids = ["dalton", "cade", "cruz", "mari"]

names = [name[0:].capitalize() for name in my_kids]
print(names)

# equivalent to...

for name in my_kids:
  print(name.capitalize())




################### Lists
my_tuple = "hello",
print(type(my_tuple))

my_other_tuple = ("hello",)
print(type(my_other_tuple))

my_tuple = ("Ford", "Toyota", "Chevrolet", "GM", "Audi")
my_new_tuple = my_tuple[2:4]
print(my_new_tuple)


my_tuple_1 = ["Ford", "Toyota", "Chevrolet"]
my_tuple_2 = ["GM", "Audi"]
my_tuple_3 = my_tuple_1 + my_tuple_2
print(my_tuple_3)



# No "extend" method but you can add two tuples togerher
my_cars_1 = ["Ford", "Toyota", "Chevrolet"]
my_cars_2 = ["GM", "Audi"]
my_cars_3 = my_cars_1 + my_cars_2
print(my_cars_3)



false_tuple = (None,"",False,0)
print(any(false_tuple))
# --> False

false_tuple += (True,)
print(any(false_tuple))
# --> True


my_cars = ("Ford", "Toyota", "Chevrolet", "Tesla", "Toyota")
print(my_cars.count("Toyota"))


my_test_scores = (87, 91, 79, 88, 80)
print(min(my_test_scores))



######################## Extra
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
