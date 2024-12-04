"""Code to solve part 02 of day 04"""
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

def is_x_mas(matrix, row, col):
    l_to_r = str(matrix[row - 1][col - 1] + matrix[row][col] + matrix[row + 1 ][col + 1])
    r_to_l = str(matrix[row - 1][col + 1] + matrix[row][col] + matrix[row + 1 ][col - 1])
    if matrix[row][col] == 'A':
        if (l_to_r == 'SAM' or l_to_r == 'MAS') and (r_to_l == 'SAM' or r_to_l == 'MAS'):
            return True
    return False
lines = np.array(read_file('input'))
RESULT = 0
# avoid outer bound to eliminate OOB-ing
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[0])-1):
        RESULT = RESULT + 1 if is_x_mas(lines, i, j) else RESULT

print(RESULT)
