from functools import reduce


test = """30373
25512
65332
33549
35390"""

with open("day8/input.txt", "r", encoding="utf-8") as f:
    input = f.read()


def createBoolGrid(inp):
    grid = []
    for elem in inp:
        grid.append([0 for i in range(len(elem))])
    return grid


def getNoOfVisableTrees(inp):
    boolGrid = createBoolGrid(inp)
    rowLen = len(inp[0])
    colHeight = len(inp)
    # from left
    for row in range(colHeight):
        height = inp[row][0]  # get first elem height
        boolGrid[row][0] = 1  # first elem is always visible
        for col in range(1, rowLen):  # skip first elem and go to the right
            if inp[row][col] > height:  # if elem is higher than the previous one
                height = inp[row][col]  # update current height level
                boolGrid[row][col] = 1  # mark as visible
    # from right
    for row in range(colHeight):
        height = inp[row][rowLen - 1]
        boolGrid[row][rowLen - 1] = 1
        for col in range(rowLen - 1, -1, -1):
            if inp[row][col] > height:
                height = inp[row][col]
                boolGrid[row][col] = 1
    # from top
    for row in range(rowLen):
        height = inp[0][row]
        boolGrid[0][row] = 1
        for col in range(colHeight):
            if inp[col][row] > height:
                height = inp[col][row]
                boolGrid[col][row] = 1
    # from bottom
    for row in range(rowLen):
        height = inp[-1][row]
        boolGrid[-1][row] = 1
        for col in range(colHeight - 1, -1, -1):
            if inp[col][row] > height:
                height = inp[col][row]
                boolGrid[col][row] = 1
    # count visible trees
    sum = 0
    for row in range(len(boolGrid)):
        # print(boolGrid[row]) # prints bool grid
        for col in range(len(boolGrid[0])):
            sum += boolGrid[row][col]

    return sum


# part 2
def findBestViewpoint(inp):
    result = 0
    rowLen = len(inp[0])
    colHeight = len(inp)
    for row in range(colHeight):
        for col in range(rowLen):
            visableTrees = [0]
            CurrentHeight = inp[row][col]
            # look left
            for elem in range(col - 1, -1, -1):
                visableTrees[-1] += 1
                if inp[row][elem] >= CurrentHeight:
                    break
            visableTrees.append(0)
            # look right
            for elem in range(col + 1, rowLen):
                visableTrees[-1] += 1
                if inp[row][elem] >= CurrentHeight:
                    break
            visableTrees.append(0)
            # look up
            for elem in range(row - 1, -1, -1):
                visableTrees[-1] += 1
                if inp[elem][col] >= CurrentHeight:
                    break
            visableTrees.append(0)
            # look down
            for elem in range(row + 1, colHeight):
                visableTrees[-1] += 1
                if inp[elem][col] >= CurrentHeight:
                    break
            result = max(result, reduce(lambda x, y: x * y, visableTrees))

    return result


def main(data):
    lines = [line.strip() for line in data.splitlines()]
    print(getNoOfVisableTrees(lines))
    print(findBestViewpoint(lines))


if __name__ == "__main__":
    main(input)
