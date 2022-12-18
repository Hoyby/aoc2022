def extractRocks(inp):
    rocks = set()
    for line in inp:
        prev = None
        for rockCoord in line.split("->"):
            x, y = map(int, rockCoord.split(","))
            if prev is not None:
                dx = x - prev[0]
                dy = y - prev[1]
                for i in range(max(abs(dx), abs(dy)) + 1):
                    xx = prev[0] + i * (1 if dx > 0 else (-1 if dx < 0 else 0))
                    yy = prev[1] + i * (1 if dy > 0 else (-1 if dy < 0 else 0))
                    rocks.add((xx, yy))
            prev = (x, y)
    return rocks


def addFloor(grid):
    floor = 2 + max(r[1] for r in grid)
    loX = min(r[0] for r in grid) - 2000
    hiX = max(r[0] for r in grid) + 2000
    for x in range(loX, hiX):
        grid.add((x, floor))
    return grid, floor


def runSimulation(grid, floor):
    did_p1 = False
    for t in range(1000000):
        sand = (500, 0)
        while True:
            if sand[1] + 1 >= floor and (not did_p1):
                did_p1 = True
                p1 = t
            if (sand[0], sand[1] + 1) not in grid:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in grid:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in grid:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                break
        if sand == (500, 0):
            p2 = t + 1
            return p1, p2
        grid.add(sand)


def main(inp):
    grid, floor = addFloor(extractRocks(inp))
    result1, result2 = runSimulation(grid, floor)
    print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day14/input.txt", "r", encoding="utf-8") as f:
        inp = f.read().splitlines()
    main(inp)
