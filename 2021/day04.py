# Giant Squid

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [x for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file('inputs/day04.txt')

order = [int(x) for x in puzzle_input[0].split(',')]
called = []

boards = [[[int(y) for y in x.split()] for x in puzzle_input[n:n+5]] for n in range(1, len(puzzle_input), 5)]

def score(call, board):
	return sum([sum([x for x in row if x not in called]) for row in board]) * call

def solve1():
	for call in order:
		called.append(call)
		for board in boards:
			for row in board:
				for number in row:
					if number not in called:
						break
				else:
					break
			else:
				for i in range(5):
					for row in board:
						if row[i] not in called:
							break
					else:
						break
				else:
					continue
			return score(call, board)

def solve2():
	while called: called.pop()
	left = set(range(len(boards)))
	for call in order:
		called.append(call)
		for i, board in enumerate(boards):
			if i not in left:
				continue
			for row in board:
				for number in row:
					if number not in called:
						break
				else:
					break
			else:
				for j in range(5):
					for row in board:
						if row[j] not in called:
							break
					else:
						break
				else:
					continue
			if len(left) > 1:
				left.remove(i)
			else:
				return score(call, board)
	    
print("Pt1:", solve1())
print("Pt2:", solve2())