def replace_spaces(nums: str) -> str:
    while '  ' in nums:
        nums = nums.replace('  ', ' ')
    return nums.strip()


def get_points(winning_nums: list[int], your_nums: list[int]) -> int:
    points = 0
    for your_num in your_nums:
        if your_num in winning_nums:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points


with open('src/4/input.txt', 'r') as fp:
    lines = fp.readlines()

s = 0
for i, line in enumerate(lines):
    start_post = line.find(':')
    line = line[start_post + 2:-1]
    winning_nums, your_nums = line.split(' | ')
    winning_nums = replace_spaces(winning_nums).split(' ')
    your_nums = replace_spaces(your_nums).split(' ')
    s += get_points(winning_nums, your_nums)

print(s)