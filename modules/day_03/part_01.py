"""Code to solve part 01 of day 03"""
import re

with open('input') as file:
    memory = file.read()

pattern = r"\w*mul\((-?\d*),(-?\d*)\)"
matches = re.findall(pattern, memory)
RESULT = 0
for match in matches:
    RESULT += (int(match[0]) * int(match[1]))

print(RESULT)
