with open("day9/input.txt", "r", encoding="utf-8") as f:
    input = f.read()


def moveTail(head, tail):
    x = head[0] - tail[0]
    y = head[1] - tail[1]
    if abs(x) <= 1 and abs(y) <= 1:  # Tail is next to head
        pass
    elif abs(x) >= 2 and abs(y) >= 2:  # Tail is diagonal to head
        tail = (
            head[0] - 1 if tail[0] < head[0] else head[0] + 1,
            head[1] - 1 if tail[1] < head[1] else head[1] + 1,
        )
    elif abs(x) >= 2:  # Tail is horizontal to head
        tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1])
    elif abs(y) >= 2:  # Tail is vertical to head
        tail = (head[0], head[1] - 1 if tail[1] < head[1] else head[1] + 1)
    return tail


def calc_rope(data):
    head = (0, 0)
    tail = [(0, 0) for _ in range(9)]
    moves = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    locationsTask1 = set([tail[0]])
    locationsTask2 = set([tail[8]])
    for ins in data.splitlines():
        direction, ammount = ins.split()
        ammount = int(ammount)
        for _ in range(ammount):
            head = head[0] + moves[direction][0], head[1] + moves[direction][1]
            tail[0] = moveTail(head, tail[0])
            for i in range(1, 9):
                tail[i] = moveTail(tail[i - 1], tail[i])
            locationsTask1.add(tail[0])
            locationsTask2.add(tail[8])
    return len(locationsTask1), len(locationsTask2)


def main(inp):
    result1, result2 = calc_rope(inp)
    print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day9/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    main(inp)
