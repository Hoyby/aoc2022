def find_common_letters(inp):
    common_letters = []
    for line in inp.splitlines():
        common_letters.append(set(line[: len(line) // 2]) & set(line[len(line) // 2 :]))
    return common_letters


def find_common_letter_priority(common_letters):
    priority = 0
    for common_letter in common_letters:
        if len(common_letter) == 1:
            letter = common_letter.pop()
            if letter.islower():
                priority += ord(letter) - 96
            else:
                priority += ord(letter) - 38
    return priority


def find_badge_letters(inp, group_size=3):
    badge_letters = []
    for i in range(0, len(inp.splitlines()), group_size):
        badge_letters.append(
            set(inp.splitlines()[i])
            & set(inp.splitlines()[i + 1])
            & set(inp.splitlines()[i + 2])
        )
    return badge_letters


def main(inp):
    result1 = find_common_letter_priority(find_common_letters(inp))
    result2 = find_common_letter_priority(find_badge_letters(inp))
    print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day3/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    main(inp)
