#!/usr/bin/env python3

page_ordering_rules = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
"""

pages_to_produce = """
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

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
