with open('input.txt') as f:
    equations = [[int(a), [int(x) for x in b.strip().split()]] for a, b in [line.strip().split(':') for line in f.readlines()]]


def checkResult(result, numbers, concat=False):
    if len(numbers) == 1:
        return result == numbers[0]
    number = numbers.pop()
    options = []
    if concat:
        if str(result).endswith(str(number)) and result != number:
            options.append(checkResult(int(str(result)[:-len(str(number))]), numbers[:], concat))
    if result % number == 0:
        options.append(checkResult(int(result / number), numbers[:], concat))
    if result > number:
        options.append(checkResult(result - number, numbers[:], concat))
    return any(options)

part1 = 0
part2 = 0
for result, numbers in equations:
    if checkResult(result, numbers.copy()):
        part1 += result
    if checkResult(result, numbers.copy(), True):
        part2 += result
print(part1, part2)
