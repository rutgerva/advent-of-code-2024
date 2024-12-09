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

def calculate_antinodes_resonance(res_factor, x1, y1, x2, y2):
    d_x = (x2 - x1) * res_factor
    d_y = (y2 - y1) * res_factor

    n_1_x = antennas[i][1] - d_x
    n_1_y = antennas[i][2] - d_y
    n_2_x = antenna[1] + d_x
    n_2_y = antenna[2] + d_y
    return n_1_x, n_1_y, n_2_x, n_2_y

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
            resonance_factor = 0
            node_1_x, node_1_y, node_2_x, node_2_y = calculate_antinodes_resonance(resonance_factor,antennas[i][1],antennas[i][2],antenna[1],antenna[2])
            resonance_factor += 1
            while is_inbounds(node_1_x, node_1_y, grid) or is_inbounds(node_2_x, node_2_y, grid):
                antinodes.append([node_1_x, node_1_y]) if is_inbounds(node_1_x, node_1_y, grid) and [node_1_x, node_1_y] not in antinodes else None
                antinodes.append([node_2_x, node_2_y]) if is_inbounds(node_2_x, node_2_y, grid) and [node_2_x, node_2_y] not in antinodes else None
                node_1_x, node_1_y, node_2_x, node_2_y = calculate_antinodes_resonance(resonance_factor, antennas[i][1],antennas[i][2], antenna[1],antenna[2])
                resonance_factor += 1

print(len(antinodes))