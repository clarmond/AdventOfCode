list1 = [3, 4, 2, 1, 3, 3]
list2 = [4, 3, 5, 3, 9, 3]

freq = {}
for i in range(len(list2)):
    val = list2[i]
    if val in freq:
        freq[val] += 1
    else:
        freq[val] = 1

total_score = 0
for i in range(len(list1)):
    val = list1[i]
    score = 0
    if val in freq:
        score = val * freq[val]
    total_score += score

print(f"Total score is {total_score}")
assert total_score == 31
