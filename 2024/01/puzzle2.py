list1 = []
list2 = []
with open("input1.txt", "r") as file:
    for line in file:
        val1, val2 = line.strip().split("   ")
        list1.append(int(val1))
        list2.append(int(val2))

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
