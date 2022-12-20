from collections import deque


def solve(part, inp):
    if part == 2:
        res = [(int(x) * 811589153) for x in inp]
    else:
        res = [int(x) for x in inp]

    res = deque(list(enumerate(res)))

    for _ in range(10 if part == 2 else 1):
        for i in range(len(res)):
            while res[0][0] != i:
                res.rotate(-1)

            topElem = res.popleft()
            newIndex = topElem[1] % len(res)

            res.insert(newIndex, topElem)

    j = -1
    for i, (_, value) in enumerate(res):
        if value == 0:
            j = i
            break

    return (
        res[(j + 1000) % len(res)][1]
        + res[(j + 2000) % len(res)][1]
        + res[(j + 3000) % len(res)][1]
    )


def main(inp):
    result1 = solve(1, inp)
    print("Result 1: ", result1)
    result2 = solve(2, inp)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day20/input.txt", "r", encoding="utf-8") as f:
        inp = f.read().splitlines()
    main(inp)
