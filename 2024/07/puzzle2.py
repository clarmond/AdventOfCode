#!/usr/bin/env python3

import itertools
import sys

data_file = sys.argv[1]

with open(data_file, "r") as file:
    data = file.read()


def combos(size):
    results = []
    for i in range(1, size + 1):
        for item in itertools.product(range(3), repeat=i):
            result = "0" * size + "".join(map(str, item))
            results.append(result[-size:])
    return results


grand_total = 0
lines_processed = 0
for line in data.split("\n"):
    lines_processed += 1
    print(f"Processing line {lines_processed}")
    equation = line.split(": ")
    answer = int(equation[0])
    values = equation[1].split(" ")
    operators = combos(len(values) - 1)
    is_valid = False
    for op_string in operators:
        total = int(values[0])
        for i in range(1, len(values)):
            op = op_string[i-1:i]
            if (op == "0"):
                total += int(values[i])
            if (op == "1"):
                total *= int(values[i])
            if (op == "2"):
                total = int(str(total) + str(values[i]))
        if total == answer:
            is_valid = True
            break
    if is_valid:
        grand_total += answer

print(f"Lines processed {lines_processed}")
print(f"Grand total {grand_total}")
