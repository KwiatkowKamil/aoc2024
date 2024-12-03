import re

print(sum(int(m.group(1)) * int(m.group(2)) for m in re.finditer(r"mul\((\d+),(\d+)\)", open('input.txt').read())))

print(sum(
    int(m.group(3)) * int(m.group(4))
    for m in re.finditer(r"(don\'t\(\))|(do\(\))|mul\((\d+),(\d+)\)", open('input.txt').read())
    if (enabled := False if m.group(1) else True if m.group(2) else enabled)
    and m.group(3)
))
