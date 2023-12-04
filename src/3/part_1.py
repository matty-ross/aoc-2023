def extract_numbers(lines: list[str]) -> list:
    numbers = []
    for y, line in enumerate(lines):
        start, end = None, None
        for x, c in enumerate(line):
            if c.isdigit():
                if start is None:
                    start = (x, y)
            else:
                if start is not None:
                    end = (x - 1, y)
                    numbers.append((start, end))
                    start, end = None, None
    return numbers


def is_number_part(lines: list, numbers: list, number: tuple) -> bool:
    y = number[0][1]
    start_x = number[0][0]
    end_x = number[1][0]
    for x in range(start_x, end_x + 1):
        if y > 0:
            if lines[y - 1][x] != '.':
                return True
        if y < len(lines) - 1:
            if lines[y + 1][x] != '.':
                return True
    if start_x > 0:
        if lines[y][start_x - 1] != '.':
            return True
    if end_x < len(lines[y]) - 1:
        if lines[y][end_x + 1] != '.':
            return True
    if start_x > 0 and y > 0:
        if lines[y - 1][start_x - 1] != '.':
            return True
    if start_x > 0 and y < len(lines) - 1:
        if lines[y + 1][start_x - 1] != '.':
            return True
    if end_x < len(lines[y]) - 1 and y > 0:
        if lines[y - 1][end_x + 1] != '.':
            return True
    if end_x < len(lines[y]) - 1 and y < len(lines) - 1:
        if lines[y + 1][end_x + 1] != '.':
            return True
    return False


def get_numeric_number(lines: list, number: tuple) -> int:
    y = number[0][1]
    start_x = number[0][0]
    end_x = number[1][0]
    return int(lines[y][start_x:end_x + 1])


with open('src/3/input.txt', 'r') as fp:
    lines = fp.readlines()

s = 0
numbers = extract_numbers(lines)
for number in numbers:
    if is_number_part(lines, numbers, number):
        n = get_numeric_number(lines, number)
        s += n
        print(n)

print(s)