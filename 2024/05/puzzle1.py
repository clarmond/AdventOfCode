#!/usr/bin/env python3

with open("input1.txt", "r") as file:
    page_ordering_rules = file.read()

with open("input2.txt", "r") as file:
    pages_to_produce = file.read()


order = {}
for line in page_ordering_rules.split("\n"):
    if len(line) < 1:
        continue
    key, val = line.split("|")
    if key not in order:
        order[key] = []
    order[key].append(val)

total = 0
for line in pages_to_produce.split("\n"):
    if len(line) < 1:
        continue
    is_valid = True
    pages = line.split(",")
    for i in range(len(pages)):
        if pages[i] in order:
            rules = order[pages[i]]
        else:
            rules = []
        for j in range(i):
            curr_page = pages[j]
            if curr_page in rules:
                is_valid = False
                break
        if is_valid == False:
            break
    if is_valid:
        middle = int(len(pages) / 2)
        total += int(pages[middle])

print(f"Total is {total}")
