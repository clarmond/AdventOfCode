#!/usr/bin/env python3

data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

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

found = 0
for r in range(num_rows):
    for c in range(line_length):
        pos1 = ""
        pos2 = ""
        pos3 = ""
        pos4 = ""
        pos5 = ""
        try:
            pos1 = rows[r][c]
            pos2 = rows[r][c+2]
            pos3 = rows[r+1][c+1]
            pos4 = rows[r+2][c]
            pos5 = rows[r+2][c+2]
        except:
            pass
        if pos1 == "M" and pos2 == "S" and pos3 == "A" and pos4 == "M" and pos5 == "S":
            found += 1
        if pos1 == "S" and pos2 == "M" and pos3 == "A" and pos4 == "S" and pos5 == "M":
            found += 1
        if pos1 == "M" and pos2 == "M" and pos3 == "A" and pos4 == "S" and pos5 == "S":
            found += 1
        if pos1 == "S" and pos2 == "S" and pos3 == "A" and pos4 == "M" and pos5 == "M":
            found += 1

print(f"Found: {found}")
