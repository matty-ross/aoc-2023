def is_game_possible(games: str) -> bool:
    for game in games.split('; '):
        cubes = game.split(', ')
        for cube in cubes:
            count, color = cube.split(' ')
            if color == 'red' and int(count) > 12:
                return False
            if color == 'green' and int(count) > 13:
                return False
            if color == 'blue' and int(count) > 14:
                return False
    return True


with open('src/2/input.txt', 'r') as fp:
    lines = fp.readlines()

s = 0
for line in lines:
    game_id, games = line[:-1].split(': ')
    if is_game_possible(games):
        s += int(game_id.split(' ')[1])
        
print(s)