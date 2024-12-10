import numpy as np

with open('input.txt') as f:
    data = np.array([[int(x) for x in list(line.strip())] for line in f])

def is_within_bounds(pos, arr):
    return 0 <= pos[0] < arr.shape[0] and 0 <= pos[1] < arr.shape[1]

padded = np.pad(data, 1, mode='constant')
start_pos_list = np.argwhere(data == 0)

directions = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1)
]

def findScore(pos, result):
    if data[tuple(pos)] == 9:
        result.add(tuple(pos))
    for d in directions:
        next_pos = pos + d
        if is_within_bounds(next_pos, data) and data[tuple(pos)] + 1 == data[tuple(next_pos)]:
            findScore(next_pos, result)

def findRating(pos):
    result = 0
    if data[tuple(pos)] == 9:
        return 1
    for d in directions:
        next_pos = pos + d
        if is_within_bounds(next_pos, data) and data[tuple(pos)] + 1 == data[tuple(next_pos)]:
            result += findRating(next_pos)
    return result

part1 = 0
part2 = 0
for start_pos in start_pos_list:
    part1set = set()
    findScore(start_pos, part1set)
    part1 += len(part1set)
    part2 += findRating(start_pos)

print(part1, part2)