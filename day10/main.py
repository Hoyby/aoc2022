def sumSignalStr(inp):
    cOfInterest = [20, 60, 100, 140, 180, 220]
    result = []
    cCount = 0
    reg = 1

    for line in inp:
        parts = line.split(" ")
        if parts[0] == "noop":
            cCount += 1
            if cCount in cOfInterest:
                result.append(cCount * reg)
        else:
            cCount += 1
            if cCount in cOfInterest:
                result.append(cCount * reg)
            cCount += 1
            if cCount in cOfInterest:
                result.append(cCount * reg)
            value = int(parts[1])
            reg += value

    return sum(result)


def drawLetters(inp):
    cCount = 0
    reg = 1

    crt = ["." for _ in range(240)]

    for line in inp:
        if line.startswith("noop"):
            pixelX = cCount % 40
            crt[cCount % 240] = "#" if abs(reg - pixelX) <= 1 else "."
            cCount += 1
        else:
            pixelX = cCount % 40
            crt[cCount % 240] = "#" if abs(reg - pixelX) <= 1 else "."
            cCount += 1
            pixelX = cCount % 40
            crt[cCount % 240] = "#" if abs(reg - pixelX) <= 1 else "."
            cCount += 1

            value = int(line.split(" ")[1])
            reg += value

    return "\n".join("".join(crt[i : i + 40]) for i in range(0, 240, 40))


def main(inp):
    result1 = sumSignalStr(inp)
    result2 = drawLetters(inp)
    print("Result 1: ", result1)
    print("Result 2: \n", result2)


if __name__ == "__main__":
    with open("day10/input.txt", "r", encoding="utf-8") as f:
        inp = f.read().splitlines()
    main(inp)
