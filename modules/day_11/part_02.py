"""Code to solve part 01 of day 11"""
from functools import lru_cache

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line.strip().split(" "))
    return all_lines

@lru_cache(maxsize=None)
def blink(s):
    if s == '0':
        return ['1']
    elif len(s) % 2 == 0:
        half = int(len(s) / 2)
        return [s[0:half] , str(int(s[half:]))]
    else:
        return [str(int(s) * 2024)]

@lru_cache(maxsize=None)
def process_stone(stones, itterations):
    if itterations == 0:
        return len(stones.split(","))
    total = 0
    for s in stones.split(","):
        total += process_stone(",".join(blink(s)), itterations-1)

    return total



all_stones = read_file('input')[0]

RESULT = 0


for stone in all_stones:
    # print(process_stone(stone, 25))
    RESULT += process_stone(stone, 75)

print(RESULT)