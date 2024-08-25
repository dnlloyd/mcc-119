### Difference
athletes = {"Mia Hamm", "Barry Bonds", "LeBron James", "Lance Armstrong"}
disqualified = {"Lance Armstrong", "Barry Bonds"}
# award_recipients = athletes.difference(disqualified)

# print(award_recipients)

athletes.difference_update(disqualified)
print(athletes)
