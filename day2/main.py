with open("day2/input.txt", "r", encoding="utf-8") as f:
    input = f.read()


test = """A Y
B X
C Z
"""


def calculate_winnerscore(P1, P2):
    if P1 == P2:
        return 3
    elif P1 == "A" and P2 == "B":  # Rock beats Paper
        return 6
    elif P1 == "C" and P2 == "A":  # Paper beats Rock
        return 6
    elif P1 == "B" and P2 == "C":  # Rock beat Scissors
        return 6
    else:
        return 0


def calc_select(P2):
    if P2 == "A":
        return 1
    elif P2 == "B":
        return 2
    elif P2 == "C":
        return 3
    else:
        return 0


def calc_roundscore(P1, P2):
    return calculate_winnerscore(P1, P2) + calc_select(P2)


def select_move(enemymove, gameoutcome):
    if gameoutcome == "X":  # I have to lose
        if enemymove == "A":
            return "C"
        elif enemymove == "B":
            return "A"
        elif enemymove == "C":
            return "B"
    elif gameoutcome == "Y":  # I have to tie
        return enemymove
    elif gameoutcome == "Z":  # I have to win
        if enemymove == "A":
            return "B"
        elif enemymove == "B":
            return "C"
        elif enemymove == "C":
            return "A"
    else:
        return "A"


def main(inp):
    scorelist = []
    for line in inp.split("\n"):
        data = line.split(" ")
        if len(data) != 2:
            continue
        player1move = data[0]
        wantedoutcome = data[1]
        player2move = select_move(player1move, wantedoutcome)
        if len(data) == 2:
            scorelist.append(calc_roundscore(player1move, player2move))
    return sum(scorelist)


print(main(input))
