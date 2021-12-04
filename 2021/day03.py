# Binary Diagnostic

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [x for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file('inputs/day03.txt')
num_bits = len(puzzle_input[0])

def solve1():
	gamma = 0
	epsilon = 0
	for i in range(num_bits):
		counts = [0, 0]
		for number in puzzle_input:
			bit = int(number[i])
			counts[bit] += 1

		most = 0 if counts[0] > counts[1] else 1
		least = 1 - most

		gamma += gamma + most
		epsilon += epsilon + least
	return gamma * epsilon
	    
print("Pt1:", solve1())
# print("Pt2:", solve2())