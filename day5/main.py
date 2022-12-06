with open("day5/input.txt", "r", encoding="utf-8") as f:
    input = f.read()

test = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def parse_input(input):
    stacks = []
    moves = []
    for line in input.splitlines():
        if len(line) < 2:
            continue
        if line.startswith("move"):
            moves.append(parse_moves(line))
        elif (line.startswith("[") | line.startswith(" ")) and (
            line.endswith("]") | line.endswith(" ")
        ):
            stacks.append(parse_stacks(line))
    stacks = stacks[:-1]
    return transposeAndParse(stacks), moves


def parse_moves(line):
    move, ammount, _, from_, _, to = line.split()
    return (int(ammount), int(from_), int(to))


def parse_stacks(line):
    spaceCount = 0
    row = []
    for letter in line:
        if letter == "[":
            spaceCount = 0
            continue
        elif letter == "]":
            spaceCount = 0
            continue
        elif spaceCount < 3 and letter == " ":
            spaceCount += 1
            continue
        elif spaceCount == 3:
            row.append("")
            spaceCount = 0
            continue
        elif letter != " " and letter.isalpha():
            spaceCount = 0
            row.append(letter)
    return row


def transposeAndParse(stacks):
    transposed = list(map(list, zip(*stacks)))
    transposed = [row[::-1] for row in transposed]
    transposed = [list(filter(None, row)) for row in transposed]
    return transposed


def prettyPrint(stacks):
    for row in stacks:
        print("".join(["[" + crate + "]" for crate in row]))


def main(inp):
    stacks, moves = parse_input(inp)
    for move in moves:
        ammount, from_, to = move

        # keep same order when ammount > 1
        if ammount > 1:
            stacks[to - 1].extend(stacks[from_ - 1][-ammount:])
            stacks[from_ - 1] = stacks[from_ - 1][:-ammount]
        else:
            stacks[to - 1].append(stacks[from_ - 1].pop())

        # move one at a time
        # for _ in range(ammount):
        #     stacks[to - 1].append(stacks[from_ - 1].pop())

    print("".join([stack[-1] for stack in stacks]))


if __name__ == "__main__":
    main(input)
