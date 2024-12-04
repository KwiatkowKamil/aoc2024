import numpy as np

with open('input.txt') as f:
    data = [list(line.strip()) for line in f.readlines()]
array = np.array(data)
padded = np.pad(array, 1, mode='constant', constant_values='.')
part1 = 0
coords_of_X = np.argwhere(padded == 'X')
vectors = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]
def findWord(_coord, _vector, word):
    for i in range(len(word)):
        _coord += _vector
        if padded[tuple(_coord)] != word[i]:
            return False
    return True


for coord in coords_of_X:
    for vector in vectors:
        part1 += findWord(coord.copy(), vector, 'MAS')

print(part1)

coords_of_A = np.argwhere(padded == 'A')
part2 = 0

for coord in coords_of_A:
    pair = 0
    for axis in [(-1, -1), (1, -1)]:
        if sorted([padded[tuple(coord + axis)], padded[tuple(coord - axis)]]) == ['M', 'S']:
            pair += 1
    if pair == 2:
        part2 += 1
print(part2)