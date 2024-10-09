calculus_class = {"Marsha", "Jan", "Peter"}
physics_class = {"Greg", "Peter", "Jan"}


# Union
all_students = calculus_class.union(physics_class)
print(f"All students: {all_students}")




# Intersection
students_in_both = calculus_class.intersection(physics_class)
print(f"Students in both: {students_in_both}")

bio_class = {"Jan", "Fred"}
students_in_all_three = calculus_class.intersection(physics_class, bio_class)
print(students_in_all_three)




# Difference
students_in_only_calc = calculus_class.difference(physics_class)
print(f"Students in only calculus: {students_in_only_calc}")


students_in_only_physics = physics_class.difference(calculus_class)
print(f"Students in only physics: {students_in_only_physics}")


athletes = {"Mia Hamm", "Barry Bonds", "LeBron James", "Lance Armstrong"}
disqualified = {"Lance Armstrong", "Barry Bonds"}
award_recipients = athletes.difference(disqualified)

print(award_recipients)




# Symmetric difference
students_in_only_one_class = calculus_class.symmetric_difference(physics_class)
print(f"Students in only one class: {students_in_only_one_class}")
