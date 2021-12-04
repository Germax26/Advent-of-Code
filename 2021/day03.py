# Binary Diagnostic

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [x for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file('inputs/day03.txt')
num_bits = len(puzzle_input[0])

def mostleastcommon(numbers, index):
	counts = [0, 0]
	for number in numbers:
		bit = int(number[index])
		counts[bit] += 1

	most = 0 if counts[0] > counts[1] else 1
	return most, 1 - most

def solve1():
	gamma = 0
	epsilon = 0
	for i in range(num_bits):
		most, least = mostleastcommon(puzzle_input, i)
		gamma += gamma + most
		epsilon += epsilon + least

	return gamma * epsilon

def solve2():
	oxylist = puzzle_input.copy()
	c02list = puzzle_input.copy()
	for bit in range(num_bits):
		most, _ = mostleastcommon(oxylist, bit)
		_, least = mostleastcommon(c02list, bit)

		if len(oxylist) > 1: oxylist = list(filter(lambda n: n[bit] == str(most), oxylist))
		if len(c02list) > 1: c02list = list(filter(lambda n: n[bit] == str(least), c02list))

	assert len(oxylist) == 1
	assert len(c02list) == 1

	return int(oxylist[0], 2) * int(c02list[0], 2)

	    
print("Pt1:", solve1())
print("Pt2:", solve2())