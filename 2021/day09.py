# Smoke Basin

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [list(map(int, x)) for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day09.txt")

def solve1():
	total = 0
	for j in range(len(puzzle_input)):
		for i in range(len(puzzle_input[j])):
			for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
				if i + dx >= 0 and j + dy >= 0 and i + dx < len(puzzle_input[j]) and j + dy < len(puzzle_input):
					if puzzle_input[j][i] >= puzzle_input[j + dy][i + dx]:
						break
			else:
				total += 1 + puzzle_input[j][i]

	return total

def solve2():
	pass

print("Pt1:", solve1())
# print("Pt2:", solve2())