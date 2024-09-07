###############################################################################
################################## Module 5 ###################################

my_simple_list = ["Ford", "Toyota", "Chevrolet", "Chevrolet"]

my_mixed_list = ["string", 9, "other string"]

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





my_list = ["Ford", "Toyota", "Chevrolet"]
my_list.append("Honda")
print(my_list)





my_list = ["Ford", "Toyota", "Chevrolet"]
my_list.extend(["Honda", "GM"])
print(my_list)



my_list = ["Ford", "Toyota", "Chevrolet"]
my_list.insert(2, "GM")
print(my_list)


my_list = ["Ford", "Toyota", "Chevrolet"]
my_list.pop(0)
print(my_list)

my_list = ["Ford", "Toyota", "Chevrolet"]
my_list.index("Ford")
print(my_list.index("Toyota"))


my_list = ["Ford", "Toyota", "Chevrolet", "GM", "Audi"]
my_list.sort(reverse=True)
print(my_list)

my_list = ["Ford", "Toyota", "Chevrolet", "GM", "Audi"]
my_list.sort(reverse=True)
print(my_list)



def myFunc(e):
  return e['year']

cars = [
  {
    'car': 'Ford',
    'year': 2005
  },
  {
    'car': 'Mitsubishi',
    'year': 2000
  },
  {
    'car': 'BMW', 
    'year': 2019
  },
  {
    'car': 'VW',
    'year': 2011
  }
]

cars.sort(key=myFunc)
print(cars)



my_kids = ["dalton", "cade", "cruz", "mari"]

# for name in my_kids:
#   print(name)

names = [name[2:].capitalize() for name in my_kids]
print(names)



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
