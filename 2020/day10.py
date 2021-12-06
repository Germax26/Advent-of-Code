# Adapter Array

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read().split("\n")
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day10.txt")
nums = sorted(puzzle_input)

def solve1():
    snums = [0] + nums
    diffs = [snums[n] - snums[n - 1] for n in range(1, len(snums))]
    return diffs.count(1) * (diffs.count(3)+1)


def solve2():
    nums.insert(0, 0)
    nums.append(max(nums)+3)
    arrange = [1]+[0]*nums[-1]
    for i in nums[1:]: 
        arrange[i] = arrange[i-3] + arrange[i-2] + arrange[i-1] # Tribinacci
    return arrange[-1]

print('Pt1:', solve1())
print('Pt2:', solve2())
