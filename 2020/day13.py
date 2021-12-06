# Shuttle Search

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read().split("\n")
    _file.close()
    return _read

puzzle_input = read_from_file("inputs/day13.txt")

earliest_time = int(puzzle_input[0])
bus_ids = puzzle_input[1].split(",")

waiting_ids = {}
waiting_times = []

ids = {}

def time_to_wait(_time, _id):
    return _id - (_time % _id)

def solve1():
    global earliest_time
    global bus_ids
    global waiting_ids
    for bus_id, i in zip(bus_ids, range(0, len(bus_ids))):
        if bus_id == 'x':
            continue
        waiting_times.append(time_to_wait(earliest_time, int(bus_id))) 
        waiting_ids[waiting_times[-1]] = int(bus_id)
        ids[int(bus_id)] = i
    return waiting_ids[min(waiting_times)] * min(waiting_times)


def solve2():
    global ids
    minValue = 0
    runningProduct = 1
    for k, v in zip(ids.keys(), ids.values()):
        while (minValue + v) % k != 0:
            minValue += runningProduct
        runningProduct *= k
    return minValue

print('Pt1:', solve1())
print('Pt2:', solve2())
