import Intcode.vm as Intcode

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read()
    _file.close()
    return _read

def solve1():
    ops = read_from_file("inputs/day02.input").split(",")
    code = []
    for i in ops:
        code.append(int(i))
    code[1] = 12
    code[2] = 2
    return Intcode.result(code)[0]

def solve2():
    ops = read_from_file("inputs/day02.input").split(",")
    code = []
    for i in ops:
        code.append(int(i))
    for i in range(0, 100):
        for j in range(0, 100):
            code[1] = i
            code[2] = j
            if Intcode.result(code)[0] == 19690720:
                return 100 * i + j

print('Pt1:', solve1())
print('Pt2:', solve2())
