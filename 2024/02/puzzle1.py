#!/usr/bin/env python3
with open("input1.txt", "r") as file:
    data = file.read()

safe_count = 0
for line in data.split("\n"):
    if len(line) > 1:
        values = line.split(" ")
        safe = True
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
                safe = False
        if (inc ^ dec) and (safe):
            print(f"Safe - {line}")
            safe_count += 1
        else:
            print(f"Not Safe - {line}")
            if (inc and dec):
                print("> increasing and decreasing")
            if (safe == False):
                print("> jumps")

print(f"Safe Count is {safe_count}")
