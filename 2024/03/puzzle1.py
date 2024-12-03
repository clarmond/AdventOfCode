#!/usr/bin/env python3
import re

with open("input1.txt", "r") as file:
    data = file.read()

total = 0
for line in data.split("\n"):
    if len(line) > 1:
        pattern = r"mul\(\d+,\d+\)"
        results = re.findall(pattern, line)
        for match in results:
            pattern = r"(\d+),(\d+)"
            results = re.findall(pattern, match)
            x, y = results[0]
            product = int(x) * int(y)
            total += product

print(f"Total is {total}")
