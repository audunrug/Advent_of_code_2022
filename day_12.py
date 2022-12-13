import numpy as np

class map():
    def __init__(self, grid, h_vals):
        s, e = np.where(grid == 'S'), np.where(grid == 'E')
        s, e = (s[0][0], s[1][0]), (e[0][0], e[1][0])
        self.start, self.end = s, e
        paths = {}
        for r in range(len(grid[:,0])):
            for c in range(len(grid[0,:])):
                to_paths = []
                for adj in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                    if adj[0] >= 0 and adj[1] >= 0:
                        if (adj[0] < len(grid[:,0])) and (adj[1] < len(grid[0,:])):
                            if h_vals[grid[adj[0],adj[1]]] - h_vals[grid[r,c]] <= 1:
                                to_paths.append(adj)
                paths[(r, c)] = to_paths
        self.paths = paths
        self.grid = grid

def find_route(map, start=None):
    if not start:
        start = map.start
    travelled = {start: 0}
    parent = {}
    queue, current = [start], 0
    while current != map.end:
        current = queue.pop(0)
        for next in map.paths[current]:
            if next not in travelled:
                parent[next] = current
                travelled[next] = travelled[parent[next]] + 1
                queue.append(next)
        if len(queue) == 0:
            break
    if map.end in travelled.keys():
        return travelled, parent
    else:
        return False

#visualizing
def walk_back(map, parents, pos, start):
    #map.grid[pos[0],pos[1]] = map.grid[pos[0],pos[1]].upper()
    if parents[pos][0] < pos[0]:
        sym= "⌄"
    elif parents[pos][0] > pos[0]:
        sym= "^"
    elif parents[pos][1] < pos[1]:
        sym= ">"
    elif parents[pos][1] > pos[1]:
        sym= "<"
    map[pos[0],pos[1]] = sym
    next_pos = parents[pos]
    if next_pos != start:
        walk_back(map, parents, next_pos, start)
    return map

height, n = {'S':0}, 0
for c in 'abcdefghijklmnopqrstuvwxyzE':
    height[c] = n
    n += 1

input_lines = np.loadtxt("inputs/day_12_input.txt", dtype='str')
input_grid = np.array([list(line) for line in input_lines])
elf_map = map(input_grid, height)

travelled, parents = find_route(elf_map)
walkback = walk_back(elf_map.grid.copy(), parents, elf_map.end, elf_map.start)
np.savetxt("walkback_day12.txt", walkback.astype("str"), fmt='%s', delimiter="")
print(travelled[elf_map.end])
print(elf_map.start)
print("")
#part 2
best_path, pos = 100000, (0,0)
for r in range(len(elf_map.grid[:,0])):
    for c in range(len(elf_map.grid[0,:])):
        if elf_map.grid[r,c] == 'a':
            if find_route(elf_map, start=(r,c)):
                print(r,c, best_path)
                trav, parents = find_route(elf_map, start=(r,c))
                path_length = trav[elf_map.end]
                if path_length < best_path:
                    best_path = path_length
                    a_pos = (r,c)
                    best_parents = parents
            else:
                print("route not found")

walkback_2 = walk_back(elf_map.grid.copy(), best_parents, elf_map.end, a_pos)
np.savetxt("walkback-2_day12.txt", walkback_2.astype("str"), fmt='%s', delimiter="")
print(best_path)
