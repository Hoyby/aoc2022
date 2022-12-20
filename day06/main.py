def getFirstMarker(input, markerLength=4):
    marker = ""
    for char in input:
        if len(marker) < markerLength:
            marker += char
        else:
            marker = marker[1:] + char
        if len(set(marker)) == markerLength:
            return input.index(marker) + markerLength, marker
    return -1, marker


def main(inp):
    # result1 = findMaxScore(inp)
    result2 = getFirstMarker(inp, 14)
    # print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day6/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    main(inp)
