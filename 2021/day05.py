# Hydrothermal Venture

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [x for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = [[tuple([int(y) for y in x.split(',')]) for x in line.split(' -> ')] for line in read_from_file("inputs/day05.txt")]

counts = {}

def solve1():
	for line in puzzle_input:
		A = line[0]
		B = line[1]
		if A[0] != B[0] and A[1] != B[1]: continue
		for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
			for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
				counts[(x, y)] = counts.get((x, y), 0) + 1

	return len([x for x in counts if counts[x] > 1])

def solve2():
	pass

print("Pt1:", solve1())
#print("Pt2:", solve2())