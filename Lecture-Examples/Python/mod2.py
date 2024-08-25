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
mystring = "My Fun Stri"
print(mystring[0])
print(mystring[3])

print(mystring[3:6])


########################## 2.2.1
print(f"Floor num: {floor_sum}")


########################## 2.2.6
if mystring.startswith("B"):
  print("YES")
else:
  print("No")

print(mystring.replace("Fun", "Bad"))

print("hello\n" * 2)