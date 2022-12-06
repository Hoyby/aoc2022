with open("day6/input.txt", "r", encoding="utf-8") as f:
    input = f.read()

test = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


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


def main():
    print(getFirstMarker(input, 14))


if __name__ == "__main__":
    main()
