from collections import defaultdict


def getSizes(input):
    location = []
    sizes = defaultdict(int)
    for line in input.splitlines():
        if line.startswith("$ cd .."):
            location.pop()
        elif line.startswith("$ cd "):
            location.append(line[5:])
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir "):
            continue
        elif line[0].isdigit():
            value = int(line.split()[0])
            for i in range(1, len(location) + 1):
                sizes["".join(location[:i])] += value
    return sizes


def freeUpEnoughSpace(sizes, spaceNeeded, totalSpace):
    usedSpace = sizes["/"]
    availableSpace = totalSpace - usedSpace
    needToFreeUp = spaceNeeded - availableSpace

    smallest = None
    for dir, size in sizes.items():
        if smallest is None or size < smallest[1]:
            if size >= needToFreeUp:
                smallest = (dir, size)

    return smallest


def main(inp):
    # result1 = findMaxScore(inp)
    result2 = freeUpEnoughSpace(getSizes(inp), 30_000_000, 70_000_000)
    # print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day7/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    main(inp)
