with open("day1/input.txt", "r", encoding="utf-8") as f:
    input = f.read()


def find_max_score(scores):
    currentScore = 0
    maxScore = 0
    for line in scores.split("\n"):
        if line == "":
            currentScore = 0
        else:
            currentScore += int(line)
            if currentScore > maxScore:
                maxScore = currentScore
    return maxScore


def find_top_three(scores):
    currentScore = 0
    topThree = [0, 0, 0]
    for line in scores.split("\n"):
        if line == "":
            currentScore = 0
        else:
            currentScore += int(line)
            if currentScore > topThree[0]:
                topThree[0] = currentScore
                topThree.sort(reverse=False)
    return topThree


result1 = find_max_score(input)
result2 = sum(find_top_three(input))
print("Result 1: ", result1)
print("Result 2: ", result2)
