def make_set(range_str):
    span = range_str.split("-")
    list = range(int(span[0]), int(span[1])+1)
    return(set(list))

def is_contained(set_1, set_2):
    if set_1.issubset(set_2) or set_2.issubset(set_1) :
        return True
    else:
        return False

def is_overlap(set_1, set_2):
    if len(set_1 & set_2) > 0:
        return True
    else:
        return False

with open("inputs/day_4_input.txt", "r") as file:
    lines = file.read().splitlines()

contains = []
overlaps = []
for line in lines:
    pair = line.split(",")
    sets = [make_set(range) for range in pair]
    contains.append(is_contained(sets[0], sets[1]))
    overlaps.append(is_overlap(sets[0], sets[1]))

print(f"Number of complete overlaps (part 1): {sum(contains)}")
print(f"Number of partial overlaps (part 2): {sum(overlaps)}")
