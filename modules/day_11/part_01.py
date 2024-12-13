"""Code to solve part 01 of day 11"""
import threading
import os
from functools import cache
def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line.strip().split(" "))
    return all_lines

def blink(stones):
    stones_after_blink = list()
    for stone in stones:
        if stone == '0':
            stones_after_blink.append('1')
        elif len(stone) % 2 == 0:
            half = int(len(stone) / 2)
            stones_after_blink.append(stone[0:half])
            stones_after_blink.append(str(int(stone[half:])))
        else:
            stones_after_blink.append(str(int(stone) * 2024))

    return stones_after_blink

alligned_stones = read_file('example_input')[0]
for i in range(0, 10):
    alligned_stones = blink(alligned_stones)
    print(alligned_stones)


