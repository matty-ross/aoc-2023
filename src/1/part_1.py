with open('src/1/input.txt', 'r') as fp:
    lines = fp.readlines()

s = 0
for line in lines:
    for c in line:
        if c.isdigit():
            l = c
            break
    for c in line[::-1]:
        if c.isdigit():
            r = c
            break
    s += int(l + r)

print(s)