#part 1
with open("day_1_input.txt") as file:
    cals = []
    elf_sums = []
    for line in file.readlines():
        if line != "\n":
            cal = int(line)
            cals.append(cal)
        else:
            elf_sums.append(sum(cals))
            cals = []

highest = max(elf_sums)
print(f"Highest sum of calories carried: {highest}")

#part 2
elf_sort = sorted(elf_sums, reverse=True)
top_three = sum(elf_sort[:3])
print(f"Highest sum of calories by top three elves: {top_three}")
