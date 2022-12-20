def findMaxScore(scores):
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


def findSumTopThree(scores):
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
    return sum(topThree)


def main(inp):
    result1 = findMaxScore(inp)
    result2 = findSumTopThree(inp)
    print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day1/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    main(inp)
