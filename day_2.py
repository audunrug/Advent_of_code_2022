#For part 1
p1 = {"A" : "rock", "B" : "paper", "C" : "scissor"}
p2 = {"X" : "rock", "Y" : "paper", "Z" : "scissor"}

shape_score = {"rock" : 1, "paper" : 2, "scissor" : 3}
result_score = {"lose" : 0, "draw" : 3, "win" : 6}

def game_result_p2(shapes):
    if shapes[0] == shapes[1]:
        return "draw"
    elif shapes[1] == "paper":
        if shapes[0] == "rock":
            return "win"
        else:
            return "lose"
    elif shapes[1] == "scissor":
        if shapes[0] == "paper":
            return "win"
        else:
            return "lose"
    elif shapes[1] == "rock":
        if shapes[0] == "scissor":
            return "win"
        else:
            return "lose"

#for part 2
p2_strat = {"X" : "lose",
            "Y" : "draw",
            "Z" : "win"}

def choose_shape(strat, p1):
    if strat ==  "draw":
        return p1
    else:
        for shape in ["rock", "paper", "scissor"]:
            if game_result_p2([p1, shape]) == strat:
                return shape

#part 1 solution
scores = []
with open("day_2_input.txt", "r") as file:
    for line in file.read().splitlines():
        play = line.split(" ")
        shapes = [p1[play[0]], p2[play[1]]]
        result = game_result_p2(shapes)
        tot_score = result_score[result] + shape_score[shapes[1]]
        scores.append(tot_score)
print(f"Sum of scores (part 1): {sum(scores)}") #11449

#part 2 solution
scores_2 = []
with open("day_2_input.txt", "r") as file:
    for line in file.read().splitlines():
        play = line.split(" ")
        p1_shape = p1[play[0]]
        strat = p2_strat[play[1]]
        p2_shape = choose_shape(strat, p1_shape)
        #print(p1_shape, p2_shape, strat)
        tot_score = result_score[strat] + shape_score[p2_shape]
        scores_2.append(tot_score)
print(f"Sum of scores (part 2): {sum(scores_2)}") #13187
