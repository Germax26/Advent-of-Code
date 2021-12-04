# Sonar Sweep

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [int(x) for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file('inputs/day01.txt')

def solve1(window=1):
	total = 0
	for i, depth in enumerate(puzzle_input[window:]):
		if depth > puzzle_input[i]:
			total += 1
	return total

def solve2():
	return solve1(window=3)
	    
print("Pt1:", solve1())
print("Pt2:", solve2())