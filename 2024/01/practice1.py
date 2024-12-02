list1 = [3, 4, 2, 1, 3, 3]
list2 = [4, 3, 5, 3, 9, 3]

list1.sort()
list2.sort()

total_dist = 0
for i in range(len(list1)):
    val1 = list1[i]
    val2 = list2[i]
    dist = abs(val1 - val2)
    total_dist = total_dist + dist

print(f"Total distance is {total_dist}")
assert total_dist == 11, "Should be 11"
