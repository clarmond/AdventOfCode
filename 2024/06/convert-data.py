with open("input1.txt", "r") as file:
    data = file.read()

html = ""
row = 0
for line in data.split("\n"):
    if len(line) < 1:
        continue
    html += f"<tr id='row>{row}'>\n"
    for i in range(len(line)):
        html += f"\t<td id='r{row}c{i}'>" + line[i:i+1] + "</td>\n"
    html += "</tr>\n"
    row += 1

print(html)
