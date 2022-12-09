test = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

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


def main(data):
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
    print(len(locationsTask1))
    print(len(locationsTask2))


if __name__ == "__main__":
    main(input)
