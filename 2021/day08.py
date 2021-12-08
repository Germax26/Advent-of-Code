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
		total += sum([len_.count(x) for x in [2, 4, 3, 7]])
	return total

def solve2():
	numbers = {
		0: 'abcefg',
		1: 'cf',
		2: 'acdeg',
		3: 'acdfg',
		4: 'bcdf',
		5: 'abdfg',
		6: 'abdefg',
		7: 'acf',
		8: 'abcdefg',
		9: 'abcdfg'
	}

	numbers = {x: list(numbers[x]) for x in numbers}

	total = 0

	for line in puzzle_input:
		digits = sorted(line[0], key=len)
		rest = line[1]

		cf = set(digits[0])
		acf = set(digits[1])
		adg = set.intersection(*map(set, digits[3:6]))
		abfg = set.intersection(*map(set, digits[6:9]))
		abcdefg = set(digits[9])

		a = acf - cf
		f = abfg & cf
		g = adg & abfg - a
		d = adg - a - g
		b = abfg - a - f - g
		c = cf - f
		e = abcdefg - adg - c - b - f

		connections = {
			list(a)[0]: 'a',
			list(b)[0]: 'b',
			list(c)[0]: 'c',
			list(d)[0]: 'd',
			list(e)[0]: 'e',
			list(f)[0]: 'f',
			list(g)[0]: 'g'
		}

		output = ''

		for number in rest:
			converted = sorted(map(lambda x: connections[x], number))
			output += str(([x[0] for x in numbers.items() if x[1] == converted][0]))

		total += int(output)

	return total

print("Pt1:", solve1())
print("Pt2:", solve2())