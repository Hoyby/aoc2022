with open("day7/input.txt", "r", encoding="utf-8") as f:
    input = f.read()

test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

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


def main():
    sizes = getSizes(input)
    smallest = freeUpEnoughSpace(sizes, 30_000_000, 70_000_000)
    print(smallest)


if __name__ == "__main__":
    main()
