#!/usr/bin/env python3

with open("input1.txt", "r") as file:
    data = file.read()

x = -1
y = -1
direction = "up"
done = False
last_row = 0
last_col = 0
visited = {}


def move_guard():
    global x
    global y
    global direction
    if direction == "up":
        y -= 1
    elif direction == "down":
        y += 1
    elif direction == "right":
        x += 1
    elif direction == "left":
        x -= 1
    if x < 0 or x > last_col:
        return True
    if y < 0 or y > last_row:
        return True
    spot = rows[y][x]
    if spot == "#":
        if direction == "up":
            direction = "right"
            y += 1
            x += 1
        elif direction == "down":
            direction = "left"
            y -= 1
            x -= 1
        elif direction == "right":
            direction = "down"
            x -= 1
            y += 1
        elif direction == "left":
            direction = "up"
            x += 1
            y -= 1
    if rows[y][x] == "#":
        move_guard()
        return False
    if x < 0 or x > last_col:
        return True
    if y < 0 or y > last_row:
        return True
    visited[f"{x},{y}"] = True
    rows[y][x] = "X"
    return False


rows = []
for line in data.split("\n"):
    if len(line) > 1:
        rows.append(list(line))
        index = line.find("^")
        last_col = len(line) - 1
        if index > -1:
            x = index
            y = len(rows) - 1
            visited[f"{x},{y}"] = True
last_row = len(rows) - 1

while not done:
    done = move_guard()

print(len(visited))
