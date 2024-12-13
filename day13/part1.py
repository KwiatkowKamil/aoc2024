import re

with open('input.txt') as f:
    no_labels = re.sub(r'Button A: |Button B: |Prize: |[XY][+=]', '', f.read())
    data = [[[int(n) for n in x.split(", ")] for x in line.split("\n")] for line in no_labels.split("\n\n")]

a_button_cost = 3
b_button_cost = 1


def checkCost(a_button, b_button, prize):
    a_times = (b_button[1] * prize[0] - b_button[0] * prize[1]) / (b_button[1] * a_button[0] - b_button[0] * a_button[1])
    b_times = (prize[0] - a_button[0] * a_times) / b_button[0]
    if a_times == int(a_times) and b_times == int(b_times):
        return a_times * a_button_cost + b_times * b_button_cost
    return 0

part1 = 0
part2 = 0
for a, b, prize in data:
    part1 += checkCost(a, b, prize)

for a, b, prize in data:
    part2 += checkCost(a, b, [prize[0] + 10000000000000, prize[1] + 10000000000000])

print(int(part1), int(part2))
