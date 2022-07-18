# Write your code here.

def get_number_of_teams():
    num = int(input("Enter the number of teams in the tournament: "))

    while num < 2:
        print("The minimum number of teams is 2, try again.")
        num = int(input("Enter the number of teams in the tournament: "))

    return num


def get_team_names(num_teams):
    names = []
    round = 1
    
    while round <= num_teams:
        
        name = input(f"Enter the name for the team {round}#: ")
        num_words = len(name.split(" "))
        if len(name) < 2:
            print("Team names must have at least 2 characters, try again.")
        elif num_words > 2:
            print("Team names may have at most 2 words, try again.")
        else:
            names.append(name)
        round += 1

    return names


def get_number_of_games_played(num_teams):
    num = int(input("Enter the number of games played by each team: "))
    while num < num_teams - 1:
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        num = int(input("Enter the number of games played by each team: "))
    return num

def get_team_wins(team_names, games_played):
    team_wins = {}
    
    for i in range(len(team_names)):
        while True:
            wins = int(input(f"Enter the number of wins Team {team_names[i]} had: "))
            if wins < 0:
                print("The minimum number of wins is 0, try again.")
            elif wins > len(team_names):
                print(f"The maximum number of wins is {len(team_names)}, try again.")
            elif wins <= games_played:
                team_wins[team_names[i]] = wins
                break

    return team_wins


# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")

games_to_be_played = int(num_teams / 2)
for _ in range(games_to_be_played):
    temp_most_wins = 0
    most_wins_team = ""

    for i in team_wins:
        if team_wins[i] > temp_most_wins:
            temp_most_wins = team_wins[i] 
            most_wins_team = i

    del team_wins[most_wins_team]
    temp_least_wins = temp_most_wins
    least_wins_team = ""

    for i in team_wins:
        if team_wins[i] < temp_least_wins:
            temp_least_wins = team_wins[i]
            least_wins_team = i

    del team_wins[least_wins_team]

    print(f"Home: {least_wins_team} VS Away: {most_wins_team}")
