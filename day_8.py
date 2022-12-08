import numpy as np

with open("inputs/day_8_input.txt", "r") as file:
    lines = file.read().splitlines()

tree_matrix = np.array([list(map(int, list(line))) for line in lines])

#part 1
cols, rows = len(tree_matrix[:,0]), len(tree_matrix[0,:])
counts = np.zeros((cols, rows), dtype=int)
counts[0,:], counts[-1,:], counts[:,0], counts[:,-1] = 1, 1, 1, 1
for i in range(1, rows-1):
    for n in range(1, cols-1):
        height = tree_matrix[i,n]
        ii, nn = i+1, n+1
        l_max, r_max  = max(tree_matrix[:i,n]), max(tree_matrix[ii:,n])
        u_max, d_max = max(tree_matrix[i,:n]), max(tree_matrix[i,nn:])
        if height > min([l_max, r_max, u_max, d_max]):
            counts[i,n] = 1
print(f"Number of visible trees (p1): {counts.sum()}") #1690

#part 2
view_matrix = np.zeros((cols, rows), dtype=int)
for i in range(1, (rows-1)):
    for n in range(1, (cols-1)):
        height = tree_matrix[i,n]
        ii, nn = i+1, n+1
        up, down = np.flip(tree_matrix[:i,n]), tree_matrix[ii:,n]
        left, right = np.flip(tree_matrix[i,:n]), tree_matrix[i,nn:]
        view_scores = []
        for view in [right, left, up, down]:
            if tree_matrix[i,n] > max(view):
                view_scores.append(len(view))
            else:
                for v in range(len(view)):
                    if view[v] >= height:
                        view_scores.append(v+1)
                        break
        view_matrix[i,n] = np.prod(view_scores)
print(f"Highest scenic score (p2): {np.max(view_matrix)}") #535680
