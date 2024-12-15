import numpy as np


dirs = {
    '^': (-1, 0),
    '>': (0,  1),
    'v': (1, 0),
    '<': (0, -1),
}

with open('input.txt') as f:
    warehouse_tmp, movements_tmp = f.read().split("\n\n")
    warehouse = np.array([list(line) for line in warehouse_tmp.split('\n')])
    movements = list(map(lambda x: dirs[x], movements_tmp.replace('\n', '')))


pos = np.argwhere(warehouse == '@')[0]

for movement in movements:
    next_pos = pos + movement
    next_block = warehouse[tuple(next_pos)]
    if next_block == '#':
        continue
    elif next_block == '.':
        warehouse[tuple(pos)] = '.'
        warehouse[tuple(next_pos)] = '@'
        pos = next_pos
    elif next_block == 'O':
        visited_pos = [tuple(pos), tuple(next_pos)]
        check_pos = next_pos.copy()
        while True:
            check_pos += movement
            visited_pos.append(tuple(check_pos))
            check_block = warehouse[tuple(check_pos)]
            if check_block == '.':
                for a, b in reversed(list(zip(visited_pos, visited_pos[1:]))):
                    temp = warehouse[a]
                    warehouse[a] = warehouse[b]
                    warehouse[b] = temp
                pos = next_pos
                break
            if check_block == 'O':
                continue
            if check_block == '#':
                break

boxes = np.argwhere(warehouse == 'O') * (100, 1)

print(sum(sum(boxes)))