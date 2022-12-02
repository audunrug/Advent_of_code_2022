#Part 1
p1 = {"A" : "rock",
      "B" : "paper",
      "C" : "scissor"}

p2 = {"X" : "rock",
      "Y" : "paper",
      "Z" : "scissor"}

shape_score = {"rock" : 1,
               "paper" : 2,
               "scissor" : 3}

result_score = {"lose" : 0,
                "draw" : 3,
                "win" : 6}

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

scores = []
with open("day_2_input.txt", "r") as file:
    for line in file.read().splitlines():
        play = line.split(" ")
        shapes = [p1[play[0]], p2[play[1]]]
        result = game_result_p2(shapes)
        tot_score = result_score[result] + shape_score[shapes[1]]
        scores.append(tot_score)

print(f"Sum of scores: {sum(scores)}")
