import math

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read()
    _file.close()
    return _read

masses = read_from_file("inputs/day01.input").split("\n")

def solve1():
    total = 0
    for i in masses:
        total += math.floor(float(i) / 3) - 2
    return total

def fuel(n):
    k = math.floor(float(n) / 3) - 2
    if k > 0:
        return k + fuel(k)
    return 0

def solve2():
    total = 0
    for i in masses:
        total += fuel(float(i))
    return total

print('Pt1:', solve1())
print('Pt2:', solve2())
