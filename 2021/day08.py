# Seven Segment Search

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [[y.split(' ') for y in x.split(' | ')] for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day08.txt")

def solve1():
	total = 0
	for line in puzzle_input:
		len_ = list(map(len, line[1]))
		print(line[1], len_)
		total += sum([len_.count(x) for x in [2, 4, 3, 7]])
	return total

def solve2():
	pass

print("Pt1:", solve1())
# print("Pt2:", solve2())