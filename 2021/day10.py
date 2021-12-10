# Syntax Scoring

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [x for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day10.txt")

def solve1():
	brackets = {
			'(': ')',
			'[': ']',
			'{': '}',
			'<': '>'
		}

	score = {
		')': 3,
		']': 57,
		'}': 1197,
		'>': 25137
	}

	def parse_chunk(tokens):
			token = tokens.pop()
			if token in brackets:
				while tokens and tokens[-1] in brackets:
					err = parse_chunk(tokens)
					if err: return err
				if tokens:
					closing = tokens.pop()
					if closing != brackets[token]:
						return closing
				else:
					return 'incomplete'
			else:
				return 'unmatched' # never reached in given input?

	total = 0

	for line in puzzle_input:
		tokens = list(reversed(list(line)))
		while tokens:
			err = parse_chunk(tokens)
			if err and err != 'incomplete':
				total += score[err]
				break


	return total

def solve2():
	pass

print("Pt1:", solve1())
# print("Pt2:", solve2())