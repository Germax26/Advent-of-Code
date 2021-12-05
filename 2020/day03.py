# Toboggan Trajectory

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read().split("\n")
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day03.txt")

def solve1(dx=3, dy=1):
    width = len(puzzle_input[0])

    num_trees = 0
    y = 0
    x = 0
    while True:

        x += dx
        y += dy
        if y >= len(puzzle_input):
            break
        if puzzle_input[y][x % width] == "#":
            num_trees+=1
    return num_trees

def solve2():
    i = 1
    for k in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        i *= solve1(k[0], k[1])
    return i
    
print("Pt1:", solve1())
print("Pt2:", solve2())
