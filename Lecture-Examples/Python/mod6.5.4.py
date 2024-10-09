### Subset and Supersets

people_who_like_animals = {"Sue", "Ed", "Martha", "Bob"}
people_who_like_cats = {"Ed", "Martha"}

if people_who_like_cats.issubset(people_who_like_animals):
  print("cat lovers are a subset of animal lovers")


if people_who_like_animals.issuperset(people_who_like_cats):
  print("animal lovers include cat lovers")
