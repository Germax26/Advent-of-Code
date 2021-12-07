# Dive!

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [int(x) for x in _file.read().split(',')]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day07.txt")

def solve1():
	total = 0
	position = sorted(puzzle_input)[int(len(puzzle_input)/2)]
	for i in puzzle_input:
		total += abs(position - i)

	return total

def solve2():
	max_crabs = max(puzzle_input) + 1
	crabs = [puzzle_input.count(x) for x in range(max_crabs)]
	fuel = sum([x * int(i * (i+1) / 2) for i, x in enumerate(crabs)])
	position = 0

	diff = -1

	while diff < 0:
		diff = sum([crabs[i] * (position - i + (i <= position)) for i in range(max_crabs)])
		fuel += diff
		position += 1

	fuel -= diff

	return fuel

print("Pt1:", solve1())
print("Pt2:", solve2())