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

def play_bingo(winner_callback, board_filter):
	while called: called.pop()
	for call in order:
		called.append(call)
		for j, board in enumerate(boards):
			if not board_filter(j):
				continue
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
			
			result = winner_callback(call, board, j)
			if result != None:
				return result
				
def solve1():
	return play_bingo(lambda call, board, _: score(call, board), lambda i: True)

def solve2():
	left = set(range(len(boards)))

	def find_last(call, board, i):
		if len(left) > 1:
			left.remove(i)
		else:
			return score(call, board)

	return play_bingo(find_last, lambda i: i in left)

print("Pt1:", solve1())
print("Pt2:", solve2())