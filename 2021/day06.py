# Lanternfish

from collections import deque

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [int(x) for x in _file.read().split(',') if x]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day06.txt")

def solve1(days=80):
	fish = deque([puzzle_input.count(x) for x in range(10)])
	for day in range(days):
		zeros = fish.popleft()
		fish[6] += zeros
		fish[8] += zeros
		fish.append(0)
	return sum(fish)

def solve2():
	return solve1(days=256)

print("Pt1:", solve1())
print("Pt2:", solve2())