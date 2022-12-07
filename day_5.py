class stack():
    def __init__(self, input):
        n_stacks = len(input[-1].split("   "))
        stacks = [[] for stack in range(n_stacks)]
        for row in input[:-1]:
            n = 0
            i = 0
            while i < len(row):
                if row[i+1] != " ":
                    stacks[n].append(row[i+1])
                i += 4
                n += 1
        self.stacks = stacks

    def move_single(self, move_str): #part 1
        stacks = self.stacks
        moves = move_str.split(" ")
        n, start, end = int(moves[1]), int(moves[3])-1, int(moves[5])-1
        for i in list(range(n)):
            box = stacks[start].pop(0)
            stacks[end].insert(0, box)
        self.stacks = stacks

    def move_multiple(self, move_str): #part 2
        stacks = self.stacks
        moves = move_str.split(" ")
        n, start, end = int(moves[1]), int(moves[3])-1, int(moves[5])-1
        new_stacks = stacks.copy()
        new_boxes = stacks[start][:n]
        del new_stacks[start][:n]
        new_boxes.extend(new_stacks[end])
        new_stacks[end] = new_boxes
        self.stacks = new_stacks

    def top_boxes(self):
        string = ""
        for stack in self.stacks:
            if len(stack) != 0:
                string += stack[0]
            else:
                string += ":"
        return string


with open("inputs/day_5_input.txt", "r") as file:
    all = file.read().splitlines()
start_config = all[:9]
moves = all[10:]

p1_stack = stack(start_config)
p2_stack = stack(start_config)

for move in moves:
    p1_stack.move_single(move) #part 1
    p2_stack.move_multiple(move) #part 2

print(f"Top boxes (part 1): {p1_stack.top_boxes()}")
print(f"Top boxes (part 2): {p2_stack.top_boxes()}")
