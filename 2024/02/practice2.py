#!/usr/bin/env python3
data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def is_safe(values):
    inc = False
    dec = False
    for i in range(len(values) - 1):
        val1 = int(values[i])
        val2 = int(values[i+1])
        if (val2 - val1 > 0):
            inc = True
        if (val2 - val1 < 0):
            dec = True
        if (abs(val1 - val2) > 3) or (val1 - val2 == 0):
            return False
    if (inc ^ dec):
        return True
    return False


safe_count = 0
for line in data.split("\n"):
    if len(line) > 1:
        values = line.split(" ")
        if is_safe(values):
            safe_count += 1
        else:
            for i in range(len(values)):
                new_list = values.copy()
                new_list.pop(i)
                if is_safe(new_list):
                    safe_count += 1
                    break

print(f"Safe Count is {safe_count}")
