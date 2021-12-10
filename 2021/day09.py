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
	flow = []
	basins = []
	for j in range(len(puzzle_input)):
		flow.append([])
		for i in range(len(puzzle_input[j])):
			x = (0, 0)
			h = puzzle_input[j][i]

			if h != 9:
				for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
					if i + dx >= 0 and j + dy >= 0 and i + dx < len(puzzle_input[j]) and j + dy < len(puzzle_input):
						if puzzle_input[j + dy][i + dx] < h:
							x = (dx, dy)
			else:
				x = 9

			if x == (0, 0):
				basins.append((i, j))
			flow[j].append(x)

	def calculate_area(x, y):
		area = 1
		for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			if x + dx >= 0 and y + dy >= 0 and x + dx < len(puzzle_input[y]) and y + dy < len(puzzle_input):
				if puzzle_input[y + dy][x + dx] == 9:
					continue
				if flow[y + dy][x + dx] == (-dx, -dy):
					area += calculate_area(x + dx, y + dy)
		return area

	areas = []

	for basin in basins:
		areas.append(calculate_area(*basin))

	total = 1
	for i in sorted(areas)[-3:]:
		total *= i
		
	return total


print("Pt1:", solve1())
print("Pt2:", solve2())