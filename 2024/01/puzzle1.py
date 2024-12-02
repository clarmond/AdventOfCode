list1 = []
list2 = []
with open("input1.txt", "r") as file:
    for line in file:
        val1, val2 = line.strip().split("   ")
        list1.append(int(val1))
        list2.append(int(val2))

list1.sort()
list2.sort()

total_dist = 0
for i in range(len(list1)):
    val1 = list1[i]
    val2 = list2[i]
    dist = abs(val1 - val2)
    total_dist = total_dist + dist

print(f"Total distance is {total_dist}")
