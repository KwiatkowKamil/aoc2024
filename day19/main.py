from functools import cache
with open('input.txt') as f:
    towels_tmp, designs_tmp = f.read().split('\n\n')
    towels = towels_tmp.split(', ')
    designs = designs_tmp.split('\n')


@cache
def checkDesign(pattern):
    checks = []
    if not pattern:
        return True
    for i in range(1, len(pattern)+1):
        if pattern[:i] in towels:
            checks.append(checkDesign(pattern[i:]))
    return sum(checks)


part1 = 0
part2 = 0
for design in designs:
    result = checkDesign(design)
    part1 += bool(result)
    part2 += result

print(part1)
print(part2)