import numpy as np

with open('input.txt') as f:
    data = np.array([list(line.strip()) for line in f])

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
start_pos = np.argwhere(data == 'S')[0]
start_dir = (0, 1)


def rot_dist(d1, d2):
    if d1 == (-d2[0], -d2[1]):
        return 2
    elif d1 == d2:
        return 0
    else:
        return 1
best_score = {}
best_final_score = float('inf')
best_tiles = set()
def checkNext(pos, dir, score, visited):
    global best_final_score
    global best_tiles
    tmp_dirs = [d for d in dirs if abs(d[0]) != abs(dir[0])]
    if tuple(pos) not in best_score:
        best_score[tuple(pos)] = score
    else:
        if score <= best_score[tuple(pos)]:
            best_score[tuple(pos)] = score
        else:
            return
    while True:
        next_pos = pos + dir
        if tuple(pos) in visited:
            break
        else:
            visited.add(tuple(pos))
        next_tile = data[tuple(next_pos)]
        if next_tile == '.':
            pos = next_pos
        for next_dir in tmp_dirs:
            if data[tuple(next_pos + next_dir)] == '.':
                checkNext(next_pos, next_dir, score + rot_dist(dir, next_dir), visited.copy())
        if next_tile == '#':
            break
        if next_tile == 'E':
            visited.add(tuple(next_pos))
            final_score = score * 1000 + len(visited)
            if final_score < best_final_score:
                best_final_score = final_score
                best_tiles = visited
            elif final_score == best_final_score:
                best_tiles.update(visited)

for dir in dirs:
    if data[tuple(start_pos + dir)] == '.':
        checkNext(start_pos, dir, rot_dist(start_dir, dir), set())

print(best_final_score - 1)
print(len(best_tiles))