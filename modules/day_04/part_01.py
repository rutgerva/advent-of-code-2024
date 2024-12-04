"""Code to solve part 01 of day 04"""
import numpy as np

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(list(line.strip()))
    return all_lines

def get_all_diagonals(matrix):
    diagonals = []
    rows, cols = len(matrix), len(matrix[0])

    # Top-left to bottom-right diagonals
    for d in range(-(rows - 1), cols):  # diagonals can start from -rows+1 to cols-1
        diagonal = [matrix[i][i - d] for i in range(max(0, d), min(rows, cols + d))]
        diagonals.append(diagonal)

    # Top-right to bottom-left diagonals
    for d in range(rows + cols - 1):
        diagonal = [matrix[i][d - i] for i in range(max(0, d - cols + 1), min(rows, d + 1))]
        diagonals.append(diagonal)

    return diagonals

def count_xmas_occurrences(arr):
    count = 0
    for i in range(len(arr)):
        line = ''.join(arr[i])
        count += line.count('XMAS')
        count += line.count('SAMX')
    return  count

out = read_file('input')

arr = np.array(list(out))
RESULT = 0
RESULT+= count_xmas_occurrences(arr)

arr = np.array(list(out)).transpose()
RESULT += count_xmas_occurrences(arr)

arr = get_all_diagonals(out)
RESULT += count_xmas_occurrences(arr)

print(RESULT)
