import ast

def is_int(val):
    try:
        v = int(val)
        return True
    except TypeError:
        return False

def as_list(val):
    if isinstance(val, int):
        return [val]
    else:
        return val

def evaluate_lists(l, r):
    #print(f"l: {l}")
    #print(f"r: {r}")
    if len(l) == 0 and len(r) != 0:
        return True
    elif len(l) != 0 and len(r) == 0:
        return False
    else:
        for i in range(len(l)):
            try:
                if is_int(l[i]) and is_int(r[i]):
                    if l[i] > r[i]:
                        return False
                    elif l[i] < r[i]:
                        return True
                    elif i == len(l)-1 and i < len(r)-1:
                        return True
                elif isinstance(l[i], list) or isinstance(r[i], list):
                    if as_list(l[i]) == as_list(r[i]):
                        if i == len(l)-1 and i < len(r)-1:
                            return True
                        else:
                            pass
                    elif evaluate_lists(as_list(l[i]), as_list(r[i])) == None:
                        pass
                    else:
                        return evaluate_lists(as_list(l[i]), as_list(r[i]))

            except IndexError:
                if i > len(r)-1:
                    return False

with open("inputs/day_13_input.txt", "r") as file:
    lines = file.read().splitlines()

#part 1
indices = []
for i in range(0, len(lines)-1, 3):
    #print(i)
    l, r = ast.literal_eval(lines[i]), ast.literal_eval(lines[i+1])
    if evaluate_lists(l, r):
        indices.append((i/3 +1))
    print(f"index: {i/3 +1}: {evaluate_lists(l, r)}")

print(sum(indices))


#part 2
lines_all = [line for line in lines if line != ""]
lines_all.append('[[2]]')
lines_all.append('[[6]]')
order = [ast.literal_eval(lines_all[0])]
for i in range(1, len(lines_all)):
    l = ast.literal_eval(lines_all[i])
    for n in range(len(order)):
        if evaluate_lists(l, order[n]):
            order.insert(n, l)
            break
        elif not evaluate_lists(l, order[n]) and n == len(order)-1:
            order.append(l)

for n in range(0, len(order)-1, 2):
    #print(evaluate_lists(order[n], order[n+1]))
    print(order[n])
    print(order[n+1])
    #print(evaluate_lists(order[n], order[n+1]))
    #print("")
print(order.index([[2]]))
print(order.index([[6]]))
print(order.index([[2]])*order.index([[6]]))
print(len(order))
#    print(ord)
