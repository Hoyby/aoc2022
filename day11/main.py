class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def __str__(self):
        return f"{self.items}, {self.operation}, {self.test}"


def makeMonkeys(monkey_parts):
    monkeys = []
    for _, monkey_part in enumerate(monkey_parts):
        lines = monkey_part.split("\n")
        items = list(map(int, lines[1][2:].split(" ", 2)[2].split(", ")))
        operation = lines[2][2:].split(" ", 3)[3].split(" ")

        mod = int(lines[3][2:].split(" ")[-1])
        if_true = int(lines[4][4:].split(" ")[-1])
        if_false = int(lines[5][4:].split(" ")[-1])

        monkeys.append(Monkey(items, operation, [mod, if_true, if_false]))
    return monkeys


def expr(operation, x, mod):
    left, op, right = operation

    assert left == "old"

    if op == "+":
        ans = x + int(right)
    else:
        if right == "old":
            ans = x * x
        else:
            ans = x * int(right)

    return ans % mod


def calcInspections(monkeys, rounds, task1):
    mod = 1
    for monkey in monkeys:
        mod *= monkey.test[0]

    n = len(monkeys)

    for _ in range(rounds):
        for i in range(n):
            monkey = monkeys[i]
            for itemsWorryLvl in monkey.items:
                itemsWorryLvl = expr(monkey.operation, itemsWorryLvl, mod)
                if task1:
                    itemsWorryLvl //= 3

                mod, if_true, if_false = monkey.test
                if itemsWorryLvl % mod == 0:
                    monkeys[if_true].items.append(itemsWorryLvl)
                else:
                    monkeys[if_false].items.append(itemsWorryLvl)

                monkey.inspections += 1

            monkey.items = []
    return sorted([m.inspections for m in monkeys])


def main(inp):
    monkeys = makeMonkeys(inp)
    inspectedItems1 = calcInspections(monkeys, 20, task1=True)
    inspectedItems2 = calcInspections(monkeys, 10000, task1=False)
    result1 = inspectedItems1[-1] * inspectedItems1[-2]
    result2 = inspectedItems2[-1] * inspectedItems2[-2]
    print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day11/input.txt", "r", encoding="utf-8") as f:
        inp = f.read().strip().split("\n\n")
    main(inp)
