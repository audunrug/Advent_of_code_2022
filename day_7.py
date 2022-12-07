with open("day_7_input.txt", "r") as file:
    lines = file.read().splitlines()

file_tree = {}
dir_sizes = {}
levels = [1]

dir_size = 0
current_dir = "root"
last_dir = ""
for line in lines[1:]:
    inputs = line.split(" ")
    if inputs[0] == "$" and inputs[1] == "cd":
        if current_dir not in dir_sizes:
            dir_sizes[current_dir] = dir_size
        if inputs[2] != "..":
            last_dir = current_dir
            current_dir = last_dir + "/" + inputs[2]
            if current_dir not in file_tree:
                file_tree[current_dir] = last_dir
            levels.append(levels[-1]+1)
        else:
            current_dir = file_tree[current_dir]
            levels.append(levels[-1]-1)
        dir_size = 0
    elif inputs[0].isnumeric():
        dir_size += int(inputs[0])
dir_sizes[current_dir] = dir_size # to include size of last dict

for level in range(max(levels), 0, -1):
    for dir in file_tree:
        if len(dir.split('/')) == level:
            dir_sizes[file_tree[dir]] += dir_sizes[dir]

#part 1
under_100k = 0

#part 2
unused_space = 70000000 - dir_sizes["root"]
delete_size = ""

for size in list(dir_sizes.values()):
    if size <= 100000:
        under_100k += size
    if (size + unused_space) >= 30000000:
        if delete_size == "" or size < delete_size:
            delete_size = size

print(f"total size of directories witha size below 100000: {under_100k}")
print(f"minimum sized directory to delete: {delete_size}")
