from functools import cache

with open('input.txt') as f:
    data = f.read().split()


@cache
def countStones(value, _blinks):
    if _blinks == 0:
        return 1
    if value == '0':
        return countStones('1', _blinks - 1)
    elif value == '1':
        return countStones('2024', _blinks - 1)
    elif len(value) % 2 == 0:
        first_half = value[:len(value) // 2]
        second_half = value[len(value) // 2:]
        return countStones(first_half, _blinks - 1) + countStones(second_half.lstrip("0") or "0", _blinks - 1)
    else:
        return countStones(str(int(value) * 2024), _blinks - 1)


part1 = 0
part2 = 0
for number in data:
    part1 += countStones(number, 25)
    part2 += countStones(number, 75)

print(part1, part2)
