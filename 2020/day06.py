# Custom Customs

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read().split("\n\n")
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day06.txt")

def solve(f):
    total = 0
    for group in puzzle_input:
        num_people = len(group.split("\n"))
        num_questions = 0
        for l in [chr(x) for x in range(97, 123)]:
            if f(group.count(l), num_people):
                num_questions += 1
        total += num_questions
    return total

def solve1():
    return solve(lambda a, b : a >= 1)

def solve2():
    return solve(lambda a, b : a == b)

print("Pt1:", solve1())
print("Pt2:", solve2())
