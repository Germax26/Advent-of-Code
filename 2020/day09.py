# Encoding Error

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read()
    _file.close()
    return _read

solution1 = 0
index = 0
nums = [int(x) for x in read_from_file("inputs/day09.input").split("\n")]

def solve1():
    global solution1
    global index
    global nums
    preamble = 25
    for n in range(preamble, len(nums)):
        isValid = False
        for i in nums[n-preamble:n]:
            shouldBreak = False
            for j in nums[n-preamble:n]:
                if i + j == nums[n]:
                    isValid = True
                    shouldBreak = True
                    break
            if shouldBreak:
                break
        if not isValid:
            solution1 = nums[n]
            index = n
            return nums[n]

def solve2():
    global nums
    for i in range(0, index):
        for j in range(i + 1, index):
            if sum(nums[i:j+1]) == solution1:
                return min(nums[i:j+1])+ max(nums[i:j+1])


print("Pt1:", solve1())
print("Pt2:", solve2())
