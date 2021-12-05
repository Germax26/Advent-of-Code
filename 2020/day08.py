# Handheld Halting

def result(code):

    ac = 0 # Accumulator
    ix = 0 # Index
    ex = [False] * len(code) # Executed

    while True:
        nx = ix + 1 # Next Index

        if ix >= len(code):
            return [ac, True] 
        if ex[ix]:
            return [ac, False]
        ex[ix] = True

        op  = code[ix][:3]
        arg = code[ix][4:]

        if op == 'acc':
            ac += int(arg)
        elif op == 'jmp':
            nx += int(arg) - 1
        elif op == 'nop':
            pass

        # Increment index
        ix = nx

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read().split('\n')
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day08.txt")
    
def solve1():
    return result(puzzle_input)[0]

def solve2():
    global puzzle_input

    for replacement in [["nop", "jmp"], ["jmp", "nop"]]:
            for i in range(0, len(puzzle_input)):
                if puzzle_input[i][:3] == replacement[0]:
                    puzzle_input[i] = replacement[1] + puzzle_input[i][3:]
                    if (_result:=result(puzzle_input))[1]:
                        return _result[0]
                    else:
                        puzzle_input = read_from_file("inputs/day08.txt")

print("Pt1:", solve1())
print("Pt2:", solve2())
