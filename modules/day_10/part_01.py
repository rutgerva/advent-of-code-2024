"""Code to solve part 01 of day 10"""
import numpy as np

MAX_HEIGHT = 9
ENDS_REACHED = list()
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
        global ENDS_REACHED
        if [cur_x, cur_y] not in ENDS_REACHED:
            ENDS_REACHED.append([cur_x, cur_y])
    next_height_y, next_height_x = np.where(topo_map == str(next_height)) # get positions of all coordinates with the next height
    potential_paths = [[next_height_x[i], next_height_y[i]] for i in range(0, len(next_height_x)) if valid_move(cur_x, cur_y, next_height_x[i], next_height_y[i])] # check for potential paths (up, down, left or right from current pos)
    if len(potential_paths) != 0:
        for path in potential_paths:
            find_valid_paths(path[0], path[1], next_height + 1, topo_map)
    # else:
    #     return [] #stop condition, no next step possible

# def find_paths(startx, starty, topo_map):
#     next_height = 1
#     next_height_x, next_height_y = np.where(topo_map == str(next_height))
#     potential_path = [[next_height_x[i], next_height_y[i]] for i in range(0, len(next_height_x)) if valid_move(startx, starty, next_height_x[i], next_height_y[i])]
#     while next_height < MAX_HEIGHT and len(potential_path) > 0:
#         next_height +=1
#     #     next_height_x, next_height_y = np.where(topo_map == str(next_height))
#     #     next_height += 1
#     return -1

topographic_map = np.array(read_file('input'))

start_y, start_x = np.where(topographic_map == '0')
result = 0
for i in range(0, len(start_y)):
    ENDS_REACHED = list()
    find_valid_paths(start_x[i], start_y[i], 1, topographic_map)
    result += len(ENDS_REACHED)

print(result)
