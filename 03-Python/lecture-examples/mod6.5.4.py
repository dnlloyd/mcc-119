### Subset and Supersets

People_who_like_animals = {"Sue", "Ed", "Martha", "Bob"}
people_who_like_cats = {"Ed", "Martha"}

if people_who_like_cats.issubset(People_who_like_animals):
  print("cat lovers are a subset of animal lovers")


if People_who_like_animals.issuperset(people_who_like_cats):
  print("animal lovers include cat lovers")
