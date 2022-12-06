def split_by_marker(input_str, l):
    segments = []
    last = 0
    for i in range(len(input_str)-l):
        chars = set(input_str[i:i+l])
        if len(chars) == l:
            segments.append(input_str[last:i+l])
            last = i
    return segments

with open("day_6_input.txt", "r") as file:
    full_str = file.read().strip()

part_1 = split_by_marker(full_str, 4)
part_2 = split_by_marker(full_str, 14)

print(f"Length of first segment (4 char marker): {len(part_1[0])}")
print(f"Length of first segment (14 char marker): {len(part_2[0])}")
