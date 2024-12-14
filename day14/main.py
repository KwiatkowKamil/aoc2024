import numpy as np
import re
import matplotlib.pyplot as plt

seconds = 100
room_size = np.array([101, 103])
midpoints = room_size // 2

with open('input.txt') as f:
    matches = re.findall(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)', f.read())

positions = np.array([[int(x), int(y)] for x, y, _, _ in matches])
velocities = np.array([[int(vx), int(vy)] for _, _, vx, vy in matches])

new_positions = (positions + velocities * seconds) % room_size

quadrants = [
    np.sum((new_positions[:, 0] < midpoints[0]) & (new_positions[:, 1] < midpoints[1])),
    np.sum((new_positions[:, 0] < midpoints[0]) & (new_positions[:, 1] > midpoints[1])),
    np.sum((new_positions[:, 0] > midpoints[0]) & (new_positions[:, 1] < midpoints[1])),
    np.sum((new_positions[:, 0] > midpoints[0]) & (new_positions[:, 1] > midpoints[1]))
]

print(np.prod(quadrants))

seconds_2 = 10000

min_second = min(([np.std((positions + velocities * s) % room_size), s] for s in range(1, seconds_2 + 1)), key=lambda x:x[0])[1]
print(min_second)
# display the frame, for fun
min_positions = (positions + velocities * min_second) % room_size
plt.figure(figsize=(8, 8))
plt.scatter(min_positions[:, 0], min_positions[:, 1], c='green')
plt.xlim(0, room_size[0])
plt.ylim(0, room_size[1])
plt.gca().invert_yaxis()
plt.show()