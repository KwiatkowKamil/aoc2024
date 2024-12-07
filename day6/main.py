import numpy as np


def is_within_bounds(pos, arr):
    return 0 <= pos[0] < arr.shape[0] and 0 <= pos[1] < arr.shape[1]


def turn_right(vector):
    return vector[1], -vector[0]


def walk(pos, direction, arr, check_loop=False):
    visited_with_direction = set()
    visited_positions = set()
    while True:
        next_pos = pos + direction
        if not is_within_bounds(next_pos, arr):
            break
        if arr[tuple(next_pos)] == '#':
            direction = turn_right(direction)
        else:
            pos = next_pos

            if check_loop:
                visited_el = (next_pos[0], next_pos[1], direction[0], direction[1])
                if visited_el in visited_with_direction:
                    return True
                visited_with_direction.add(visited_el)
            else:
                visited_positions.add(tuple(next_pos))

    return visited_positions if not check_loop else False

with open('input.txt') as f:
    data = np.array([list(line.strip()) for line in f])

start_pos = np.argwhere(data == '^')[0]
direction = (-1, 0)
visited = walk(start_pos, direction, data, False)
print(len(visited) + 1)
part2 = 0
for pos in visited:
    temp = data.copy()
    temp[pos] = '#'
    if walk(start_pos, direction, temp, True):
        part2 += 1
print(part2)