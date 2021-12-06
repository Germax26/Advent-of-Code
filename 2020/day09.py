# Encoding Error

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [int(x) for x in _file.read().split('\n')]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day09.txt")

solution1 = 0
index = 0

def solve1():
    global solution1
    global index
    preamble = 25
    for n in range(preamble, len(puzzle_input)):
        isValid = False
        for i in puzzle_input[n-preamble:n]:
            shouldBreak = False
            for j in puzzle_input[n-preamble:n]:
                if i + j == puzzle_input[n]:
                    isValid = True
                    shouldBreak = True
                    break
            if shouldBreak:
                break
        if not isValid:
            solution1 = puzzle_input[n]
            index = n
            return puzzle_input[n]

def solve2():
    global nums
    for i in range(0, index):
        for j in range(i + 1, index):
            if sum(puzzle_input[i:j+1]) == solution1:
                return min(puzzle_input[i:j+1])+ max(puzzle_input[i:j+1])


print("Pt1:", solve1())
print("Pt2:", solve2())
