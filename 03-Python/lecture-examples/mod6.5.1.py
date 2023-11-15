### Union
calculus_class = {"Marsha", "Jan", "Peter"}
physics_class = {"Greg", "Peter", "Jan"}

all_students = calculus_class.union(physics_class)
# print(all_students)


numbers_1 = {1, 2, 3}
numbers_2 = {3, 4, 5}

numbers_3 = numbers_1 | numbers_2
# print(numbers_3)


calculus_class = {"Marsha", "Jan", "Peter"}
physics_class = {"Greg", "Peter", "Jan"}
bio_class = {"Jan"}

### Intersection
students_in_calc_and_physics = calculus_class.intersection(physics_class, bio_class)
# print(students_in_calc_and_physics)

# numbers_1 = {1, 2, 3}
# numbers_2 = {3, 4, 5}

# numbers_3 = numbers_1 & numbers_2
# print(numbers_3)



### Difference
# athletes = {"Mia Hamm", "Barry Bonds", "LeBron James", "Lance Armstrong"}
# disqualified = {"Lance Armstrong", "Barry Bonds"}
# award_recipients = athletes.difference(disqualified)

# print(award_recipients)



### Symmetric difference
# returns all the items present in given sets, except the items in their intersections.
calculus_class = {"Marsha", "Jan", "Peter"}
physics_class = {"Greg", "Peter", "Jan"}

students_in_single_class = calculus_class.symmetric_difference(physics_class)
print(students_in_single_class)
