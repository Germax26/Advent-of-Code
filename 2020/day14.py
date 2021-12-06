# Docking Data

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read().split("\n")
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day14.txt")

memory = {}
mask = ''

def solve1(part=1):
    global puzzle_input
    global memory
    global mask
    mask = ''
    memory = {}
    for i in puzzle_input:
        j = i.split(" = ")
        instr = j[0]
        value = j[1]
        if instr == 'mask':
            mask = value
        else:
            loc = int(instr.split("[")[1][:-1])
            value = int(value)
            if part == 1:
                bvalue = bin(value)[2:]
                bvalue = '0' * (36 - len(bvalue)) + bvalue
                wvalue = ''
                for i in range(0, 36):
                    if mask[i] in ['0', '1']:
                        wvalue += mask[i]
                    elif mask[i] == 'X':
                        wvalue += bvalue[i]
                dvalue = int(wvalue, 2)
                memory[loc] = dvalue
            elif part == 2:
                bloc = bin(loc)[2:]
                bloc = '0' * (36 - len(bloc)) + bloc

                wloc = ''
                num_xs = 0
                for i in range(0, 36):
                    if mask[i] == '0':
                        wloc += bloc[i]

                    elif mask[i] in ['1', 'X']:
                        wloc += mask[i]
                        if mask[i] == 'X':
                            num_xs += 1
                for i in range(0, pow(2, num_xs)):
                    bi = bin(i)[2:]
                    bi = '0' * (num_xs - len(bi)) + bi

                    dloc = ''
                    x = 0
                    for j in range(0, 36):
                        if wloc[j] in ['0', '1']:
                            dloc += wloc[j]
                        else:
                            dloc += bi[x]
                            x += 1
                    memory[int(dloc, 2)] = value
    total = 0
    for i in memory.values():
        total += i
    return total
    



def solve2():
    return solve1(2)

print('Pt1:', solve1())
print('Pt2:', solve2())
