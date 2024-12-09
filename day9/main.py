with open('input.txt') as f:
    data = [int(x) for x in f.read()]

spaces = data[1::2]
files = data[::2]

position = 0
checksum = 0
i = 0
index = len(files) - 1
while files and spaces:
    if i % 2 == 0:
        for j in range(data[i]):
            if files:
                if files[0] > 0:
                    checksum += position * (i // 2)
                    files[0] -= 1
                    position += 1
                if files[0] == 0:
                    del files[0]
    else:
        for j in range(data[i]):
            files[-1] -= 1
            spaces[0] -= 1
            checksum += position * index
            position += 1
            if files[-1] == 0:
                del files[-1]
                index -= 1
            if spaces[0] == 0:
                del spaces[0]
    i += 1
print(checksum)
def get_int_range_sum(a, b):
    return (b - a + 1) * (a + b) / 2


spaces = data[1::2]
p_spaces = data[1::2]
files = data[::2]
moved = [False] * len(files)
checksum = 0
for i, file in reversed(list(enumerate(files))):
    for j, space in enumerate(spaces[:i]):
        if file <= space:
            position = sum(data[:((j*2)+1)]) + p_spaces[j] - spaces[j]
            checksum += get_int_range_sum(position, position + file - 1) * i
            spaces[j] = space - file
            moved[i] = True
            break
        else:
            continue
for i in range(len(files)):
    if not moved[i]:
        position = sum(data[:i*2])
        checksum += get_int_range_sum(position, position + files[i] - 1) * i

print(checksum)