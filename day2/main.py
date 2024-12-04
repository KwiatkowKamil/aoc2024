with open('input.txt') as f:
    reports = [[int(x) for x in line.split()] for line in f]
part1 = 0


def is_safe(_level):
    distances = [b - a for a, b in zip(_level, _level[1:])]
    if all(abs(x) < 4 and x != 0 for x in distances) and (
            all(x > 0 for x in distances) or all(x < 0 for x in distances)):
        return True
    return False


for level in reports:
    part1 += is_safe(level)
print(part1)

part2 = 0
for level in reports:
    for i in range(len(level)):
        dampened = level[:i] + level[i + 1:]
        if is_safe(dampened):
            part2 += 1
            break

print(part2)