### Difference
athletes = {"Mia Hamm", "Barry Bonds", "LeBron James", "Lance Armstrong"}
print(f"Athletes: {athletes}")

disqualified = {"Lance Armstrong", "Barry Bonds"}
award_recipients = athletes.difference(disqualified)

print(f"Award Recipients: {award_recipients}")

print("\nRemoving disqualified atheletes")
athletes.difference_update(disqualified)
print(f"Athletes: {athletes}")
