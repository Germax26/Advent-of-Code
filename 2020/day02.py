# Password Philosophy

def read_from_file(file_name):
    _file = open(file_name, "r")
    _read = _file.read().split("\n")
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day02.txt")

def solve1():
    i = 0
    for pwd in puzzle_input:
        spwd = pwd.split(": ")
        policy = spwd[0]
        password = spwd[1]

        spolicy = policy.split(" ")
        limit = spolicy[0]
        letter = spolicy[1]

        slimit = limit.split("-")
        lower = int(slimit[0])
        higher = int(slimit[1])

        c = password.count(letter)
        if c >= lower and c <= higher:
            i+=1
    return i

def xor(a, b):
    if a:
        return not b
    else:
        return b

def solve2():
    i = 0
    for pwd in puzzle_input:
        spwd = pwd.split(": ")
        policy = spwd[0]
        password = spwd[1]

        spolicy = policy.split(" ")
        limit = spolicy[0]
        letter = spolicy[1]

        slimit = limit.split("-")
        lower = int(slimit[0])
        higher = int(slimit[1])
        
        if xor(password[lower-1:lower] == letter, password[higher-1:higher] == letter):
            i+=1
    return i
    
print("Pt1:", solve1())
print("Pt2:", solve2())
