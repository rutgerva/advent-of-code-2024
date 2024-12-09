"""Code to solve part 01 of day 08"""
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

def is_inbounds(x, y, grid):
    return 0 < x < len(grid) and 0 < y < len(grid[0])
def is_antenna(c):
    pattern = r'^[a-zA-Z0-9]$'
    return re.match(pattern, c)

grid = read_file('example_input')
antennas = list()
for j in range(0, len(grid)):
    for i in range(0, len(grid[j])):
        if is_antenna(grid[i][j]):
            antennas.append([grid[i][j], i, j])
[antenna in antennas if antenna[0] == '0']


print(antennas)