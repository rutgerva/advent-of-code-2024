"""Code to solve part 02 of day 10"""
import numpy as np

MAX_HEIGHT = 9

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append([c for c in line.strip()])
    return all_lines

def valid_move(cur_x, cur_y, dest_x, dest_y):
    if cur_x == dest_x:
        return cur_y == dest_y - 1 or cur_y == dest_y + 1
    elif cur_y ==  dest_y:
        return cur_x == dest_x - 1 or cur_x == dest_x + 1
    else:
        return False

def find_valid_paths(cur_x, cur_y, next_height, topo_map):
    if next_height > MAX_HEIGHT:
        return 1
    next_height_y, next_height_x = np.where(topo_map == str(next_height)) # get positions of all coordinates with the next height
    potential_paths = [[next_height_x[i], next_height_y[i]] for i in range(0, len(next_height_x)) if valid_move(cur_x, cur_y, next_height_x[i], next_height_y[i])] # check for potential paths (up, down, left or right from current pos)
    if len(potential_paths) != 0:
        paths = 0
        for path in potential_paths:
            paths += find_valid_paths(path[0], path[1], next_height + 1, topo_map)
        return paths
    else:
        return 0 #stop condition, no next step possible

topographic_map = np.array(read_file('input'))

start_y, start_x = np.where(topographic_map == '0')


result = 0
for i in range(0, len(start_y)):
    result += find_valid_paths(start_x[i], start_y[i], 1, topographic_map)

print(result)
