DIGITS = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

def get_digit_left(line: str, pos: int) -> int:
    for k, v in DIGITS.items():
        if line[pos:pos + len(k)] == k:
            return v
    return None

def get_digit_right(line: str, pos: int) -> int:
    for k, v in DIGITS.items():
        if line[pos - len(k):pos] == k:
            return v
    return None


with open('src/1/input.txt', 'r') as fp:
    lines = fp.readlines()

s = 0
for line in lines:
    for i in range(len(line)):
        if line[i].isdigit():
            l = line[i]
            break
        d = get_digit_left(line, i)
        if d is not None:
            l = d
            break
    for i in range(len(line))[::-1]:
        if line[i].isdigit():
            r = line[i]
            break
        d = get_digit_right(line, i)
        if d is not None:
            r = d
            break
    s += int(l + r)

print(s)