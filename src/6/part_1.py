def replace_spaces(line: str) -> str:
    while '  ' in line:
        line = line.replace('  ', ' ')
    return line.strip()


with open('src/6/input.txt', 'r') as fp:
    time = [int(t) for t in replace_spaces(fp.readline().replace('Time:', '')).split()]
    distance = [int(d) for d in replace_spaces(fp.readline().replace('Distance:', '')).split()]

ways = []
for i in range(len(time)):
    w = 0
    for t in range(time[i] + 1):
        d = t * (time[i] - t)
        if d > distance[i]:
            w += 1
    ways.append(w)

if len(ways) > 1:
    p = 1
    for w in ways:
        p *= w
    print(p)
else:
    print(0)