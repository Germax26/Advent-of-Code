# Dive !

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [x for x in _file.read().split('\n') if x]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day02.txt")

def solve1():
	position = 0
	depth = 0
	for instruction in puzzle_input:
		cmd, val = instruction.split()
		val = int(val)
		if cmd == "forward":
			position += val
		elif cmd == "down":
			depth += val
		elif cmd == "up":
			depth -= val
		else:
			raise Exception(f"Unknown command: {cmd}.")

	return position * depth

def solve2():
	position = 0
	depth = 0
	aim = 0
	for instruction in puzzle_input:
		cmd, val = instruction.split()
		val = int(val)
		if cmd == "forward":
			position += val
			depth += aim * val
		elif cmd == "down":
			aim += val
		elif cmd == "up":
			aim -= val
		else:
			raise Exception(f"Unknown command: {cmd}.")

	return position * depth

print("Pt1:", solve1())
print("Pt2:", solve2())