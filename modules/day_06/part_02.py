"""Code to solve part 02 of day 06"""
import numpy as np
from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(list(line.strip()))
    return all_lines


def turn_90_degrees(direction):
    if direction == Direction.LEFT:
        return Direction.UP
    else:
        return Direction(direction.value + 1)


def find_initial_position():
    possible_directions = [(Direction.UP, '^'), (Direction.RIGHT, '>'), (Direction.DOWN, 'v'), (Direction.LEFT, '<')]
    for direction in possible_directions:
        location = np.where(guard_map == direction[1])
        if len(location[0]) > 0:
            return direction[0], (int(location[0][0]), int(location[1][0]))


def has_object(row, column):
    matches = [True for i in range(0, len(objects[0])) if objects[0][i] == row and objects[1][i] == column]
    if len(matches) > 0:
        return True
    return False

def detect_loop(prev_location, cur_location, steps):
    matches = [True for i in range(0, len(trace)-steps) if trace[i][0] == prev_location and trace[i+steps][0] == cur_location]
    return len(matches) > 1

def traverse(direction, from_location):
    # Same column, row index smaller than current location
    if direction == Direction.UP:
        for row in range(from_location[0], -1, -1):
            if has_object(row, from_location[1]):
                return True, row + 1, from_location[1], Direction.RIGHT
            mark_position(row, from_location[1], Direction.UP)
    # # same row, column index greater than current location
    elif direction == Direction.RIGHT:
        for col in range(from_location[1], len(guard_map[0])):
            if has_object(from_location[0], col):
                return True, from_location[0], col - 1, Direction.DOWN
            mark_position(from_location[0], col, Direction.RIGHT)
    # # same column, row index greater than current location
    elif direction == Direction.DOWN:
        for row in range(from_location[0], len(guard_map[1])):
            if has_object(row, from_location[1]):
                return True, row - 1, from_location[1], Direction.LEFT
            mark_position(row, from_location[1], Direction.DOWN)
    # # same row, column index smaller than current location
    else:
        for col in range(from_location[1], -1, -1):
            if has_object(from_location[0], col):
                return True, from_location[0], col + 1, Direction.UP
            mark_position(from_location[0], col, Direction.LEFT)
    return False, None, None, None


def mark_position(row, col, direction):
    guard_map[row][col] = 'X'
    trace.append([[row,col], direction])

guard_map = np.array(read_file('input'))
original_map = guard_map.copy()
current_direction, current_location = find_initial_position()
start_position = [current_location[0], current_location[1]]
objects = np.where(guard_map == '#')

# Create Trace of visited path of Guard (Assume no loop initially)
trace = list()
collision_detected = True
while collision_detected:
    result = traverse(current_direction, current_location)
    previous_length = len(trace)
    collision_detected = result[0]
    previous_location = current_location
    current_location = result[1], result[2]
    current_direction = result[3]

#Re-initialize
possible_obstructions = 0
guard_map = original_map.copy()

path = trace.copy()
for i in range(0, len(path) - 1):
    if path[i+1][0] == start_position or len([p for p in path[0:i+1] if p[0] == path[i+1][0]]) > 0:
        continue
    #Place an object next on the path
    guard_map[path[i+1][0][0]][path[i+1][0][1]] = '#'
    #re-calculate objects list
    objects = np.where(guard_map == '#')
    current_location = path[i][0]
    current_direction = path[i][1]
    collision_detected = True
    loop_detected = False
    trace = list()
    previous_length = 0
    while collision_detected and not loop_detected:
        result = traverse(current_direction, current_location)
        steps = len(trace) - previous_length
        previous_length = len(trace)
        collision_detected = result[0]
        previous_location = current_location
        current_location = result[1], result[2]
        current_direction = result[3]
        loop_detected = detect_loop([previous_location[0],previous_location[1]], [current_location[0], current_location[1]], steps)

    if loop_detected:
        print(path[i+1])
    possible_obstructions = possible_obstructions + 1 if loop_detected else possible_obstructions
    guard_map = original_map.copy()

print(possible_obstructions)
