import numpy as np

class monkey():
    def __init__(self, items, opr_type, opr_val, div, yes_monkey, no_monkey):
        self.items = items
        self.opr_type, self.opr_val = opr_type, opr_val
        self.yes_mon, self.no_mon = yes_monkey, no_monkey
        self.monkeylvl = 0
        self.div = div

    def inspect(self, value):
        self.monkeylvl += 1
        return int(value/3)

    def throw_item(self):
        val = self.items.pop(0)
        if self.opr_type == "*":
            if self.opr_val != "old":
                val *= int(self.opr_val)
            else:
                val *= val
        elif self.opr_type == "+":
            if self.opr_val != "old":
                val += int(self.opr_val)
            else:
                val += val
        if self.inspect(val) % self.div == 0:
            return val, self.yes_mon
        else:
            return val, self.no_mon

    def get_item(self, new_element):
        self.items.append(new_element)

class worse_monkey(monkey):
    def inspect(self, value):
        self.monkeylvl += 1
        return value

    def get_item(self, new_element, monkey_lcm):
        self.items.append(new_element % monkey_lcm)

with open("inputs/day_11_input.txt", "r") as file:
    lines = file.read().splitlines()

p1_monkeys = []
p2_monkeys = []
for i in range(0, len(lines), 7):
    items = [int(e) for e in lines[i+1].split(": ")[1].split(", ")]
    opr, val = lines[i+2].split(" ")[-2], lines[i+2].split(" ")[-1]
    div = int(lines[i+3].split(" ")[-1])
    yes, no = int(lines[i+4].split(" ")[-1]), int(lines[i+5].split(" ")[-1])
    p1_monkeys.append(monkey(items, opr, val, div, yes, no))
    p2_monkeys.append(worse_monkey(items, opr, val, div, yes, no))

#part 1
#p1_monkeys = monkey_list.copy()
for n in range(20):
    for i in range(len(p1_monkeys)):
        for item in p1_monkeys[i].items.copy():

            throw, new = p1_monkeys[i].throw_item()
            p1_monkeys[new].get_item(throw)
            #if n == 1:
                #print(throw, new)
            #print(throw, new)

n_throws = [mnk.monkeylvl for mnk in p1_monkeys]
sort_throws = sorted(n_throws)
print(sort_throws[-1]*sort_throws[-2])
print("")

# p2
monkey_lcm = int(np.prod(np.array([monk.div for monk in p2_monkeys])))
print(np.array([monk.div for monk in p2_monkeys]))
print(monkey_lcm)
for n in range(10000):
    for i in range(len(p2_monkeys)):
        for item in p2_monkeys[i].items.copy():
            throw, new = p2_monkeys[i].throw_item()
            p2_monkeys[new].get_item(throw, monkey_lcm)
            #print(throw, new)

n_throws = [mnk.monkeylvl for mnk in p2_monkeys]
sort_throws = sorted(n_throws)
print(sort_throws[-1]*sort_throws[-2])
