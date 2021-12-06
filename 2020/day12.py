# Rain Risk

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read().split('\n')
    _file.close()
    return _read

dir = "E"
left = {
    "E": "N",
    "N": "W",
    "W": "S",
    "S": "E"
}
right = {
    "E": "S",
    "N": "E",
    "W": "N",
    "S": "W"
}
x = 0
y = 0

wx = 10
wy = 1

puzzle_input = read_from_file("inputs/day12.txt")

def solve1():
    global x
    global y
    # global puzzle_input
    global left
    global dir
    global right
    for instruction in puzzle_input:
        action = instruction[:1]
        value = int(instruction[1:])
        if instruction[:1] == "N":
            y += int(instruction[1:])
        elif instruction[:1] == "E":
            x += int(instruction[1:])
        elif instruction[:1] == "S":
            y -= int(instruction[1:])
        elif instruction[:1] == "W":
            x -= int(instruction[1:])
        elif instruction[:1] == "L":
            if instruction[1:] == "90":
                dir = left[dir]
            elif instruction[1:] == "180":
                dir = left[left[dir]]
            elif instruction[1:] == "270":
                dir = right[dir]
            else:
                print(instruction[1:])
        elif instruction[:1] == "R":
            if instruction[1:] == "90":
                dir = right[dir]
            elif instruction[1:] == "180":
                dir = left[left[dir]]
            elif instruction[1:] == "270":
                dir = left[dir]
            else:
                print(instruction[1:])
        elif instruction[:1] == "F":
            if dir == "N":
                y += int(instruction[1:])
            elif dir == "E":
                x += int(instruction[1:])
            elif dir == "S":
                y -= int(instruction[1:])
            elif dir == "W":
                x -= int(instruction[1:])
    return abs(x) + abs(y)

def solve2():
    global x
    global y
    global wx
    global wy
    # global puzzle_input
    for instruction in puzzle_input:
        action = instruction[:1]
        value = int(instruction[1:])
        if action == "N":
            wy += value
        elif action == "E":
            wx += value
        elif action == "S":
            wy -= value
        elif action == "W":
            wx -= value
        elif action == "L":
            new_x = 0
            new_y = 0
            if value == 90:
                new_x = -wy
                new_y = wx
            elif value == 180:
                new_x = -wx
                new_y = -wy
            elif value == 270:
                new_x = wy
                new_y = -wx
            else:
                print("unknown", value)
            wx = new_x
            wy = new_y
        elif action == "R":
            new_x = 0
            new_y = 0
            if value == 90:
                new_x = wy
                new_y = -wx
            elif value == 180:
                new_x = -wx
                new_y = -wy
            elif value == 270:
                new_x = -wy
                new_y = wx
            else:
                print("unknown", value)
            wx = new_x
            wy = new_y
        elif action == "F":
            x += wx * value
            y += wy * value
    return abs(x) + abs(y)

print('Pt1:', solve1())
print('Pt2:', solve2())
