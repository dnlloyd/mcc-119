my_int = -1
print(type(my_int))

my_float = 1.1
print(type(my_float))

my_hex_of_my_int = hex(my_int)
print(my_hex_of_my_int)

my_bin_of_my_int = bin(my_int)
print(my_bin_of_my_int)


########################## 2.1.2
sum = 3 + 7 - 1 * 4 / 3
print(sum)

floor_sum = 3 + 7 - 1 * 4 // 3
print(floor_sum)

floor_sum += 1
print(floor_sum)

floor_sum = ((3 + 7) - 1 * 4) // 3
print(floor_sum)


########################## 2.2.1
print("hello" * 2)

print("hello" + "my" + "name" + "is")

#           01234567890
mystring = "MyFunString"
print(mystring[0])
print(mystring[3])

print(mystring[3:6])


########################## 2.2.1
print(f"Floor num: {floor_sum}")


########################## 2.2.5
print(f"This is the contents of mystring: {mystring}")


########################## 2.2.6
if mystring.startswith("B"):
  print("YES")
else:
  print("No")

print(mystring.replace("Fun", "Bad"))

print("hello\n" * 2)


########################## 2.3

students = ["Dan", "Joe", "Martha"]

new_students = ["Bob", "Ed"]

all_students = students + new_students

all_students.append("Jim")

print(all_students)


########################## 2.4

teacher = True

if teacher:
  print("I'm a teacher")


########################## 2.4.2

student = False

if teacher and student:
  print("you're prob tired")

if not teacher:
  print("I'm not a teacher")
else:
  print("I'm a teacher")

if 5 < 7:
  print("yes")
else:
  print("no")

# Truthy and falsy numbers
# https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/

my_int = 5

if teacher and my_int:
  print("you're prob tired")

if "Dan" in students:
  print("yes")
  