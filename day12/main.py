import numpy as np

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]



def group_adjacent(points):
    points_set = set(points)
    visited = set()

    def dfs(start):
        stack = [start]
        group = []
        visited.add(start)

        while stack:
            current = stack.pop()
            group.append(current)
            for neighbor in (tuple(np.add(current, dir)) for dir in dirs):
                if neighbor in points_set and neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return group

    return [dfs(p) for p in points if p not in visited]
def is_within_bounds(pos, arr):
    return 0 <= pos[0] < arr.shape[0] and 0 <= pos[1] < arr.shape[1]


with open('input.txt') as f:
    data = np.array([[x for x in list(line.strip())] for line in f])

plant_types = np.unique(data)
part1 = 0
part2 = 0
for plant_type in plant_types:
    for group in group_adjacent([tuple(x) for x in np.argwhere(data == plant_type)]):
        area = len(group)
        perimeter = 0
        dir_to_points = {dir: [] for dir in dirs}
        for point in group:
            for dir in dirs:
                tmp = tuple(np.add(point, dir))
                if is_within_bounds(tmp, data):
                    if data[tmp] != plant_type:
                        perimeter += 1
                        dir_to_points[dir].append(point)
                else:
                    dir_to_points[dir].append(point)
                    perimeter += 1
        part1 += area * perimeter
        sides = 0
        for dir in dir_to_points:
            sides += len(group_adjacent(dir_to_points[dir]))
        part2 += area * sides
print(part1, part2)
