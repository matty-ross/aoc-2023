def get_prev_value(history: list[int]) -> int:
    differences_list = []
    prev_history = history
    while True:
        differences = []
        for i in range(len(prev_history) - 1):
            d = prev_history[i + 1] - prev_history[i]
            differences.append(d)
        differences_list.append(differences)
        if all(d == 0 for d in differences):
            break
        prev_history = differences
    
    differences_list[-1].insert(0, 0)
    for i in reversed(range(1, len(differences_list))):
        d = differences_list[i - 1][0] - differences_list[i][0]
        differences_list[i - 1].insert(0, d)
    
    return history[0] - differences_list[0][0]


with open('src/9/input.txt', 'r') as fp:
    lines = fp.readlines()

s = 0
for line in lines:
    history = [int(n) for n in line.strip().split(' ')]
    s += get_prev_value(history)

print(s)