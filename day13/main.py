from functools import cmp_to_key


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]

    return next(
        (c for c in (compare(x, y) for x, y in zip(a, b)) if c), len(a) - len(b)
    )


def countCorrectOrdered(inp):
    ans = 0
    for i, pair in enumerate(inp.split("\n\n"), 1):
        a, b = map(eval, pair.split("\n"))
        if compare(a, b) <= 0:
            ans += i
    return ans


def sortAndFindKeyProduct(inp):
    packets = []
    for line in inp.splitlines():
        if line:
            packets += [eval(line)]
    packets += [[[2]], [[6]]]

    packets.sort(key=cmp_to_key(compare))

    a = packets.index([[2]]) + 1
    b = packets.index([[6]]) + 1
    return a * b


def main(inp):
    result1 = countCorrectOrdered(inp)
    result2 = sortAndFindKeyProduct(inp)
    print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day13/input.txt", "r", encoding="utf-8") as f:
        inp = f.read().strip()
    main(inp)
