import random

# List of participant names
with open("nimilista.txt", "r") as file:
    people = [line.strip() for line in file]

# Print the lenght of people
print("Listan pituus/nimien määrä:")
people_count = len(people)
print(people_count)

# Shuffle the list randomly before forming the teams
random.shuffle(people)

# List to form teams
teams = []

while len(people) >= 3:
    # Select three people from the list
    selected_people = people[:3]

    # Append the team to the list of teams
    teams.append(selected_people)

    # Remove the selected people from the list
    people = people[3:]

# Handle the remaining person(s)
if people:
    # Add the remaining person(s) to the last team
    teams[-1].extend(people)
else:
    print("Kaikki ihmiset läpikäyty listasta.")

# Print the teams
for i, team in enumerate(teams, start=1):
    print(f"Tiimi {i}:", team)
