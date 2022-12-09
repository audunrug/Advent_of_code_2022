import numpy as np

class knot():
    """Input chords must be a double list [[],[]] """
    def __init__(self, input_coords, length):
        self.pos = [input_coords for l in range(length)]
        self.tail_log = [self.pos[-1]]

    #update internal head position
    def move_head(self, dir):
        p = self.pos[0].copy()
        if dir == "R":
            p[1] += 1
        elif dir == "L":
            p[1] -= 1
        elif dir == "D":
            p[0] += 1
        elif dir == "U":
            p[0] -= 1
        self.pos[0] = p

    #update internal tail position
    def move_tails(self):
        for i in range(1, len(self.pos)):
            h = self.pos[i-1].copy()
            t = self.pos[i].copy()
            if abs(h[0] - t[0]) and abs(h[1] - t[1]) == 2:
                if h[0] > t[0]:
                    t[0] += 1
                elif h[0] < t[0]:
                    t[0] -= 1
                if h[1] > t[1]:
                    t[1] += 1
                elif h[1] < t[1]:
                    t[1] -= 1
            elif (h[0] - t[0]) > 1:
                t = h.copy()
                t[0] -= 1
            elif (h[0] - t[0]) < -1:
                t = h.copy()
                t[0] += 1
            elif (h[1] - t[1]) > 1:
                t = h.copy()
                t[1] -= 1
            elif (h[1] - t[1]) < -1:
                t = h.copy()
                t[1] += 1
            self.pos[i] = t.copy()

    #move knot according to input
    def move_both(self, input_move):
        dir = input_move.split(" ")[0]
        steps = int(input_move.split(" ")[1])
        for step in range(steps):
            self.move_head(dir)
            self.move_tails()
            if self.pos[-1] not in self.tail_log:
                self.tail_log.append(self.pos[-1])

    #quick and dirty visualization (which loops around)
    def print_pos(self):
        dim = len(self.pos)
        matrix = np.zeros((dim, dim), dtype=object)
        matrix[:,:] = "."
        for pos in range(len(self.pos)-1, -1, -1):
            r, c = self.pos[pos][0] % dim, self.pos[pos][1] % dim
            if pos == 0:
                matrix[r,c] = "H"
            else:
                matrix[r,c] = str(pos)
        print(matrix)
        print("")

with open("inputs/day_9_input.txt", "r") as file:
    moves = file.read().splitlines()

#test = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]
p1_knot = knot([0,0],2)
p2_knot = knot([0,0],10)
for move in moves: #test:
    p1_knot.move_both(move)
    p2_knot.move_both(move)
    #visualize
    print(move)
    p2_knot.print_pos()

#part 1
print(len(p1_knot.tail_log))
#part 2
print(len(p2_knot.tail_log))
