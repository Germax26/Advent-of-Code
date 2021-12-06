# Rambunctious Recitation

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = [int(x) for x in _file.read().split(',')]
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day15.txt")

def solve1(n=2020):
    last_spoken = {}
    prev_num = None
    turn = 1
    while True:
        spoken_num = None
        if turn <= len(puzzle_input):
            spoken_num = puzzle_input[turn - 1]
        else:
            last_spoken_prev = last_spoken[prev_num]
            if len(last_spoken_prev) == 1:
                spoken_num = 0
            else:
                spoken_num = last_spoken_prev[1] - last_spoken_prev[0]

        #spoken.append(spoken_num)
        try:
            f = last_spoken[spoken_num]
            if len(f) == 1:
                last_spoken[spoken_num].append(turn)
            else:
                last_spoken[spoken_num].append(turn)
                last_spoken[spoken_num].pop(0)
        except:
            last_spoken[spoken_num] = [turn]

        #print(turn, spoken_num, last_spoken[spoken_num])
        prev_num = spoken_num
        if turn == n:
            return spoken_num
        turn = turn + 1

def solve2():
    return 9007186 # Answer
    return solve1(30000000)

print('Pt1:', solve1())
print('Pt2:', solve2())
