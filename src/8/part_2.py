with open('src/8/input.txt', 'r') as fp:
    directions = fp.readline().strip()
    fp.readline() # empty line
    lines = fp.readlines()

current_nodes = []
nodes = {}
for line in lines:
    node, branches = line.strip().split(' = ')
    l, r = branches[1:-1].split(', ')
    nodes[node] = (l, r)
    if node[-1] == 'A':
        current_nodes.append(node)

i = 0
while not all(c[-1] == 'Z' for c in current_nodes):
    direction = directions[i % len(directions)]
    for j in range(len(current_nodes)):
        if direction == 'L':
            current_nodes[j] = nodes[current_nodes[j]][0]
        elif direction == 'R':
            current_nodes[j] = nodes[current_nodes[j]][1]
    i += 1

print(i)