#!/usr/bin/env python3
import re

data = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

line = re.sub(r"\n", "", data)
print(line)

total = 0
pattern = r"don't\(\).*?do\(\)"
new_line = re.sub(pattern, "", line)
print(line)
print(new_line)
pattern = r"mul\(\d+,\d+\)"
results = re.findall(pattern, new_line)
for match in results:
    pattern = r"(\d+),(\d+)"
    results = re.findall(pattern, match)
    x, y = results[0]
    product = int(x) * int(y)
    total += product

print(f"Total is {total}")
