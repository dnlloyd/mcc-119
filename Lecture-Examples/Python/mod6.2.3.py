the_lloyds = {
  "father": "Dan",
  "mother": "Mel",
  "son": "Dalton"
}

new_family = the_lloyds.copy()
# vs. 
# new_family = the_lloyds

the_lloyds["father"] = "Bob"

print("The Lloyds")
print(the_lloyds)

print("")

print("New Family")
print(new_family)
