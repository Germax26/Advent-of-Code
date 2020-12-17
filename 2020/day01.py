# Report Repair

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read()
    _file.close()
    return _read

def k_sum(nums, target, k): # O(n^k-1)
    if k == 1:
        if target in nums:
            return [nums.index(target)]
        return [-1]
    if k == 2:
        ptr1 = 0
        ptr2 = len(nums) - 1
        while ptr1 < ptr2:
            curr = nums[ptr1] + nums[ptr2]
            if curr < target:
                ptr1 += 1
            elif curr > target:
                ptr2 -= 1
            else:
                return [ptr1, ptr2]
        return [-1, -1]
    for n in range(0, len(nums)):
        diff = target - nums[n]
        k_sub_1_sum = k_sum(nums, diff, k - 1)
        if k_sub_1_sum != [-1] * (k - 1):
            if n not in k_sub_1_sum:
                return [n] + k_sub_1_sum
    return [-1] * k

def solve1(k=2):
    nums = sorted([int(n) for n in read_from_file("inputs/day01.input").split("\n")])
    total = 1
    for i in k_sum(nums, 2020, k):
        total *= nums[i]
    return total

def solve2():
    return solve1(3)

print('Pt1:', solve1())
print('Pt2:', solve2())
