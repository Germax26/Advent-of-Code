# Seating System

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read().split('\n')
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day11.txt")
grid = [list(i) for i in puzzle_input]
prev_grid = [[i for i in j] for j in grid]

def num_neighbors(grid, row, col, tolerance, part):
    assert(part in [1, 2])

    num_occupied = 0
    if part == 1: # Adjecent
        for i in range(-1, 2):
            if row + i >= 0 and row + i < len(grid):
                for j in range(-1, 2):
                    if col + j >= 0 and col + j < len(grid[row]):
                        if i == 0 and j == 0:
                            continue
                        neighbor = grid[row+i][col+j]
                        if neighbor == "#":
                            num_occupied += 1
    elif part == 2:
        for set_dir in [[[-1, -1], [-1, 1], [1, -1], [1, 1]], [[0, -1], [1, 0], [0, 1], [-1, 0]]]:
            for _dir in set_dir:
                dx = _dir[0]
                dy = _dir[1]
                while (row + dy >= 0) and (row + dy < len(grid)) and (col + dx >= 0) and (col + dx < len(grid[row])):
                    neighbor = grid[row + dy][col + dx]
                    if neighbor in ["#", "L"]:
                        if neighbor == "#":
                            num_occupied += 1
                        break
                    dx += _dir[0]
                    dy += _dir[1]
    return num_occupied

def step(grid, tolerance, part):
    new_grid = []
    for row in range(0, len(grid)):
        new_grid.append([])
        for col in range(0, len(grid[row])):
            me = grid[row][col]
            new_me = me
            num_occupied = 0
            if me != '.':
                num_occupied = num_neighbors(grid, row, col, tolerance, part)
            if num_occupied == 0 and me == "L":
                new_me = "#"
            elif num_occupied >= tolerance and me == "#":
                new_me = "L"
            new_grid[row].append(new_me)
    return new_grid

def solve1(part=1, tolerance=4):
    global prev_grid
    global grid
    while True:
        grid = step(grid, tolerance, part)
        isSame = True
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if prev_grid[i][j] != grid[i][j]:
                    isSame = False
                    break

        if isSame:
            return sum([row.count("#") for row in grid])
        prev_grid = grid

def solve2():
    global grid
    global prev_grid
    grid = [list(i) for i in puzzle_input]
    prev_grid = [[i for i in j] for j in grid]
    return solve1(2, 5)

print('Pt1:', solve1())
print('Pt2:', solve2())
