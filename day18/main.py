from collections import deque


def extExposed(pos, cubes, min_coord, max_coord):
    stack = deque([pos])
    visited = set()

    while len(stack) > 0:
        pop = stack.popleft()

        if pop in cubes:
            continue

        for coord in range(3):
            if not (min_coord <= pop[coord] <= max_coord):
                return True

        if pop in visited:
            continue
        visited.add(pop)

        for neighbor in getNeigbors(pop):
            if neighbor not in visited:
                stack.append(neighbor)

    return False


def getNeigbors(pos):
    neighbors = [
        (pos[0] + 1, pos[1], pos[2]),
        (pos[0] - 1, pos[1], pos[2]),
        (pos[0], pos[1] + 1, pos[2]),
        (pos[0], pos[1] - 1, pos[2]),
        (pos[0], pos[1], pos[2] + 1),
        (pos[0], pos[1], pos[2] - 1),
    ]
    return neighbors


def solve(part, inp):
    cubes = set()
    minCoord = float("inf")
    maxCoord = float("-inf")
    for line in inp:
        x, y, z = map(int, line.split(","))
        cubes.add((x, y, z))
        for coord in [x, y, z]:
            minCoord = min(minCoord, coord)
            maxCoord = max(maxCoord, coord)

    ans = 0
    for pos in cubes:
        neighbors = getNeigbors(pos)
        for neighbor in neighbors:
            if neighbor not in cubes:
                if part == 1:
                    ans += 1
                if part == 2:
                    if extExposed(neighbor, cubes, minCoord, maxCoord):
                        ans += 1
    return ans


def main(inp):
    result1 = solve(1, inp)
    print("Result 1: ", result1)
    result2 = solve(2, inp)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day18/input.txt", "r", encoding="utf-8") as f:
        inp = f.read().splitlines()
    main(inp)
