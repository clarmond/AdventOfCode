#!/usr/bin/env python3
import re

data = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

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
