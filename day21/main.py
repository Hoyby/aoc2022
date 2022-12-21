operations = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
    "-": lambda x, y: x - y,
    "=": lambda x, y: x == y,
}


def recurse(monkeys, monkey, part, memo={}):
    if monkey not in monkeys:
        print("Error: Monkey not found: ", monkey)
        return None

    if monkey in memo and monkey != "root":
        return memo[monkey]

    if monkeys[monkey].isnumeric():  # Base case
        return int(monkeys[monkey])

    monkey1, op, monkey2 = monkeys[monkey].split(" ")
    recLeft = recurse(monkeys, monkey1, part, memo)
    recRight = recurse(monkeys, monkey2, part, memo)

    if part == 2 and monkey == "root":
        op = "-"

    result = operations[op](recLeft, recRight)

    memo[monkey] = result

    return result


def solve(part, inp):
    monkeys = dict()

    for line in inp:
        split = line.split(": ")
        monkeys[split[0]] = split[1]
    if part == 1:
        ans = recurse(monkeys, "root", part, {})
        return ans

    # binary search to find the answer
    left, right = 1, 10**18
    while left <= right:
        mid = (left + right) // 2
        monkeys["humn"] = str(mid)

        result = recurse(monkeys, "root", part, {})
        print("Trying humn:", mid, "| diff = ", result)

        if result > 0:
            left = mid + 1
        else:
            right = mid - 1

    return left


def main(inp):
    result1 = solve(1, inp)
    result2 = solve(2, inp)

    print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day21/input.txt", "r", encoding="utf-8") as f:
        inp = f.read().splitlines()
    main(inp)
