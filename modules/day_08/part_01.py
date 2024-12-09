"""Code to solve part 01 of day 08"""
import re
import numpy as np
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
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])
def is_antenna(c):
    pattern = r'^[a-zA-Z0-9]$'
    return re.match(pattern, c)

grid = np.array(read_file('input'))
antennas = list()
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if is_antenna(grid[i][j]):
            antennas.append([grid[i][j], int(j), int(i)])
antinodes = list()
for i in range(len(antennas)):
    frequency = antennas[i][0]
    for antenna in antennas[i + 1:]:
        if antenna[0] == frequency:
            dist_x = antenna[1] - antennas[i][1]
            dist_y = antenna[2] - antennas[i][2]
            node_1_x = antennas[i][1] - dist_x
            node_1_y = antennas[i][2] - dist_y
            node_2_x = antenna[1] + dist_x
            node_2_y = antenna[2] + dist_y
            antinodes.append([node_1_x, node_1_y]) if is_inbounds(node_1_x, node_1_y, grid) and [node_1_x, node_1_y] not in antinodes else None
            antinodes.append([node_2_x, node_2_y]) if is_inbounds(node_2_x, node_2_y, grid) and [node_2_x, node_2_y] not in antinodes else None

print(len(antinodes))