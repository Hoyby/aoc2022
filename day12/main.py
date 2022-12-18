from collections import deque


def convertToNumbers(inp):
    height = len(inp)
    width = len(inp[0])
    numberGrid = [[0 for _ in range(width)] for _ in range(height)]

    for r in range(height):
        for c in range(width):
            if inp[r][c] == "S":
                numberGrid[r][c] = 1
            elif inp[r][c] == "E":
                numberGrid[r][c] = 26
            else:
                numberGrid[r][c] = ord(inp[r][c]) - ord("a") + 1

    return numberGrid, height, width


def getStartingLocations(inp, part, numberGrid, height, width):
    startingLocations = deque()
    for r in range(height):
        for c in range(width):
            if (part == 1 and inp[r][c] == "S") or (
                part == 2 and numberGrid[r][c] == 1
            ):
                startingLocations.append(((r, c), 0))
    return startingLocations


def bfs(inp, part):
    numberGrid, height, width = convertToNumbers(inp)
    queue = getStartingLocations(inp, part, numberGrid, height, width)

    visited = set()
    while queue:
        (r, c), d = queue.popleft()

        if (r, c) in visited:
            continue

        if inp[r][c] == "E":
            return d

        visited.add((r, c))

        # Check all 4 directions
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r + dr
            cc = c + dc
            if (
                0 <= rr < height
                and 0 <= cc < width
                and numberGrid[rr][cc] <= 1 + numberGrid[r][c]
            ):
                queue.append(((rr, cc), d + 1))


def main(inp):
    result1 = bfs(inp, part=1)
    result2 = bfs(inp, part=2)
    print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day12/input.txt", "r", encoding="utf-8") as f:
        inp = f.read().splitlines()
    main(inp)
