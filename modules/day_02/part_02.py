"""Code to solve part 02 of day 02"""
import re
from enum import Enum

class LevelTrend(Enum):
    INCREASING = 1
    DECREASING = 2
    EQUAL = 3
    NONE = 4
def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line)
    return all_lines

def get_trend(first, second):
    """Method retrieves trend from a pair"""
    if first > second:
        return LevelTrend.DECREASING
    if second > first:
        return LevelTrend.INCREASING
    return LevelTrend.EQUAL

def is_safe(list_of_pairs):
    trend = LevelTrend.NONE
    for first, second in list_of_pairs:
        if abs(first - second) > 3:
            return False
        if trend == LevelTrend.NONE:
            trend = get_trend(first, second)
        if trend == LevelTrend.EQUAL:
            return False
        if trend != get_trend(first, second):
            return False
    return True

RESULT = 0
for line in read_file('input'):
    line_as_numbers = re.split('\s+', line.strip())
    levels = len(line_as_numbers)
    attempt = 0
    while True:
        if attempt != 0:
            line_as_numbers = re.split('\s+', line.strip())
            del line_as_numbers[attempt-1]
        pairs = []
        for i in range(len(line_as_numbers) - 1):
            pairs.append((int(line_as_numbers[i]), int(line_as_numbers[i + 1])))
        if is_safe(pairs):
            RESULT += 1
            break
        if attempt == levels:
            break
        attempt += 1
print(RESULT)
