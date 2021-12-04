# Sonar Sweep

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [int(x) for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file('inputs/day01.txt')

def solve1():
	total = 0
	for i, depth in enumerate(puzzle_input[1:]):
		if depth > puzzle_input[i]:
			total += 1
	return total
    
print("Pt1:", solve1())