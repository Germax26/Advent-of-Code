# Binary Boarding

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read()
    _file.close()
    return _read

def solve1(final=lambda possible, highest, lowest: highest):
    seats = read_from_file("inputs/day05.input").split("\n")
    possible = [[True, i] for i in range(0, 1024)]
    lowest = len(possible)
    highest = 0
    for seat in seats:
        val = ""
        for i in list(seat):
            if i == "F" or i == "L":
                val += "0"
            if i == "B" or i == "R":
                val += "1"
        highest = max(highest, int(val, 2))
        lowest = min(lowest, int(val, 2))
        possible[int(val, 2)][0] = False
    return final(possible, highest, lowest)


def solve2():
    return solve1(lambda possible, highest, lowest: [x[1] for x in possible if x[0] if x[1] > lowest  if x[1] < highest][0])

print("Pt1:", solve1())
print("Pt2:", solve2())
