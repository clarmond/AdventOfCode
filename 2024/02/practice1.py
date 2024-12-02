data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

safe_count = 0
for line in data.split("\n"):
    if len(line) > 1:
        values = line.split(" ")
        safe = True
        for i in range(len(values) - 1):
            val1 = int(values[i])
            val2 = int(values[i+1])
            if (abs(val1 - val2) > 2):
                safe = False
                break
        if safe:
            safe_count += 1

print(f"Safe Count is {safe_count}")
