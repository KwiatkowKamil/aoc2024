def getResult(a):
    output = []
    while a > 0:
        b = a % 8
        b = b ^ 1
        b = b ^ a // (2 ** b)
        a = a // 8
        b = b ^ 6
        output.append(b % 8)
    return output


def findRegisterA(program, a, pointer):
    if pointer == len(program):
        return a
    for i in range(8):
        result = getResult(a * 8 + i)
        if result and result[0] == program[pointer]:
            nextA = findRegisterA(program, a * 8 + i, pointer + 1)
            if nextA:
                return nextA


program = [2, 4, 1, 1, 7, 5, 4, 0, 0, 3, 1, 6, 5, 5, 3, 0]

print(findRegisterA(program[::-1], 0, 0))
