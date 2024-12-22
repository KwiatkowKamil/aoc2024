import numpy as np
from collections import deque
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(start, end, arr, n):
    q = deque()
    q.append((start, 0))
    visited = np.full(arr.shape, fill_value=False)
    visited[start] = True
    rows, cols = arr.shape
    while q:
        pos, distance = q.popleft()
        if pos == end:
            return distance
        for dx, dy in dirs:
            next_pos = pos[0] + dx, pos[1] + dy
            if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols and arr[next_pos] >= n and not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, distance + 1))

with open('input.txt') as f:
    bytes = np.array([[int(x) for x in line.strip().split(',')] for line in f.readlines()])

size = 70
n = 1024
arr = np.full((size+1, size+1), len(bytes)+1, dtype=int)

for i, (y, x) in enumerate(bytes):
    arr[x, y] = i


print(bfs((0, 0), (size, size), arr, n))

left = n
right = len(bytes)

while left < right:
    mid = (left + right) // 2
    if not bfs((0, 0), (size, size), arr, mid):
        right = mid
    else:
        left = mid + 1

print(str(bytes[mid - 1][0]) + ',' + str(bytes[mid - 1][1]))