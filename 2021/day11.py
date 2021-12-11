# Dumbo Octopus

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [list(map(int, x)) for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day11.txt")

pm1 = [-1, 0, 1]

def solve():
	answer1, answer2 = 0, 0

	octopuses = puzzle_input

	size = len(octopuses) * len(octopuses[0])

	num_flashes = 0

	step = 1
	while True:
		old_flashes = num_flashes

		octopuses = [[octopus + 1 for octopus in row] for row in octopuses]

		new_octopuses = octopuses.copy()

		should_break = False
		while not should_break:
			should_break = True
			for y, row in enumerate(octopuses):
				for x, octopus in enumerate(row):
					if octopus > 9:
						num_flashes += 1
						new_octopuses[y][x] = 0
						for dx in pm1:
							for dy in pm1:
								nx, ny = x + dx, y + dy
								if nx >= 0 and nx < len(row) and ny >= 0 and ny < len(octopuses):
									if new_octopuses[ny][nx]:
										new_octopuses[ny][nx] += 1
										if new_octopuses[ny][nx] > 9:
											should_break = False

		octopuses = new_octopuses

		if step == 100:
			answer1 = num_flashes
		if num_flashes - old_flashes == size:
			answer2 = step
			break

		step += 1

	return answer1, answer2

answer1, answer2 = solve()

print("Pt1:", answer1)
print("Pt2:", answer2)