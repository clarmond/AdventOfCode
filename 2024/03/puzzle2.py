#!/usr/bin/env python3
import re

with open("input1.txt", "r") as file:
    data = file.read()

line = re.sub(r"\n", "", data)
print(line)

total = 0
pattern = r"don't\(\).*?do\(\)"
new_line = re.sub(pattern, "", line)
pattern = r"don't\(\).*?$"
new_line = re.sub(pattern, "", new_line)
pattern = r"mul\(\d+,\d+\)"
results = re.findall(pattern, new_line)
for match in results:
    pattern = r"(\d+),(\d+)"
    results = re.findall(pattern, match)
    x, y = results[0]
    product = int(x) * int(y)
    total += product

print(f"Total is {total}")
