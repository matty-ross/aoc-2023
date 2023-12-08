with open('src/8/input.txt', 'r') as fp:
    directions = fp.readline().strip()
    fp.readline() # empty line
    lines = fp.readlines()

nodes = {}
for line in lines:
    node, branches = line.strip().split(' = ')
    l, r = branches[1:-1].split(', ')
    nodes[node] = (l, r)

curr_node = 'AAA'
i = 0
while curr_node != 'ZZZ':
    direction = directions[i % len(directions)]
    if direction == 'L':
        curr_node = nodes[curr_node][0]
    elif direction == 'R':
        curr_node = nodes[curr_node][1]
    i += 1

print(i)