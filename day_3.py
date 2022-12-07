import re

priorities = {}
n = 1
for letter in "abcdefghijklmnopqrstuvwxyz":
    priorities[letter] = n
    priorities[letter.upper()] = n + 26
    n += 1

with open("inputs/day_3_input.txt", "r") as file:
    lines = file.read().splitlines()

#part 1
values = []
for line in lines:
    half = int(len(line)/2)
    exp = "[" + line[0:half] + "]"
    match = re.search(exp, line[half:len(line)])
    item = match.group()
    values.append(priorities[item])

#part 2
group_values = []
for i in range(0, len(lines), 3):
    s1, s2, s3 = set(lines[i]), set(lines[i+1]), set(lines[i+2])
    shared = (s1 & s2 & s3).pop()
    group_values.append(priorities[shared])

print(f"Sum of shared item values (part 1): {sum(values)}")
print(f"Sum of group item values (part 2): {sum(group_values)}")
