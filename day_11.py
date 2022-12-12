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
        val = self.inspect(val)
        if val % self.div == 0:
            return val, self.yes_mon
        else:
            return val, self.no_mon

    def get_item(self, new_element):
        self.items.append(new_element)

#for part 2
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

def get_mnk_business(monkeys, rounds, mnk_lcm=False):
    for n in range(rounds):
        for i in range(len(monkeys)):
            for item in monkeys[i].items.copy():
                throw, new = monkeys[i].throw_item()
                if not mnk_lcm:
                    monkeys[new].get_item(throw)
                else:
                    monkeys[new].get_item(throw, mnk_lcm)
    n_levels = [mnk.monkeylvl for mnk in monkeys]
    sort_levels = sorted(n_levels, reverse=True)
    return sort_levels[0]*sort_levels[1]

#part 1
print(get_mnk_business(p1_monkeys, 20))

#part 2
monkey_lcm = int(np.prod(np.array([monk.div for monk in p2_monkeys])))
print(get_mnk_business(p2_monkeys, 10000, monkey_lcm))
