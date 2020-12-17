# Ticket Translation

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read()
    _file.close()
    return _read

puzzle_input = read_from_file('inputs/day16.input').split("\n")
pzi = [[], []]
rules = []
tickets = []
possible = []

def parse(f):
    global pzi
    global puzzle_input
    global rules
    global tickets
    global possible
    
    n = 0
    for i in f:
        if i in ['your ticket:', 'nearby tickets:']:
            n = 1
        else:
            pzi[n].append(i)
    rules = pzi[0]
    tickets = pzi[1]
    pzi[1].remove('')

    for i in range(0, len(rules)):
        rules[i] = rules[i].split(": ")
        if rules[i] != ['']:
            rules[i][1] = rules[i][1].split(" or ")
            for j in range(0, len(rules[i][1])):
                rules[i][1][j] = [int(n) for n in rules[i][1][j].split("-")]

    for i in range(0, len(tickets)):
        tickets[i] = [int(n) for n in tickets[i].split(",")]

    rules.remove([''])
    
    for i in range(0, len(tickets[0])):
        possible.append(set([rule[0] for rule in rules]))\

def solve1():
    global rules
    global tickets
    global possible
    error_rate = 0
    for ticket in tickets[1:]:
        position = 0
        for value in [int(v) for v in ticket]:
            fields = set()
            for rule in rules:
                if (value >= rule[1][0][0] and value <= rule[1][0][1]) or (value >= rule[1][1][0] and value <= rule[1][1][1]):
                    fields.add(rule[0])
            if len(fields) == 0:
                error_rate += value
            else:
                possible[position] = possible[position].intersection(fields)
            position += 1
    return error_rate

def solve2():
    global rules
    global tickets
    global possible

    queue = []
    completed = []

    while True:
        if queue == []:
            for seat in possible:
                if len(seat) == 1:
                    field = [e for e in seat][0]
                    if field not in completed:
                        queue.append([e for e in seat][0])
                        completed.append(queue[-1])
                        break
            else:
                break
        else:
            for seat in possible:
                if queue[0] in seat:
                    if len(seat) != 1:
                        seat.remove(queue[0])
            queue.pop(0)

    total = 1
    for i, v, in zip(range(0, len(possible)), [list(j)[0] for j in possible]):
        if v.startswith('departure'):
            total *= tickets[0][i]
    return total

parse(puzzle_input)
print('Pt1:', solve1())
print('Pt2:', solve2())
