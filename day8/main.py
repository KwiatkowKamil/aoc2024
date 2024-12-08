import numpy as np
from itertools import combinations


def get_line_points(P0, P1, t_values):
    x0, y0 = P0
    x1, y1 = P1
    points = []
    for m in t_values:
        x = x0 + m * (x1 - x0)
        y = y0 + m * (y1 - y0)
        points.append((x, y))
    return points


def is_within_bounds(pos, arr):
    return 0 <= pos[0] < arr.shape[0] and 0 <= pos[1] < arr.shape[1]


def count_nodes(_antennas, points, _data):
    for antenna_type in _antennas:
        for p1, p2 in combinations(antenna_type, 2):
            for x, y in get_line_points(p1, p2, points):
                if int(x) == x and int(y) == y and is_within_bounds((x, y), _data):
                    _data[(int(x), int(y))] = '#'
    return len(np.argwhere(_data == '#'))


with open('input.txt') as f:
    data = np.array([list(line.strip()) for line in f])

unique_el_list = np.unique(data)
antennas = [np.argwhere(data == x) for x in unique_el_list if x != '.']

halfway_points = [2 / 3, 2, 1 / 3, -1]
all_points = [i for i in range(-38, 38)]

print(count_nodes(antennas, halfway_points, data.copy()))
print(count_nodes(antennas, all_points, data.copy()))
