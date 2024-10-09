vowels = {"a", "e", "i", "o", "u"}


### Iteration
for vowel in vowels:
  print(vowel)



### Methods

# Pop is random
# https://www.w3schools.com/python/ref_set_pop.asp
popped = vowels.pop()

print(f"vowels: {vowels}")
print(f"popped: {popped}")


# remove
vowels = {"a", "e", "i", "o", "u"}
vowels.remove("a")
print(vowels)
vowels.remove("a")   # error raised
# vs.
vowels.discard("a")  # no error raised


# clear
vowels.clear()
print(vowels)
