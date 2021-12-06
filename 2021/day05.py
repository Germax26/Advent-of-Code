# Hydrothermal Venture

def sign(x):
	'''
	I really hate the fact that python doesn't have its own sign() function.
	This also happens in math. There's a notation for abs(), which is | |,
	but no notation for sign()! You have to use the word 'sign'!
	
	WTF!
	'''

	# In this implementation, sign(0) = 0

	if x: return int(abs(x) / x)
	return x

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [x for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = [[tuple([int(y) for y in x.split(',')]) for x in line.split(' -> ')] for line in read_from_file("inputs/day05.txt")]

def solve1(include_diags=False):
	counts = {}
	for line in puzzle_input:

		A = line[0]
		B = line[1]

		x = A[0]
		y = A[1]

		dx = sign(B[0] - A[0])
		dy = sign(B[1] - A[1])

		if not include_diags and dx != 0 and dy != 0: continue

		while x != B[0] or y != B[1]:
			
			pos = (x, y)
			counts[pos] = counts.get(pos, 0) + 1
			x += dx
			y += dy

		pos = (x, y)
		counts[pos] = counts.get(pos, 0) + 1

	return len([x for x in counts if counts[x] > 1])

def solve2():
	return solve1(include_diags=True)

print("Pt1:", solve1())
print("Pt2:", solve2())