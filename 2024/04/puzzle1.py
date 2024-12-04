#!/usr/bin/env python3

with open("input.txt", "r") as file:
    data = file.read()

rows = []
for line in data.split("\n"):
    if len(line) < 1:
        continue
    line_length = len(line)
    elements = []
    for col in range(line_length):
        chr = line[col:col+1]
        elements.append(chr)
    rows.append(elements)

num_rows = len(rows)

# Find horizontal
horiz = 0
for row in rows:
    row_length = len(row)
    for c in range(row_length):
        check_word = ""
        for i in range(c, row_length):
            check_word += row[i]
        if check_word[0:4] == "XMAS":
            horiz += 1
        if check_word[0:4] == "SAMX":
            horiz += 1

# Find vertical
vert = 0
for c in range(line_length):
    for r in range(num_rows):
        check_word = ""
        for i in range(r, num_rows):
            check_word += rows[i][c]
        if check_word[0:4] == "XMAS":
            vert += 1
        if check_word[0:4] == "SAMX":
            vert += 1

# Find diagonally
diag = 0
for r in range(num_rows):
    check_word = ""
    for c in range(line_length):
        chr1 = ""
        chr2 = ""
        chr3 = ""
        chr4 = ""
        try:
            chr1 = rows[r][c]
            chr2 = rows[r+1][c+1]
            chr3 = rows[r+2][c+2]
            chr4 = rows[r+3][c+3]
        except:
            pass
        check_word = chr1 + chr2 + chr3 + chr4
        if check_word == "XMAS":
            diag += 1
        if check_word == "SAMX":
            diag += 1
        chr1 = ""
        chr2 = ""
        chr3 = ""
        chr4 = ""
        try:
            chr1 = rows[r][c]
            if c - 1 >= 0:
                chr2 = rows[r+1][c-1]
            if c - 2 >= 0:
                chr3 = rows[r+2][c-2]
            if c - 3 >= 0:
                chr4 = rows[r+3][c-3]
        except:
            pass
        check_word = chr1 + chr2 + chr3 + chr4
        if check_word == "XMAS":
            diag += 1
        if check_word == "SAMX":
            diag += 1

total = horiz + vert + diag
print(f"Horizontal:  {horiz}")
print(f"Vertical:    {vert}")
print(f"Diagonal:    {diag}")
print(f"Total:      {total}")
