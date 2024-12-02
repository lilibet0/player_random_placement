import random


# Subroutines
def check_validity(num_players, field):
    if num_players <= 0:
        return False
    elif field is None:
        return False
    elif len(field) % 2 != 0:
        return False
    else:
        return True


def find_freespace(field):
    free_space_team1 = []
    free_space_team2 = []

    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col]:
                if col < (len(field[0]) // 2):
                    free_space_team1 = [(row, col)] + free_space_team1
                else:
                    free_space_team2 = [(row, col)] + free_space_team2

    return free_space_team1, free_space_team2
    
    
# Find max number of players that can be on the field
def get_max_players(num_players, free_space_team1, free_space_team2):
    team_players = num_players
    # Must have an equal number of players on each team
    if len(free_space_team1) < team_players:
        team_players = len(free_space_team1)
    if len(free_space_team2) < team_players:
        team_players = len(free_space_team2)

    return team_players


# Fischer-Yates algorithm
def fischer_yates_shuffle(free_space):
    for i in range(len(free_space) - 1, 0, -1):
        j = random.randint(0, i)
        exhange = free_space[j]
        free_space[j] = free_space[i]
        free_space[i] = exhange


# Return one set of coordinates
def find_positions(num_players, free_space):
    positions = []

    for i in range(num_players):
        new_position_index = random.randint(0, len(free_space) - 1)
        positions.append(free_space[new_position_index])
        del free_space[new_position_index]
        fischer_yates_shuffle(free_space)

    return positions


def placement(num_players, field):
    if check_validity(num_players, field) is False:
        return None

    # Find free spaces on each side
    free_space_team1, free_space_team2 = find_freespace(field)

    # Find number of players that will be on the field for each team
    team_players = get_max_players(num_players, free_space_team1, free_space_team2)

    if len(free_space_team1) == 0 or len(free_space_team2) == 0:
        return (), ()

    team1_positions = find_positions(team_players, free_space_team1)
    team2_positions = find_positions(team_players, free_space_team2)

    return tuple(team1_positions), tuple(team2_positions)
