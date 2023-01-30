from tabulate import tabulate as tbl

# Number into ordinal ie. 1 -> 1st, 2 -> 2nd
ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])

# Pointing for each team event based on position
# Key = position, value = points awarded
team_pointing = {
	1: 5,
	2: 4,
	3: 3,
	4: 2,
	5: 1
}

# Pointing for each individual event based on position
# Key = position, value = points awarded
indiv_pointing = {
	1: 20,
	2: 19,
	3: 18,
	4: 17,
	5: 16,
	6: 15,
	7: 14,
	8: 13,
	9: 12,
	10: 11,
	11: 10,
	12: 9,
	13: 8,
	14: 7,
	15: 6,
	16: 5,
	17: 4,
	18: 3,
	19: 2,
	20: 1,
}

events = {}

points = {}

team_members = {}

indivs = {}

final_ranking_table = []

print("Welcome to the tournament!\n")

# Number of events
while True:
	while True:
		try:
			num_events = int(input("How many events will you have?"))
			break
		except ValueError:
			print("Invalid number of events chosen. 1-5")

	if 0 < num_events < 6:
		break
	else:
		print("Invalid number of events chosen. 1-5")

# Get event names
for i in range(1, num_events + 1):
	event_name = input(f"Name of event {i}: ")
	events.__setitem__(i, event_name)

# Display chosen events
print("Here are the events you've chosen:")
for k, v in events.items():
	print(f"[{k}]: {v}")

# Print out the scoring for individual events
# print("\nIndividual events:")
# for pos, pnt in indiv_pointing.items():
# 	print(f"{ordinal(pos)} place gets {pnt} points")

# Ask whether individual or team mode
while True:
	game_type_choice = input("\nWould you like to play as a team or individual? ( T / I )").upper()

	if not game_type_choice == "T" and not game_type_choice == "I":
		print("Invalid game type choice. Please select either T or I.")
	else:
		break

# Find out if user wants a custom point system?
while True:
	custom_points_choice = input("\nWould you like to use a custom point system? ( Y / N )").upper()

	if not custom_points_choice == "Y" and not custom_points_choice == "N":
		print("Invalid choice. Please select either Y or N.")
	else:
		print("If applicable, you will be able to input the custom pointing system once you pick a game type.")
		break

if game_type_choice == "T":
	# Loop until valid number of teams
	while True:
		# Get number of teams, make sure type is correct
		while True:
			try:
				num_teams = int(input("\nHow many teams would you like to enter?"))
				break
			except ValueError:
				print("Invalid number of teams provided. Try again")

		# Checks whether number of teams is within bounds
		if 1 < num_teams < 5:
			break
		else:
			print("Invalid number of teams provided. Try again")

	# Get team name for every team, append to points and pointing table with base value 0
	for i in range(0, num_teams):
		team_name = input(f"Team {i + 1} name:")
		points.__setitem__(team_name, 0)
		if custom_points_choice == "Y":
			team_pointing.__setitem__(i + 1, 0)

	# Get custom pointing system if chosen above
	if custom_points_choice == "Y":
		# Insert new value for number of points at each position in dict
		for pos in team_pointing:
			while True:
				try:
					num_points_at_pos = int(input(f"Set number of points for position {pos}: "))
					team_pointing[pos] = num_points_at_pos
					break
				except ValueError:
					print("Invalid number of members. Try again")

	# Print out the scoring for team events
	print("\nTeam events:\n")
	for pos, pnt in team_pointing.items():
		print(f"{ordinal(pos)} place gets {pnt} points")

	# Input and add names of members in each team
	for team in points:
		# Loop until valid number of members
		while True:
			# Get number of members, make sure type is correct
			while True:
				try:
					num_mems = int(input(f"\nSet number of members in team {team}:"))
					break
				except ValueError:
					print("Invalid number of members. Try again")

			# Checks whether number of members is within bounds
			if 1 < num_mems < 6:
				break
			else:
				print("Invalid number of members. Try again")

		# Empty list of members to be appended after
		members = []

		# Append name of member to list for every member
		for _ in range(0, num_mems):
			members.append(input("Member name:"))

		# Add list of members to dictionary with key of team name
		team_members.__setitem__(team, members)

	for evt in events:
		print("Please specify ranking for event", events[evt])

		to_append_list = []

		# print(len(points))
		# For every team
		for i in range(0, len(points)):
			temp_ranking = {}

			while True:
				temp_ranking[ordinal(i)] = input(f"{ordinal(i+1)} place: ")

				if temp_ranking[ordinal(i)] in points.keys():
					break
				else:
					print("Invalid team name given")

			to_append_list.append(temp_ranking[ordinal(i)])

		final_ranking_table.append(to_append_list)

	# Abbreviated for simplicity + visibility
	frt = final_ranking_table
	for evt in frt:
		for i in range(0, len(frt[frt.index(evt)])):
			# Gets name of team from final ranking table and adds points based on position from pointing table
			points[frt[frt.index(evt)][i]] = points[frt[frt.index(evt)][i]] + team_pointing[i+1]

	# print(frt)

	scoreboard = dict(reversed(points.items()))
	# print(scoreboard)

	# Prints final scoreboard with place
	# counter = 1
	# for team, score in scoreboard.items():
	# 	print(f"{ordinal(counter)} place: {team} with {score} points")
	# 	counter += 1
	headers = ["team name", "points"]
	print(tbl(scoreboard.items(), tablefmt="github", headers=headers))

else:
	# TODO: indiviuals
	pass

# print(team_members)
