with open('input.txt') as f:
    lists = list(zip(*[map(int, line.split()) for line in f]))

print(sum(abs(a-b) for a, b in zip(*map(sorted, lists))))
print(sum(x * lists[1].count(x) for x in lists[0]))