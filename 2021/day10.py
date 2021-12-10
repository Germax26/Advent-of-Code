# Syntax Scoring

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [x for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day10.txt")

brackets = {
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>'
}

scores = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

points = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
}

def parse_chunk(tokens, depth=0):
	token = tokens.pop()
	while tokens and tokens[-1] in brackets:
		err = parse_chunk(tokens, depth+1)
		if err: 
			if err[:4] == 'inc:':
				return err + brackets[token]
			return err
	if tokens:
		closing = tokens.pop()
		if closing != brackets[token]:
			return 'cor:' + closing # corrupted
	else:
		return 'inc:' + brackets[token]  # incomplete

def solve():
	total1 = 0
	total2 = []

	for line in puzzle_input:
		tokens = list(reversed(list(line)))
		while tokens:
			err = parse_chunk(tokens)

			if not err: continue

			err_code = err[:4]
			err_val = err[4:]

			if err_code == 'cor:':
				total1 += scores[err_val]
				break

			elif err_code == 'inc:':
				total = 0
				for i in err_val:
					total *= 5
					total += points[i]
				total2.append(total)
				break

	total2.sort()

	return total1, total2[int(len(total2)/2)]

answer1, answer2 = solve()

def solve1(): return answer1
def solve2(): return answer2

print("Pt1:", solve1())
print("Pt2:", solve2())