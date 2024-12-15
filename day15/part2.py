import numpy as np
import sys
dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

def swap_tiles(a, b):
    temp = warehouse[tuple(a)]
    warehouse[tuple(a)] = warehouse[tuple(b)]
    warehouse[tuple(b)] = temp


class Box:
    def __init__(self, left_pos):
        self.left_pos = left_pos
        self.right_pos = left_pos + (0, 1)

    def move(self, direction, check = True):
        next_left = self.left_pos + direction
        next_right = self.right_pos + direction
        tile_left = warehouse[tuple(next_left)]
        tile_right = warehouse[tuple(next_right)]
        if direction == (0, 1):
            if tile_right == '.' or (isinstance(tile_right, Box) and tile_right.move(direction, False)):
                if not check:
                    self.performMove(direction)
                return True
            if tile_right == '#' or (isinstance(tile_right, Box) and not tile_right.move(direction, False)):
                return False
        if direction == (0, -1):
            if tile_left == '.' or (isinstance(tile_left, Box) and tile_left.move(direction, False)):
                if not check:
                    self.performMove(direction)
                return True
            if tile_left == '#' or (isinstance(tile_left, Box) and not tile_left.move(direction, False)):
                return False
        else:
            if tile_left == '.' and tile_right == '.':
                if not check:
                    self.performMove(direction)
                return True
            if tile_left == '#' or tile_right == '#':
                return False
            if isinstance(tile_left, Box) and isinstance(tile_right, Box) and tile_left != tile_right:
                if tile_left.move(direction) and tile_right.move(direction):
                    if not check:
                        tile_left.move(direction, False)
                        tile_right.move(direction, False)
                        self.performMove(direction)
                    return True
            if isinstance(tile_left, Box):
                if tile_left.move(direction) and (tile_right == '.' or tile_left == tile_right):
                    if not check:
                        tile_left.move(direction, False)
                        self.performMove(direction)
                    return True
                return False
            if isinstance(tile_right, Box):
                if tile_right.move(direction) and (tile_left == '.' or tile_right == tile_left):
                    if not check:
                        tile_right.move(direction, False)
                        self.performMove(direction)
                    return True
                return False
    def performMove(self, direction):
        if direction == (0, -1):
            swap_tiles(self.left_pos, self.left_pos + direction)
            swap_tiles(self.right_pos, self.right_pos + direction)
        else:
            swap_tiles(self.right_pos, self.right_pos + direction)
            swap_tiles(self.left_pos, self.left_pos + direction)
        self.left_pos += direction
        self.right_pos += direction

    def __str__(self):
        return '|'

with open('input.txt') as f:
    warehouse_tmp, movements_tmp = f.read().split("\n\n")
    warehouse_tmp = warehouse_tmp.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    warehouse = np.array([list(line) for line in warehouse_tmp.split('\n')], dtype=object)
    dirs = list(map(lambda x: dirs[x], movements_tmp.replace('\n', '')))

pos = np.argwhere(warehouse == '@')[0]
boxes = np.argwhere(warehouse == '[')
for box in boxes:
    tmp = Box(box)
    warehouse[tuple(box)] = tmp
    warehouse[tuple(box + (0, 1))] = tmp

for index, dir in enumerate(dirs):
    next_pos = pos + dir
    next_block = warehouse[tuple(next_pos)]
    if next_block == '#':
        continue
    elif next_block == '.':
        warehouse[tuple(pos)] = '.'
        warehouse[tuple(next_pos)] = '@'
        pos = next_pos
    elif isinstance(next_block, Box):
        if next_block.move(dir, False):
            warehouse[tuple(pos)] = '.'
            warehouse[tuple(next_pos)] = '@'
            pos = next_pos

result = 0
box_pos_list = np.argwhere(warehouse.astype(str) == '|')
for box_pos in box_pos_list:
    box = warehouse[tuple(box_pos)]
    if isinstance(box, Box) and tuple(box.left_pos) == tuple(box_pos):
        result += box_pos * (100, 1)
print(sum(result))