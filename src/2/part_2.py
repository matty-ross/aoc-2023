def get_min_cubes(games: str) -> (int, int, int):
    r, g, b = None, None, None
    for game in games.split('; '):
        cubes = game.split(', ')
        for cube in cubes:
            count, color = cube.split(' ')
            count = int(count)
            if color == 'red' and (r is None or r < count):
                r = count
            if color == 'green' and (g is None or g < count):
                g = count
            if color == 'blue' and (b is None or b < count):
                b = count
    return r, g, b


with open('src/2/input.txt', 'r') as fp:
    lines = fp.readlines()

s = 0
for line in lines:
    _, games = line[:-1].split(': ')
    r, g, b = get_min_cubes(games)
    s += r * g * b
        
print(s)