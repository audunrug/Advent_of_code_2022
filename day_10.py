with open("inputs/day_10_input.txt", "r") as file:
    lines = file.read().splitlines()

signals, x, c = [], 1, 0 # part 1
screen, row, marker = ["" for i in range(19, 220, 40)], 0, [0,1,2] # part 2
for line in lines:
    if line == "noop":
        c += 1
        signals.append(x*c) #p1
        if c%40 in marker and row < 6: #p2
            screen[row] = screen[row] + "#"
        elif row < 6:
            screen[row] = screen[row] + "."
        if c % 40 == 0:
            row += 1
    else:
        for i in [0,1]:
            c += 1
            if c % 40 == 0:
                row += 1
            signals.append(x*(c)) #p1
            if c%40 in marker and row < 6: #p2
                screen[row] = screen[row] + "#"
            elif row < 6:
                screen[row] = screen[row] + "."

        x += int(line.split(" ")[1])
        marker = list(range(x, x+3))


print(sum([signals[i] for i in range(19, 220, 40)])) #p1
for row in screen: #p2
    print(row)
