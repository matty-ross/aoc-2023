with open('src/6/input.txt', 'r') as fp:
    time = int(fp.readline().replace('Time:', '').replace(' ', ''))
    distance = int(fp.readline().replace('Distance:', '').replace(' ', ''))
    
w = 0
for t in range(time + 1):
    d = t * (time - t)
    if d > distance:
        w += 1

print(w)