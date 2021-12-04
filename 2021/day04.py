# Giant Squid

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [x for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file('inputs/day04_simple.txt')

order = [int(x) for x in puzzle_input[0].split(',')]
called = []

boards = [[[int(y) for y in x.split()] for x in puzzle_input[n:n+5]] for n in range(1, len(puzzle_input), 5)]

def solve1():
	pass

def solve2():
	pass
	    
print("Pt1:", solve1())
# print("Pt2:", solve2())