"""Code to solve part 01 of day 13"""
import numpy as np
import re

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line.strip())
    return all_lines

def is_integer(number):
    return np.isclose(number, np.round(number))

count = 1
button_a = None
button_b = None
prize = None
file = read_file('input')
total_tokens = 0
for line in file:
    if count == 1:
        numbers = re.findall(r'\d+', line)
        button_a = {"x": int(numbers[0]), "y": int(numbers[1])}
    elif count == 2:
        numbers = re.findall(r'\d+', line)
        button_b = {"x": int(numbers[0]), "y": int(numbers[1])}
    elif count == 3:
        numbers = re.findall(r'\d+', line)
        prize = {"x": int(numbers[0]), "y": int(numbers[1])}
    else:
        A = np.array([[button_a["x"], button_b["x"]], [button_a["y"], button_b["y"]]])
        B = np.array([prize["x"], prize["y"]])
        solution = np.linalg.solve(A, B)
        if is_integer(solution[0]) and is_integer(solution[1]):
            total_tokens += ((3 * solution[0]) + solution[1])
    count = count + 1 if count < 4 else 1

print(total_tokens)

