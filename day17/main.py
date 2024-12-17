import re
import math


class Program:
    instruction_pointer = 0

    def __init__(self, registers_, program_, str_program_):
        self.output = ""
        self.registers = registers_
        self.program = program_
        self.str_program = str_program_
        self.instructions = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def get_combo_operand(self, value):
        if value in [0, 1, 2, 3]:
            return value
        if value == 4:
            return self.registers['A']
        if value == 5:
            return self.registers['B']
        if value == 6:
            return self.registers['C']
        if value == 7:
            print('Not a valid program.')

    def adv(self, operand):
        self.registers['A'] = math.trunc(self.registers['A'] // (2 ** self.get_combo_operand(operand)))

    def bxl(self, operand):
        self.registers['B'] = self.registers['B'] ^ operand

    def bst(self, operand):
        self.registers['B'] = self.get_combo_operand(operand) % 8

    def jnz(self, operand):
        if self.registers['A'] == 0:
            return
        self.instruction_pointer = operand - 2

    def bxc(self, operand):
        self.registers['B'] = self.registers['B'] ^ self.registers['C']

    def out(self, operand):
        self.output += str(self.get_combo_operand(operand) % 8) + ','

    def bdv(self, operand):
        self.registers['B'] = math.trunc(self.registers['A'] // (2 ** self.get_combo_operand(operand)))

    def cdv(self, operand):
        self.registers['C'] = math.trunc(self.registers['A'] // (2 ** self.get_combo_operand(operand)))

    def execute(self):
        while self.instruction_pointer < len(self.program):
            instruction = self.program[self.instruction_pointer]
            operand = self.program[self.instruction_pointer+1]
            self.instructions[instruction](operand)
            self.instruction_pointer += 2
        if self.output[:-1] == self.str_program:
            return True
        return False

pattern = (
    r"Register A:\s*(\d+)\s*"
    r"Register B:\s*(\d+)\s*"
    r"Register C:\s*(\d+)\s*"
    r"Program:\s*([\d,]+)"
)

with open('input.txt') as f:
    match = re.search(pattern, f.read())

registers = {
    'A': int(match.group(1)),
    'B': int(match.group(2)),
    'C': int(match.group(3)),
}
str_program = match.group(4)
program = [int(num) for num in match.group(4).split(",")]

p = Program(registers, program, str_program)
p.execute()

print(p.output[:-1])
