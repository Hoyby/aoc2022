def is_subset(a, b):
    return a[0] >= b[0] and a[1] <= b[1]


def count_subsets(inp):
    count = 0
    for line in inp.splitlines():
        a, b = line.split(",")
        a = tuple(map(int, a.split("-")))
        b = tuple(map(int, b.split("-")))
        if is_subset(a, b) or is_subset(b, a):
            count += 1
    return count


def is_overlap(a, b):
    return a[0] <= b[0] and a[1] >= b[0] or b[0] <= a[0] and b[1] >= a[0]


def count_overlaps(inp):
    count = 0
    for line in inp.splitlines():
        a, b = line.split(",")
        a = tuple(map(int, a.split("-")))
        b = tuple(map(int, b.split("-")))
        if is_overlap(a, b):
            count += 1
    return count


def main(inp):
    # result1 = findMaxScore(inp)
    result2 = count_overlaps(inp)
    # print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day4/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    main(inp)
