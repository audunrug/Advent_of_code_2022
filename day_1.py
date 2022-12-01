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

print(f"Highest sum of calories carried: {max(elf_sums)}")

#part 2
elf_sort = sorted(elf_sums, reverse=True)
print(f"Highest sum of calories by top three elves: {sum(elf_sort[:3])}")
